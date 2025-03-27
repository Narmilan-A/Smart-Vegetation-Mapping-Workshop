# Import general python libraries
import numpy as np
import matplotlib.pyplot as plt
import joblib
from skimage import exposure
import seaborn as sns
import os
import cv2
from scipy.ndimage import convolve

# Import the GDAL module from the osgeo package
from osgeo import gdal
#----------------------------------------------------------------------#
# Define function to calculate vegetation indices
def calculate_veg_indices(input_img):
# Extract the all channels from the input image
    RedEdge = input_img[:, :, 3]
    nir = input_img[:, :, 4]
    red = input_img[:, :, 2]
    green = input_img[:, :, 1]
    blue = input_img[:, :, 0]

    # Calculate vegetation indices
    ndvi = (nir - red) / (nir + red)
    gndvi = (nir - green) / (nir + green)
    ndre = (nir - RedEdge) / (nir + RedEdge)
    gci = (nir)/(green) - 1
    msavi = ((2 * nir) + 1 -(np.sqrt(np.power((2 * nir + 1), 2) - 8*(nir - red))))/2
    exg = ((2*green)-red-blue)/(red+green+blue)
    sri = (nir / red)
    arvi = (nir - (2*red - blue)) / (nir + (2*red - blue))
    lci = (nir - RedEdge) / (nir + red)
    hrfi = (red - blue) / (green + blue)
    dvi = (nir - red)
    rvi = (nir)/(red)
    tvi = (60*(nir - green)) - (100 * (red - green))
    gdvi = (nir - green)
    ngrdi = (green - red) / (green + red)
    grvi = (red - green) / (red + green)
    rgi = (red / green)
    endvi = ((nir + green) - (2 * blue)) / ((nir + green) + (2 * blue))
    evi=(2.5 * (nir - red)) / (nir + (6 * red) - (7.5 * blue) + 1)
    sipi= (nir - blue) / (nir - red)
    osavi= (1.16 * (nir - red)) / (nir + red + 0.16)
    gosavi=(nir - green) / (nir + green + 0.16)
    exr= ((1.4 * red) - green) / (red + green + blue)
    exgr= (((2 * green) - red - blue) / (red + green + blue)) - (((1.4 * red) - green) / (red + green + blue))
    ndi=(green - red) / (green + red)
    gcc= green / (red + green + blue)
    reci= (nir) / (RedEdge) - 1
    ndwi= (green - nir) / (green + nir)

    #veg_indices = np.stack((ndvi,ndre,hrfi,gndvi,gci,msavi,exg,sri,arvi,lci, dvi, rvi, tvi, gdvi, ngrdi, grvi, rgi, endvi, evi,sipi,osavi,gosavi,exr,exgr,ndi,gcc,reci,ndwi), axis=2)
    veg_indices = np.stack((dvi,gdvi,msavi,tvi,gosavi), axis=2)
    #veg_indices = np.stack((dvi,gdvi,msavi), axis=2)

    return veg_indices
#----------------------------------------------------------------------#
# Define a 7x7 low-pass averaging kernel
kernel_size = 7
kernel = np.ones((kernel_size, kernel_size)) / (kernel_size**2)

# Define a function to apply Gaussian blur to an image
def apply_gaussian_blur(img):
    return cv2.GaussianBlur(img, (7,7), 0)

# Function to apply mean filter in a 3x3 window
def apply_mean_filter(img):
    return cv2.blur(img, (5,5))
#----------------------------------------------------------------------#
root_data_folder = r'F:/scc_final_submission'
root_image_folder = r'E:/SCC_Project/scc_final_submission/pandanus_classification/msi_image_mask_rois/testing'
root_model_folder =os.path.join(root_image_folder, 'xgb_spectral_model&outcomes_2bands_5_VIs')
#----------------------------------------------------------------------#
# Load the saved model
model_file_path = os.path.join(root_model_folder, 'best_xgb_model.pkl')
best_xgb_model = joblib.load(model_file_path)
#------------------------------------------------------------------#
# Display and export the prediction results
print('Exporting the prediction results... ', end="", flush=True)

# Store the images and masks
input_imgs = []


input_img_folder = os.path.join(root_image_folder, 'msi_rois')

# Retrieve all image and mask files
img_files = [file for file in os.listdir(input_img_folder) if file.endswith(".tif")]

# Sort the files to ensure consistent ordering
img_files.sort()

# Loop over the files and extract all the images and masks
for i in range(len(img_files)):
    img_file = os.path.join(input_img_folder, img_files[i])
    ds_img = gdal.Open(img_file)
    input_img = np.array([ds_img.GetRasterBand(j + 1).ReadAsArray() for j in range(5)])

    input_img = np.transpose(input_img, (1, 2, 0))

    input_img = exposure.equalize_hist(input_img)

    veg_indices = calculate_veg_indices(input_img)
    input_img = np.concatenate((input_img, veg_indices), axis=2)

    input_img = np.delete(input_img, [0,1,2], axis=2)

    # for c in range(input_img.shape[2]):
    #     input_img[:, :, c] = convolve(input_img[:, :, c], kernel)
    # input_img = apply_gaussian_blur(input_img)

    input_img = apply_mean_filter(input_img)

    input_imgs.append(input_img)

    input_prediction_2d_RF = None
  
    # Predict using the classifier models
    input_img_hist_array = input_img[np.newaxis, ...]
    input_img_hist_array_2d = input_img_hist_array.reshape(-1, input_img_hist_array.shape[-1])

    if 'best_xgb_model' in locals():
        input_prediction_RF = best_xgb_model.predict(input_img_hist_array_2d)
        input_prediction_2d_RF = input_prediction_RF.reshape(input_img_hist_array.shape[1],input_img_hist_array.shape[2])
        # Get the input image file name without extension
        img_file_name = os.path.splitext(img_files[i])[0]

        prediction_folder = os.path.join(root_model_folder, 'prediction')
        if not os.path.exists(prediction_folder):
            os.makedirs(prediction_folder)     
        pred_image_file_RF = os.path.join(prediction_folder, f'xgb_predicted_{img_file_name}.dat')
        driver = gdal.GetDriverByName('ENVI')
        pred_image_ds_RF = driver.Create(pred_image_file_RF, input_prediction_2d_RF.shape[1], input_prediction_2d_RF.shape[0], 1, gdal.GDT_Float32)
        pred_image_ds_RF.GetRasterBand(1).WriteArray(input_prediction_2d_RF)
        pred_image_ds_RF.SetGeoTransform(ds_img.GetGeoTransform())
        pred_image_ds_RF.SetProjection(ds_img.GetProjection())
        pred_image_ds_RF = None

print("Completed")
#-------------------------------------****************************-----------------------------------------------#
#-------------------------------------****************************-----------------------------------------------#
#-------------------------------------****************************-----------------------------------------------#