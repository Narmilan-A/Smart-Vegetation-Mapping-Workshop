# Import general python libraries
import numpy as np
import os
import cv2
from skimage import exposure
from scipy.ndimage import convolve
from empatches import EMPatches

# Import the GDAL module from the osgeo package
from osgeo import gdal
from osgeo.gdalconst import GDT_Byte

# Import necessary functions and classes from Keras
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
# Function to map labels to colors
def map_labels_to_colors(prediction):
    color_mapping = {
        0: [0, 255, 0],  # Green for ID 0
        1: [255, 0, 0],  # Red for ID 1
    }
    colored_image = np.zeros((prediction.shape[0], prediction.shape[1], 3), dtype=np.uint8)
    for label, color in color_mapping.items():
        mask = prediction == label
        colored_image[mask] = color
    return colored_image
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
# Load multispectral images
images = []
input_img_folder = os.path.join(root_image_folder, 'msi_rois')

# Retrieve all image
img_files = [file for file in os.listdir(input_img_folder) if file.endswith(".tif")]
#-------------------------------------------------------------------------------------------------------------#
# Prediction
patch_size = 256
total_files = len(img_files)
ignored_files = 0

for i in range(len(img_files)):
    img_file = os.path.join(input_img_folder, img_files[i])
    img_ds = gdal.Open(img_file)
    input_img = np.array(img_ds.ReadAsArray(), dtype=np.float32)
    input_img = np.transpose(input_img, (1, 2, 0))
    input_img = exposure.equalize_hist(input_img)

    veg_indices = calculate_veg_indices(input_img)
    input_img = np.concatenate((input_img, veg_indices), axis=2)

    # Check the image size
    if input_img.shape[0] < patch_size or input_img.shape[1] < patch_size:
        ignored_files += 1
        continue
#----------------------------------------------------------------------#
    # Check if both width and height are greater than patch_size
    if input_img.shape[0] >= patch_size and input_img.shape[1] >= patch_size:
        emp = EMPatches()
        img_patches, indices = emp.extract_patches(input_img, patchsize=patch_size, overlap=0.3)

        # Create patches of the desired size
        resized_patches = []
        for patch in img_patches:
            patch_height, patch_width, _ = patch.shape
            if patch_height < patch_size or patch_width < patch_size:
                target_height = max(patch_height, patch_size)
                target_width = max(patch_width, patch_size)
                resized_patch = np.zeros((target_height, target_width, patch.shape[2]), dtype=np.float32)
                resized_patch[:patch_height, :patch_width, :] = patch
            else:
                resized_patch = patch[:patch_size, :patch_size, :]
            resized_patches.append(resized_patch)

        img_patches_processed = unet_model.predict(np.array(resized_patches))
        merged_img_patches_processed = emp.merge_patches(img_patches_processed, indices, mode='min')

        # Retrieve geo information
        geotransform = img_ds.GetGeoTransform()
        projection = img_ds.GetProjection()

        # Reshape the predicted image to 2D
        pred_image = np.argmax(merged_img_patches_processed, axis=-1)

        # Create a new .dat and .hdr file for the predicted image
        driver = gdal.GetDriverByName('ENVI')
        pred_image_file = os.path.splitext(img_files[i])[0] + '_pred.dat'

        # Define the path to the "prediction" folder
        prediction_folder = os.path.join(root_model_folder, 'prediction')

        # Check if the "prediction" folder exists, and create it if it doesn't
        if not os.path.exists(prediction_folder):
            os.makedirs(prediction_folder)

        pred_image_path = os.path.join(prediction_folder, pred_image_file)

        # Create the output GDAL dataset
        pred_image_ds = driver.Create(pred_image_path, pred_image.shape[1], pred_image.shape[0], 1, gdal.GDT_Byte)

        # Write the predicted image data to the new file
        pred_image_ds.GetRasterBand(1).WriteArray(pred_image)

        # Add spatial reference information
        pred_image_ds.SetGeoTransform(geotransform)
        pred_image_ds.SetProjection(projection)

        # Close the files
        pred_image_ds = None

        print(f"Prediction.dat saved for image {img_files[i]}")
#----------------------------------------------------------------------#
        # Map labels to colors for the .tif file
        colored_prediction = map_labels_to_colors(pred_image)

        # Create the directory for the .tif file if it doesn't exist
        tif_file_directory = os.path.join(root_model_folder, 'prediction')
        if not os.path.exists(tif_file_directory):
            os.makedirs(tif_file_directory)

        # Create a new .tif file for the colored prediction image (with color mapping)
        driver = gdal.GetDriverByName('GTiff')
        pred_image_file = os.path.splitext(img_files[i])[0] + '_pred.tif'
        tif_file_path = os.path.join(tif_file_directory, pred_image_file)
        pred_image_ds = driver.Create(tif_file_path, pred_image.shape[1], pred_image.shape[0], 3, GDT_Byte)
        pred_image_ds.GetRasterBand(1).WriteArray(colored_prediction[:, :, 0])
        pred_image_ds.GetRasterBand(2).WriteArray(colored_prediction[:, :, 1])
        pred_image_ds.GetRasterBand(3).WriteArray(colored_prediction[:, :, 2])
        pred_image_ds.SetGeoTransform(geotransform)
        pred_image_ds.SetProjection(projection)
        pred_image_ds = None
        print(f"prediction.tif saved for image {img_files[i]}")
#----------------------------------------------------------------------#
print(f"Total MS ROIs: {total_files}")
print(f"Ignored MS ROIs: {ignored_files}")

print("All predictions saved.")
#-------------------------xxxxxx---------------------------------------#

#--------------------------------------------xxxxxx------------------------------------------------------------#