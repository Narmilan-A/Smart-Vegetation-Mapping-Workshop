# Import general python libraries
import numpy as np
import os
import pandas as pd
import cv2
import matplotlib.pyplot as plt
import seaborn as sns
from skimage import exposure
from scipy.ndimage import convolve
from time import time
import random
import random as python_random
import tensorflow as tf
import sys

# Import the GDAL module from the osgeo package
from osgeo import gdal

# Import necessary functions from scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

# Import necessary functions and classes from Keras
from keras.utils import to_categorical
from keras.optimizers import Adam
#from keras.losses import categorical_crossentropy
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.metrics import BinaryAccuracy, Precision, Recall, IoU, MeanIoU, FalseNegatives, FalsePositives
from keras.models import Model
from keras.layers import Input, Conv2D, MaxPooling2D, Conv2DTranspose, concatenate, Dropout, BatchNormalization
from keras.callbacks import ModelCheckpoint
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
root_data_folder = r'/content/drive/MyDrive/SCC/pandanus_classification'
root_image_folder = r'/content/drive/MyDrive/SCC/pandanus_classification/msi_image_mask_rois/training'
root_model_folder =os.path.join(root_data_folder, 'model&outcomes')
# Check if the "model&outcomes" folder exists, and create it if it doesn't
if not os.path.exists(root_model_folder):
    os.makedirs(root_model_folder)
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
# This function takes the mask_patches data and converts it into a categorical representation.
mask_patches_to_categorical = to_categorical(mask_patches, num_classes=2)
#-------------------------------------------------------------------------------------------------------------#
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(image_patches, mask_patches_to_categorical, test_size=0.25, random_state=22)
#-------------------------------------------------------------------------------------------------------------#
#save, print and confirm the model data
output_file = os.path.join(root_model_folder, 'trainng and validation samples.txt')
# Save the print results to a text file
with open(output_file, "w") as file:
    file.write("image_patches.shape: {}\n".format(image_patches.shape))
    file.write("mask_patches.shape: {}\n".format(mask_patches.shape))

# Save the model data to the text file
with open(output_file, "a") as file:
    file.write("\nX_train shape: {}\n".format(X_train.shape))
    file.write("X_test shape: {}\n".format(X_test.shape))
    file.write("y_train shape: {}\n".format(y_train.shape))
    file.write("y_test shape: {}\n".format(y_test.shape))
    file.write("Image height: {}\n".format(X_train.shape[1]))
    file.write("Image width: {}\n".format(X_train.shape[2]))
    file.write("Image channels: {}\n".format(X_train.shape[3]))

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
#-------------------------------------------------------------------------------------------------------------#
# Apply K-Fold cross validation
print ("Applying K-Fold cross validation...")
start_time = time()

cv = KFold(n_splits=10, shuffle=True, random_state=22)

# Create a list to store the best model paths and validation loss
best_model_paths = []

# K-fold Cross Validation model evaluation
fold_no = 1
acc_per_fold = [] #save accuracy from each fold
loss_per_fold = [] #save accuracy from each fold

