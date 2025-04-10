# Aerial Data Processing with Agisoft Metashape for Beginners

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Processing Steps in Agisoft Metashape](#processing-steps-in-agisoft-metashape)
   - [Step 1: Add Photos](#step-1-add-photos)
   - [Step 2: Align Photos](#step-2-align-photos)
   - [Step 3: Import Camera Positions](#step-3-import-camera-positions)
   - [Step 4: Import Ground Control Points (GCPs)](#step-4-import-ground-control-points-gcps)
   - [Step 5: Optimize Camera Alignment](#step-5-optimize-camera-alignment)
   - [Step 6: Build Dense Cloud](#step-6-build-dense-cloud)
   - [Step 7: Build DEM (Digital Elevation Model)](#step-7-build-dem)
   - [Step 8: Build Orthomosaic](#step-8-build-orthomosaic)
4. [Exporting Results](#exporting-results)
   - [Step 9: Export DEM](#step-9-export-dem)
   - [Step 10: Export Orthomosaic](#step-10-export-orthomosaic)
5. [Hyperparameters and Their Explanation](#hyperparameters-and-their-explanation)
6. [Additional Resources](#additional-resources)

## Introduction

**Agisoft Metashape** is a photogrammetry software that processes aerial images from drones and converts them into valuable 3D models, Digital Elevation Models (DEMs), and orthomosaics. This guide provides a step-by-step explanation of how to process your aerial images using Metashape, suitable for beginners with detailed instructions and hyperparameters' explanations.

## Prerequisites

Before starting, make sure you have:

- **Agisoft Metashape** installed on your computer. Download it from [Agisoft's website](https://www.agisoft.com/).
- A set of **aerial photos** taken by a drone (ensure they have sufficient overlap).
- **Ground Control Points (GCPs)** (optional but highly recommended for accuracy).
- **Camera positions** (if available, optional but beneficial).
- A computer capable of handling large datasets (especially for high-resolution imagery).

## Processing Steps in Agisoft Metashape

### Step 1: Add Photos

This step involves importing the photos you want to process into Agisoft Metashape.

1. Open **Agisoft Metashape**.
2. In the **Workflow** pane (on the left), click on **"Add Photos"**.
3. A file dialog will open. Select the folder containing the images from your drone flight.
4. After selecting the folder, Metashape will automatically load all the photos into the project. These images should have overlap with each other for proper alignment.

#### Notes:
- Photos should have at least 60-80% overlap between adjacent photos for good results.
- The images must be in a supported format (JPEG, PNG, TIFF).

### Step 2: Align Photos

In this step, Metashape aligns the photos by finding matching features between them and estimating the position of the cameras.

1. Go to the **Workflow** menu at the top of the window and select **"Align Photos"**.
2. A dialog will appear asking you to set alignment parameters.
   - **Accuracy**: Choose the level of alignment accuracy.
     - **Low**: Faster, used for preliminary processing or small projects.
     - **Medium**: Balanced between accuracy and speed (default).
     - **High**: Higher accuracy but more time-consuming.
     - **Highest**: Best quality, most accurate, but takes the longest time.
   - **Key Point Limit**: This parameter defines the maximum number of points to be used for image matching. A higher value results in better alignment but requires more computing power.
   - **Tie Point Limit**: This controls the number of tie points used to find correspondences between photos. A higher value results in better accuracy but increases the time to process.

3. After setting the parameters, click **OK** to start the alignment process.
4. Metashape will generate a sparse point cloud, showing the alignment of the camera positions and images.

#### Notes:
- The alignment process uses algorithms to detect common features (e.g., corners, edges) between overlapping images.
- If there are issues (e.g., poor alignment), try increasing the **Key Point Limit** or **Accuracy** setting.

### Step 3: Import Camera Positions

If you have GPS data (camera positions), importing it will help refine the accuracy of your model. This step is optional but beneficial.

1. Go to **Reference** > **Import** > **Import Cameras...**.
2. Select your GPS data file (typically CSV, KML, or XML format) and load it into Metashape.
3. The software will assign the imported camera positions to the images and improve the alignment.

#### Notes:
- GPS data should include the latitude, longitude, altitude, and orientation of the camera for each image.

### Step 4: Import Ground Control Points (GCPs)

Ground Control Points (GCPs) are known coordinates (e.g., surveyed locations) that help georeference the 3D model, improving its accuracy.

1. Go to **Reference** > **Import** > **Import Ground Control Points...**.
2. Select your GCP file (usually in CSV format).
3. For each GCP, Metashape will ask you to match the point locations in the images. Click on the photo, and mark the point where it appears in the image.
4. After importing and matching the GCPs, Metashape will optimize the alignment based on this information.

#### Notes:
- Ensure that your GCPs are in the same coordinate system as your project. Metashape supports many coordinate systems, including UTM and geographic coordinates.

### Step 5: Optimize Camera Alignment

After importing the GCPs and camera positions, optimize the alignment to ensure maximum accuracy.

1. Go to **Tools** > **Optimize Cameras**.
2. In the dialog box, select the parameters you want to optimize:
   - **Focal Length**: Adjusts the camera’s focal length based on the data.
   - **Lens Distortion**: Corrects any distortion caused by the lens.
   - **Marker Coordinates**: Fine-tunes the positions of the GCPs.
3. Click **OK** to run the optimization.

#### Notes:
- Optimizing camera alignment ensures that the camera positions and GCPs are correctly adjusted for the best possible alignment of the images.

### Step 6: Build Dense Cloud

Once the photos are aligned, you can generate a **dense point cloud** that represents the 3D geometry of the scene.

1. Go to **Workflow** > **Build Dense Cloud**.
2. In the dialog box, set the following parameters:
   - **Quality**: Choose between Low, Medium, High, and Ultra High.
     - **Low**: Faster but lower-quality point cloud.
     - **Medium**: Balanced quality and processing time.
     - **High**: Higher-quality point cloud but slower.
     - **Ultra High**: Best quality, but takes the longest.
   - **Depth Filtering**: Choose between **Mild**, **Moderate**, and **Aggressive**. This helps to filter noise from the point cloud.
   - **Point Confidence**: Select **Normal** or **High** to define how confident the software should be about the points.

3. Click **OK** to build the dense cloud.

#### Notes:
- Higher quality settings result in more detailed point clouds, but they take longer to process and require more memory.

### Step 7: Build DEM (Digital Elevation Model)

Now that you have a dense point cloud, you can generate a **Digital Elevation Model (DEM)**, which represents the topography of the area.

1. Go to **Workflow** > **Build DEM**.
2. In the dialog box, choose:
   - **Source Data**: Select **Dense Cloud** (this is usually the best choice for DEM generation).
   - **Interpolation**: Choose **Average** or **Min**. Average will smooth the surface, while Min can help to capture lower features like depressions.
   - **Resolution**: Define the spatial resolution (e.g., 0.1 m for high detail, 1 m for large areas).

3. Click **OK** to generate the DEM.

#### Notes:
- A higher resolution will result in a more detailed DEM, but it also requires more memory and takes longer to process.

### Step 8: Build Orthomosaic

After creating the DEM, you can generate an **orthomosaic** which is a geometrically corrected image of your study area.

1. Go to **Workflow** > **Build Orthomosaic**.
2. In the dialog box, choose:
   - **Projection**: Select the coordinate system for the orthomosaic (e.g., UTM).
   - **Surface**: Choose between **Height Field** (using DEM) or **Orthophoto**.
   - **Resolution**: Choose the resolution for the output (e.g., 0.1 m for detailed imagery).
3. Click **OK** to generate the orthomosaic.

#### Notes:
- Higher resolution results in better detail but requires more processing time.

## Exporting Results

Once you've created the DEM and orthomosaic, you can export them for further analysis or use.

### Step 9: Export DEM

To export the DEM:
1. Right-click on the DEM in the "Chunks" pane.
2. Select **Export** > **Export DEM**.
3. Choose the format (e.g., GeoTIFF) and set the output location.
4. Click **OK** to export.

### Step 10: Export Orthomosaic

To export the orthomosaic:
1. Right-click on the orthomosaic in the "Chunks" pane.
2. Select **Export** > **Export Orthomosaic**.
3. Choose the desired format (e.g., GeoTIFF, JPEG) and set the output location.
4. Click **OK** to export.

## Hyperparameters and Their Explanation

### **Accuracy**
- **Low**: Faster but less accurate, suitable for small or test projects.
- **Medium**: Balanced accuracy and processing time.
- **High**: Slower but more accurate.
- **Highest**: Maximum accuracy, but the slowest and requires more computing resources.

### **Key Point Limit**
The number of key points Metashape uses to match features between images. A higher value means better feature matching but requires more processing power.

### **Tie Point Limit**
The number of tie points Metashape uses to match overlapping features between images. Increasing this number improves alignment but slows down the process.

### **Depth Filtering**
Controls how aggressively Metashape filters out noise from the point cloud. **Aggressive** filtering is useful in noisy datasets, but it may discard valuable data points.

### **Point Confidence**
A measure of how confident Metashape is in placing a point in the correct location. Higher confidence leads to better results but takes more time to process.

## Additional Resources

For further learning, here are some useful links:
- [Agisoft Metashape Documentation](https://www.agisoft.com/support/documentation/)
- [Metashape User Forum](https://www.agisoft.com/forum/)
- [Agisoft Metashape Tutorials on YouTube](https://www.youtube.com/results?search_query=agisoft+metashape+tutorial)

---

This guide covers all the basic steps required to start processing your drone data in **Agisoft Metashape**. Be sure to experiment with different settings to see how they impact your results.
