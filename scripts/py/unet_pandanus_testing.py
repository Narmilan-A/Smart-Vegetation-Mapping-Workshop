# Import general python libraries
import numpy as np
import os
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
from skimage import exposure
from scipy.ndimage import convolve

# Import the GDAL module from the osgeo package
from osgeo import gdal

# Import necessary functions from scikit-learn
from sklearn.metrics import confusion_matrix, classification_report

# Import necessary functions and classes from Keras
from keras.utils import to_categorical
from keras.models import load_model
#-------------------------------------------------------------------------------------------------------------#
# Define the function for normalisation of vegetation indices
def post_idx_calc(index, normalise):
    # Replace nan with zero and inf with finite numbers
    idx = np.nan_to_num(index)
    if normalise:
        return cv2.normalize(
            idx, None, alpha=0.0, beta=1.0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    else:
        return idx
#-------------------------------------------------------------------------------------------------------------#
# Define function to calculate vegetation indices
def calculate_veg_indices(input_img):
# Extract the all channels from the input image
    RedEdge = input_img[:, :, 3]
    nir = input_img[:, :, 4]
    red = input_img[:, :, 2]
    green = input_img[:, :, 1]
    blue = input_img[:, :, 0]

# Define all the vegetation indices
    # Calculate vegetation indices
    ndvi = post_idx_calc((nir - red) / (nir + red),normalise=False)
    dvi = post_idx_calc((nir - red),normalise=False)
    tvi = post_idx_calc((60*(nir - green)) - (100 * (red - green)),normalise=False)
    gdvi = post_idx_calc((nir - green),normalise=False)
    endvi = post_idx_calc(((nir + green) - (2 * blue)) / ((nir + green) + (2 * blue)),normalise=False)

    veg_indices = np.stack((ndvi, dvi, tvi, gdvi, endvi), axis=2)

    return veg_indices
#-------------------------------------------------------------------------------------------------------------#
# Define a function to get the width and height of an image using GDAL (If required)
def get_image_dimensions(file_path):
    ds = gdal.Open(file_path)
    if ds is not None:
        width = ds.RasterXSize
        height = ds.RasterYSize
        return width, height
    return None, None

# Minimum width and height for filtering
min_width = 256
min_height = 256
max_width = 2000
max_height = 2000
#-------------------------------------------------------------------------------------------------------------#
# Define the tile size and overlap percentage
tile_size = 256
overlap = int(tile_size * 0.3)
#-------------------------------------------------------------------------------------------------------------#
# Define the root directory with input images and respective masks
root_data_folder = r'/home/n10837647/pandanus_classification'
root_image_folder = r'/home/n10837647/pandanus_classification/msi_image_mask_rois/testing'
root_model_folder =os.path.join(root_data_folder, 'model&outcomes')
#-------------------------------------------------------------------------------------------------------------#
# Load unet model
unet_model = load_model(os.path.join(root_model_folder,'save_best_model.hdf5'))
print("Model loaded")
#-------------------------------------------------------------------------------------------------------------#
# Store the tiled images and masks
image_patches = []
mask_patches = []

# Define a function to get the width and height of an image using GDAL
def get_image_dimensions(file_path):
    ds = gdal.Open(file_path)
    if ds is not None:
        width = ds.RasterXSize
        height = ds.RasterYSize
        return width, height
    return None, None

# Specify the folder paths for images and masks
image_folder_path = os.path.join(root_image_folder, 'msi_rois')
mask_folder_path = os.path.join(root_image_folder, 'msi_mask_rois')

# Filter image and mask files based on dimensions
filtered_image_files = []
filtered_mask_files = []

input_img_folder = os.path.join(root_image_folder, 'msi_rois')
input_mask_folder = os.path.join(root_image_folder, 'msi_mask_rois')

img_files = [file for file in os.listdir(input_img_folder) if file.endswith(".tif")]
mask_files = [file for file in os.listdir(input_mask_folder) if file.endswith(".tif")]

# Iterate through the image files
for img_file in img_files:
    img_path = os.path.join(image_folder_path, img_file)
    img_width, img_height = get_image_dimensions(img_path)
    
    if img_width is not None and img_height is not None:
        if min_width <= img_width <= max_width and min_height <= img_height <= max_height:
            filtered_image_files.append(img_path)

# Iterate through the mask files
for mask_file in mask_files:
    mask_path = os.path.join(mask_folder_path, mask_file)
    mask_width, mask_height = get_image_dimensions(mask_path)
    
    if mask_width is not None and mask_height is not None:
        if min_width <= mask_width <= max_width and min_height <= mask_height <= max_height:
            filtered_mask_files.append(mask_path)

# Print the number of filtered image and mask files
print(f"Number of filtered image files: {len(filtered_image_files)}")
print(f"Number of filtered mask files: {len(filtered_mask_files)}")
#-------------------------------------------------------------------------------------------------------------#
# Sort the filtered files to ensure consistent ordering
filtered_image_files.sort()
filtered_mask_files.sort()

for i in range(len(filtered_image_files)):
    img_file = os.path.basename(filtered_image_files[i])  # Get the file name without the path
    mask_file = os.path.basename(filtered_mask_files[i])  # Get the file name without the path
    
    ds_img = gdal.Open(filtered_image_files[i])
    ds_mask = gdal.Open(filtered_mask_files[i])
    width = ds_img.RasterXSize
    height = ds_img.RasterYSize

    # Calculate the number of tiles in the image
    num_tiles_x = (width - tile_size) // (tile_size - overlap) + 1
    num_tiles_y = (height - tile_size) // (tile_size - overlap) + 1

    for y in range(num_tiles_y):
        for x in range(num_tiles_x):
            # Calculate the tile coordinates
            x_start = x * (tile_size - overlap)
            y_start = y * (tile_size - overlap)
            x_end = x_start + tile_size
            y_end = y_start + tile_size

            # Extract the image tile
            input_bands = 5  # Number of input bands
            input_img = np.array([ds_img.GetRasterBand(j + 1).ReadAsArray(x_start, y_start, tile_size, tile_size) for j in range(input_bands)])
            input_img = np.transpose(input_img, (1, 2, 0))
            input_img = exposure.equalize_hist(input_img)
            
            veg_indices = calculate_veg_indices(input_img)
            input_img = np.concatenate((input_img, veg_indices), axis=2)

            input_mask = ds_mask.GetRasterBand(1).ReadAsArray(x_start, y_start, tile_size, tile_size).astype(int)
           
            image_patches.append(input_img)
            mask_patches.append(input_mask)

    print(f"Processed image: {img_file} --> Processed mask: {mask_file}")

# Convert the lists to NumPy arrays
image_patches = np.array(image_patches)
mask_patches = np.array(mask_patches)

# Print the shape of the arrays
print("image_patches.shape: {}".format(image_patches.shape))
print("mask_patches.shape: {}".format(mask_patches.shape))
#-------------------------------------------------------------------------------------------------------------#
# Save the print results to a text file
output_file = os.path.join(root_model_folder, 'testing samples.txt')
with open(output_file, "w") as file:
    file.write("image_patches.shape: {}\n".format(image_patches.shape))
    file.write("mask_patches.shape: {}\n".format(mask_patches.shape))
#-------------------------------------------------------------------------------------------------------------#
# This function takes the mask_patches data and converts it into a categorical representation. 
mask_patches_to_categorical = to_categorical(mask_patches, num_classes=2)
#-------------------------------------------------------------------------------------------------------------#
#Confusion_matrix and Classification_report
#----------------#
# Confusion_matrix
#----------------#

# Predict on the validation data
y_pred = unet_model.predict(image_patches)

# Convert the predicted and true masks to class labels
y_pred_classes = np.argmax(y_pred, axis=-1)
y_test_classes = np.argmax(mask_patches_to_categorical, axis=-1)

# Compute the confusion matrix
cm = confusion_matrix(y_test_classes.ravel(), y_pred_classes.ravel())

# Print the confusion matrix
print(cm)
# #------------------------------------------------------------------#
# Plot the confusion matrix 
labels = ['Background','Pandanous']
# Plot the confusion matrix using heatmap()
plt.figure()
sns.heatmap(cm, annot=True, cmap='Blues', fmt='d', xticklabels=labels, yticklabels=labels)
plt.title('confusion matrix_heatmap')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.savefig(os.path.join(root_model_folder, 'CM_heatmap_validation.png'), bbox_inches='tight')
plt.show()
print('Saved testing_confusion matrix_heatmap')
#------------------------------------------------------------------#
#---------------------#
# classification report
#---------------------#
cr = classification_report(y_test_classes.ravel(), y_pred_classes.ravel(), target_names=['Background','Pandanous'])
# Print the classification report
print(cr)
#------------------------------------------------------------------#
# Export confusion matrix and classification report as .txt
file_path = os.path.join(root_model_folder, 'model testing performance report.txt')
with open(file_path, 'w') as file:
    file.write("Confusion Matrix:\n")
    file.write(str(cm))
    file.write("\n\n")
    file.write("Classification Report:\n")
    file.write(cr)
print('Saved classification_and_confusion_report')
#-------------------------------------------------------------------------------------------------------------#
#IOU
# Calculate and save IoU for each class
class_iou = []
with open(file_path, 'a') as file:
    file.write("\n\nIoU Results:\n")
    for i in range(2):
        true_class = (y_test_classes == i)
        pred_class = (y_pred_classes == i)
        intersection = np.sum(true_class * pred_class)
        union = np.sum(true_class) + np.sum(pred_class) - intersection
        iou = intersection / union
        class_iou.append(iou)
        file.write("IoU for class {}: {:.2f}\n".format(i+1, iou))
        print("IoU for class {}: {:.2f}".format(i+1, iou))
# Calculate and save average IoU
average_iou = np.mean(class_iou)
with open(file_path, 'a') as file:
    file.write("Average IoU: {:.2f}".format(average_iou))
    print("Average IoU: {:.2f}".format(average_iou))
print('Saved IoU results')
#-------------------------xxxxxx------------------------------------------------------------------------------#