for fold_no, (train, test) in enumerate(cv.split(X_train, y_train), 1):
    print('   ')
    print(f'Training for fold {fold_no} ...')

    n_classes = 2

    def UNet(n_classes, image_height, image_width, image_channels):
        inputs = Input((image_height, image_width, image_channels))

        seed_value = 22
        random.seed(seed_value)
        np.random.seed(seed_value)
        tf.random.set_seed(seed_value)
        python_random.seed(seed_value)

        c1 = Conv2D(64, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(inputs)
        c1 = BatchNormalization()(c1)
        c1 = Dropout(0.2)(c1)
        c1 = Conv2D(64, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(c1)
        c1 = BatchNormalization()(c1)
        p1 = MaxPooling2D((2,2))(c1)

        c2 = Conv2D(128, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(p1)
        c2 = BatchNormalization()(c2)
        c2 = Dropout(0.2)(c2)
        c2 = Conv2D(128, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(c2)
        c2 = BatchNormalization()(c2)
        p2 = MaxPooling2D((2,2))(c2)

        c3 = Conv2D(256, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(p2)
        c3 = BatchNormalization()(c3)
        c3 = Dropout(0.2)(c3)
        c3 = Conv2D(256, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(c3)
        c3= BatchNormalization()(c3)
        p3 = MaxPooling2D((2,2))(c3)

        c4 = Conv2D(512, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(p3)
        c4 = BatchNormalization()(c4)
        c4 = Dropout(0.2)(c4)
        c4 = Conv2D(512, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(c4)
        c4 = BatchNormalization()(c4)
        p4 = MaxPooling2D((2,2))(c4)

        c5 = Conv2D(1024, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(p4)
        c5 = BatchNormalization()(c5)
        c5 = Dropout(0.2)(c5)
        c5 = Conv2D(1024, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(c5)
        c5 = BatchNormalization()(c5)

        u6 = Conv2DTranspose(512, (2,2), strides=(2,2), padding="same")(c5)
        u6 = concatenate([u6, c4])
        c6 = Conv2D(512, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(u6)
        c6 = BatchNormalization()(c6)
        c6 = Dropout(0.2)(c6)
        c6 = Conv2D(512, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(c6)
        c6 = BatchNormalization()(c6)

        u7 = Conv2DTranspose(256, (2,2), strides=(2,2), padding="same")(c6)
        u7 = concatenate([u7, c3])
        c7 = Conv2D(256, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(u7)
        c7 = BatchNormalization()(c7)
        c7 = Dropout(0.2)(c7)
        c7 = Conv2D(256, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(c7)
        c7 = BatchNormalization()(c7)

        u8 = Conv2DTranspose(128, (2,2), strides=(2,2), padding="same")(c7)
        u8 = concatenate([u8, c2])
        c8 = Conv2D(128, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(u8)
        c8 = BatchNormalization()(c8)
        c8 = Dropout(0.2)(c8)
        c8 = Conv2D(128, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(c8)
        c8 = BatchNormalization()(c8)

        u9 = Conv2DTranspose(64, (2,2), strides=(2,2), padding="same")(c8)
        u9 = concatenate([u9, c1], axis=3)
        c9 = Conv2D(64, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(u9)
        c9 = BatchNormalization()(c9)
        c9 = Dropout(0.2)(c9)
        c9 = Conv2D(64, (3,3), activation="relu", kernel_initializer="he_normal", padding="same")(c9)
        c9 = BatchNormalization()(c9)

        outputs = Conv2D(n_classes, (1,1), activation="softmax")(c9)

        model = Model(inputs=inputs, outputs=outputs)
        return model
    #----------------------------------------------------------------------#
    # Create the model
    image_height = X_train.shape[1]
    image_width = X_train.shape[2]
    image_channels = X_train.shape[3]
    model=UNet(n_classes=n_classes,
                            image_height=image_height,
                            image_width=image_width,
                            image_channels=image_channels)
    #----------------------------------------------------------------------#
    #Complie the model
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss=BinaryCrossentropy(),
        metrics=[BinaryAccuracy(),Precision(class_id=1), Recall(class_id=1), IoU(num_classes=2,target_class_ids=[1]), MeanIoU(num_classes=2), FalseNegatives(), FalsePositives()])

    # Specify the filepath for where to save the weights for the best model
    best_model_path = os.path.join(root_model_folder, f'save_best_model_fold_{fold_no}.hdf5')

    # Create a ModelCheckpoint for the best model based on validation loss
    checkpoint_best_model = ModelCheckpoint(
        best_model_path,
        save_best_only=True,
        monitor='val_loss',
        mode='min'
    )

    # Train the model
    history = model.fit(X_train, y_train,
                    batch_size=30,
                    verbose=1,
                    epochs=200,
                    validation_data=(X_test, y_test),
                    shuffle=True,
                    callbacks=[checkpoint_best_model])

    best_model_paths.append(best_model_path)


    # Evaluate the model - report accuracy and capture it into a list for future reporting
    scores = model.evaluate(X_test, y_test, verbose=1)
    acc_per_fold.append(scores[1] * 100)

    scores = model.evaluate(X_test, y_test, verbose=1)
    loss_per_fold.append(scores[0])

    fold_no = fold_no + 1

# Initialize a list to store fold numbers and corresponding accuracies and loss
fold_and_acc_list = [(fold_no, acc) for fold_no, acc in enumerate(acc_per_fold, 1)]
fold_and_loss_list = [(fold_no, loss) for fold_no, loss in enumerate(loss_per_fold, 1)]

# Calculate the average val_binary_accuracy
average_accuracy = sum(acc_per_fold) / len(acc_per_fold)

# Calculate the average val_binary_accuracy
average_loss = sum(loss_per_fold) / len(acc_per_fold)

for fold_no, acc in enumerate(acc_per_fold, 1):
    print(f'Fold {fold_no} val_binary_accuracy: {acc}\n"')

for fold_no, acc in enumerate(loss_per_fold, 1):
    print(f'Fold {fold_no} val_binary_loss: {acc}\n"')

print(f"Average val_binary_accuracy across all folds: {average_accuracy}\n")
print(f"Average val_binary_loss across all folds: {average_loss}\n")

# Calculate and print the training time
end_time = time()
training_time = end_time - start_time
print(f"Training time: {training_time} seconds")

# Export confusion matrix and classification report as .txt
file_path = os.path.join(root_model_folder, 'K_Fold_outcome report.txt')
with open(file_path, 'w') as file:
    file.write(f"Training Time: {training_time} seconds\n")
    for fold_no, acc in fold_and_acc_list:
        file.write(f'Fold {fold_no} val_binary_accuracy: {acc}\n')

    for fold_no, loss in fold_and_loss_list:
        file.write(f'Fold {fold_no} val_binary_loss: {loss}\n')

    file.write(f"Average val_binary_accuracy across all folds: {average_accuracy}\n")
    file.write(f"Average val_binary_loss across all folds: {average_loss}\n")
print('K_Fold_outcome report')


# Initialize fold numbers
fold_numbers = list(range(1, len(acc_per_fold) + 1))

# Plot the accuracy
plt.figure(figsize=(10, 8))
plt.bar(fold_numbers, acc_per_fold, color='green')
plt.title('Validation Accuracy vs. Fold Number')
plt.xlabel('Fold Number')
plt.ylabel('val_accuracy(%)')
plt.xticks(fold_numbers)
plt.axhline(y=average_accuracy, color='red', linestyle='--', label=f'Average Accuracy(%): {average_accuracy:.2f}')
plt.legend(loc='upper right')
plt.savefig(os.path.join(root_model_folder, 'K_Fold_accuracy.png'), bbox_inches='tight')
plt.tight_layout()
plt.show()
print('Saved K_Fold Accuracy graph')

# Create a bar chart for binary loss
plt.figure(figsize=(10, 8))
plt.bar(fold_numbers, loss_per_fold, color='blue')
plt.title('Validation Loss vs. Fold Number')
plt.xlabel('Fold Number')
plt.ylabel('val_loss')
plt.xticks(fold_numbers)
plt.axhline(y=average_loss, color='red', linestyle='--', label=f'Average Loss: {average_loss:.2f}')
plt.legend(loc='upper right')
plt.savefig(os.path.join(root_model_folder, 'K-Fold_loss.png'), bbox_inches='tight')
plt.tight_layout()
plt.show()
print('Saved K-Fold_loss graph')

print ("Done K-Fold cross validation")
#----------------------------------------------------------------------#
# Calculate the standard deviation of val_binary_accuracy and val_binary_loss
accuracy_std = np.std(acc_per_fold)
loss_std = np.std(loss_per_fold)

# Print the standard deviation
print(f"Standard Deviation of val_binary_accuracy: {accuracy_std:.2f}\n")
print(f"Standard Deviation of val_binary_loss: {loss_std:.2f}\n")

# Plot the accuracy with both average and standard deviation lines
plt.figure(figsize=(10, 8))
plt.bar(fold_numbers, acc_per_fold, color='green', label='Accuracy')
plt.axhline(y=average_accuracy, color='red', linestyle='--', label=f'Average Accuracy(%): {average_accuracy:.2f}')
plt.errorbar(fold_numbers, acc_per_fold, yerr=accuracy_std, linestyle='None', color='black', capsize=5, label='Std Deviation')
plt.title('Validation Accuracy vs. Fold Number')
plt.xlabel('Fold Number')
plt.ylabel('val_accuracy(%)')
plt.xticks(fold_numbers)
plt.legend(loc='upper right')
plt.savefig(os.path.join(root_model_folder, 'K_Fold_accuracy_std.png'), bbox_inches='tight')
plt.tight_layout()
plt.show()
print('Saved K_Fold Accuracy with std graph')

# Plot the loss with both average and standard deviation lines
plt.figure(figsize=(10, 8))
plt.bar(fold_numbers, loss_per_fold, color='blue', label='Loss')
plt.axhline(y=average_loss, color='red', linestyle='--', label=f'Average Loss: {average_loss:.2f}')
plt.errorbar(fold_numbers, loss_per_fold, yerr=loss_std, linestyle='None', color='black', capsize=5, label='Std Deviation')
plt.title('Validation Loss vs. Fold Number')
plt.xlabel('Fold Number')
plt.ylabel('val_loss')
plt.xticks(fold_numbers)
plt.legend(loc='upper right')
plt.savefig(os.path.join(root_model_folder, 'K-Fold_loss_std.png'), bbox_inches='tight')
plt.tight_layout()
plt.show()
print('Saved K-Fold_loss graph')

print("Done K-Fold cross validation with std graph")
#----------------------------------------------------------------------#
# Calculate the standard deviation of val_binary_accuracy and val_binary_loss
accuracy_std = np.std(acc_per_fold)
loss_std = np.std(loss_per_fold)

# Print the standard deviation
print(f"Standard Deviation of val_binary_accuracy: {accuracy_std:.2f}\n")
print(f"Standard Deviation of val_binary_loss: {loss_std:.2f}\n")

with open(file_path, 'a') as file:
    file.write(f"Standard Deviation of val_binary_accuracy: {accuracy_std}\n")
    file.write(f"Standard Deviation of val_binary_loss: {average_loss}\n")

# Plot the accuracy with both average and standard deviation lines
plt.figure(figsize=(10, 8))
plt.bar(fold_numbers, acc_per_fold, color='green', label='Accuracy')
plt.axhline(y=average_accuracy, color='red', linestyle='--', label=f'Average Accuracy(%): {average_accuracy:.2f}')
plt.errorbar(fold_numbers, acc_per_fold, yerr=accuracy_std, linestyle='None', color='black', capsize=5, label='Std Deviation')
plt.title('Validation Accuracy vs. Fold Number')
plt.xlabel('Fold Number')
plt.ylabel('val_accuracy(%)')
plt.xticks(fold_numbers)
plt.legend(loc='upper right')
plt.savefig(os.path.join(root_model_folder, 'K_Fold_accuracy_std.png'), bbox_inches='tight')
plt.tight_layout()
plt.show()
print('Saved K_Fold Accuracy with std graph')

# Plot the loss with both average and standard deviation lines
plt.figure(figsize=(10, 8))
plt.bar(fold_numbers, loss_per_fold, color='blue', label='Loss')
plt.axhline(y=average_loss, color='red', linestyle='--', label=f'Average Loss: {average_loss:.2f}')
plt.errorbar(fold_numbers, loss_per_fold, yerr=loss_std, linestyle='None', color='black', capsize=5, label='Std Deviation')
plt.title('Validation Loss vs. Fold Number')
plt.xlabel('Fold Number')
plt.ylabel('val_loss')
plt.xticks(fold_numbers)
plt.legend(loc='upper right')
plt.savefig(os.path.join(root_model_folder, 'K-Fold_loss_std.png'), bbox_inches='tight')
plt.tight_layout()
plt.show()
print('Saved K-Fold_loss graph')

print("Done K-Fold cross validation with std graph")
#--------------------------------------------xxxxxx-----------------------------------------------------------#

