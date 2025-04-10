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

---

## Introduction

**Agisoft Metashape** is a photogrammetry software that allows you to process drone images and create 3D models, Digital Elevation Models (DEMs), and orthomosaics. This guide is designed for beginners and explains each step of the processing pipeline, breaking down key concepts and settings to help you achieve accurate results with minimal technical knowledge.

---

## Prerequisites

Before starting, ensure that you have:

- **Agisoft Metashape installed**: Download it from [Agisoft's official website](https://www.agisoft.com/).
- **A set of aerial images**: These should ideally have 60-80% overlap between adjacent images to allow for proper feature matching during the alignment step.
- **Camera position data**: If available, this is helpful in improving the accuracy of the alignment.
- **Ground Control Points (GCPs)**: These are known geographic coordinates that help improve georeferencing accuracy. (This is optional, but highly recommended for precise models).

---

## Processing Steps in Agisoft Metashape

### Step 1: Add Photos

**Purpose**: Import the photos you want to process into the software.

1. Open **Agisoft Metashape**.
2. In the **Workflow** menu on the left, click on **"Add Photos"**.
3. A dialog will appear asking you to select the folder containing the images. Select the folder and click **Open**.
4. Metashape will load all the images into the project.

#### Notes:
- Ensure the photos are from the same drone flight and that they have proper overlap (60-80%).
- The photos should be in supported formats like JPEG, PNG, or TIFF.

---

### Step 2: Align Photos

**Purpose**: Align the photos by detecting common features between them and estimating the position of the cameras.

1. Go to **Workflow** > **Align Photos**.
2. A dialog will appear asking you to set alignment parameters:
   - **Accuracy**: Select one of the following settings:
     - **Low**: Faster but less accurate. Good for small test projects.
     - **Medium**: Balanced between speed and accuracy (default).
     - **High**: Higher accuracy but slower processing.
     - **Highest**: Very high accuracy but the slowest.
   - **Key Point Limit**: This defines the maximum number of key points to be matched between images. Higher values result in better accuracy but require more computing resources.
   - **Tie Point Limit**: This determines the number of tie points (corresponding points between images) used for alignment. More tie points improve alignment accuracy but require more time to process.

3. Click **OK** to begin the alignment process.

#### Explanation:
- **Key points** are distinctive features (like edges or corners) that Metashape uses to identify matching features across different photos.
- **Tie points** are the correspondences between those key points, used to improve the geometric relationship between images.

---

### Step 3: Import Camera Positions

**Purpose**: Import the camera positions if available. This step improves the model's accuracy.

1. Go to **Reference** > **Import** > **Import Cameras**.
2. Select your GPS data file (usually in CSV, KML, or XML format) and load it into Metashape.
3. After importing the camera positions, Metashape will assign those positions to the corresponding images.

#### Notes:
- This step is only useful if you have GPS data for the drone flight. It helps to improve the alignment of the photos.
- GPS data should include the camera's latitude, longitude, altitude, and orientation (yaw, pitch, and roll).

---

### Step 4: Import Ground Control Points (GCPs)

**Purpose**: Import known geographic coordinates (GCPs) to improve the accuracy of the georeferenced model.

1. Go to **Reference** > **Import** > **Import Ground Control Points**.
2. Select the GCP file (usually in CSV format) and load it into Metashape.
3. After importing, Metashape will match the GCPs to the photos. This step involves manually selecting the GCPs in the photos and matching them with the corresponding coordinates from the GCP file.
4. Once matched, Metashape will optimize the alignment using these GCPs.

#### Explanation:
- **Ground Control Points (GCPs)** are specific locations with known coordinates on the earth's surface (often surveyed points) that help improve the accuracy of georeferencing. GCPs are optional but highly recommended when high-accuracy georeferencing is needed.

---

### Step 5: Optimize Camera Alignment

**Purpose**: Refine the camera alignment by adjusting the parameters based on the GCPs and imported camera positions.

1. Go to **Tools** > **Optimize Cameras**.
2. A dialog will appear with several parameters you can optimize:
   - **Focal Length**: This optimizes the camera's focal length, especially if there’s lens distortion.
   - **Lens Distortion**: This corrects any distortions in the images caused by the camera lens.
   - **Marker Coordinates**: This option allows you to optimize the positions of the GCPs.
3. Click **OK** to start the optimization process.

#### Notes:
- Optimizing the alignment ensures that the model is as accurate as possible by adjusting the camera positions and GCPs according to the observed data.

---

### Step 6: Build Dense Cloud

**Purpose**: Create a dense point cloud that represents the 3D geometry of the scene.

1. Go to **Workflow** > **Build Dense Cloud**.
2. Set the following parameters:
   - **Quality**: Choose between **Low**, **Medium**, **High**, or **Ultra High**. Higher quality produces a denser point cloud with more details but takes more time.
   - **Depth Filtering**: Choose the depth filtering method:
     - **Mild**: Removes minimal noise.
     - **Moderate**: Balances between noise removal and data retention.
     - **Aggressive**: Removes more noise but might also discard useful points.
   - **Point Confidence**: This determines how much confidence Metashape has in the detected points. A higher setting means more accurate points but requires more processing power.

3. Click **OK** to begin building the dense cloud.

#### Notes:
- The dense cloud is a collection of 3D points that represent the object or scene. The quality and resolution of this cloud depend on the **Dense Cloud Quality** setting you choose.
- **Higher quality** will result in a more detailed model, but the processing time increases.

---

### Step 7: Build DEM (Digital Elevation Model)

**Purpose**: Create a Digital Elevation Model (DEM), which represents the terrain surface of the study area.

1. Go to **Workflow** > **Build DEM**.
2. Set the following parameters:
   - **Source Data**: Choose **Dense Cloud** as the source for building the DEM.
   - **Interpolation**: Select **Average** (smoothes the surface) or **Min** (captures depressions better).
   - **Resolution**: Define the resolution (e.g., 0.1 m for high resolution, 1 m for large areas).
3. Click **OK** to generate the DEM.

#### Notes:
- The **DEM** represents the ground surface and helps you visualize terrain features like hills, valleys, and flat areas. It can also be used for analysis like slope, aspect, and elevation changes.

---

### Step 8: Build Orthomosaic

**Purpose**: Generate a georeferenced orthophoto, which is a geometrically corrected image of the study area.

1. Go to **Workflow** > **Build Orthomosaic**.
2. Set the following parameters:
   - **Projection**: Choose the coordinate system for the orthomosaic (e.g., UTM).
   - **Surface**: Choose between **Height Field** (use the DEM) or **Orthophoto**.
   - **Resolution**: Set the resolution (e.g., 0.1 m for high detail).
3. Click **OK** to generate the orthomosaic.

#### Notes:
- The **orthomosaic** is a true-to-scale map of the area, created by stitching together the photos while correcting distortions. It is ideal for visual analysis or mapping purposes.

---

## Exporting Results

### Step 9: Export DEM

To export the DEM:

1. Right-click on the DEM in the **"Chunks"** pane.
2. Select **Export** > **Export DEM**.
3. Choose the file format (e.g., GeoTIFF) and specify the location where you want to save the DEM.
4. Click **OK** to export the DEM.

---

### Step 10: Export Orthomosaic

To export the orthomosaic:

1. Right-click on the orthomosaic in the **"Chunks"** pane.
2. Select **Export** > **Export Orthomosaic**.
3. Choose the format (GeoTIFF, JPEG) and set the output location.
4. Click **OK** to export the orthomosaic.

---

## Hyperparameters and Their Explanation

### **Accuracy**
- **Low**: Faster processing, but the result may be less accurate.
- **Medium**: Balanced between speed and quality (default).
- **High**: Slow, but offers very accurate results.
- **Highest**: Takes a lot of time and computing power but provides the best accuracy.

### **Key Point Limit**
- The number of key points Metashape uses to match features between photos. Increasing this number improves accuracy but requires more processing time and memory.

### **Depth Filtering**
- **Mild**: Keeps most points but filters out minor noise.
- **Moderate**: Strikes a balance between retaining detail and filtering noise.
- **Aggressive**: Filters out a lot of noise but may discard some details.

### **Point Confidence**
- This parameter defines how confident the software is about the points it detects. Higher confidence means better quality but may increase processing time.

---

## Additional Resources

For further learning, refer to these helpful resources:

- [Agisoft Metashape Documentation](https://www.agisoft.com/support/documentation/)
- [Metashape User Forum](https://www.agisoft.com/forum/)
- [Agisoft Metashape Tutorials on YouTube](https://www.youtube.com/results?search_query=agisoft+metashape+tutorial)

---

This guide should help you understand the basics of processing aerial images with **Agisoft Metashape**. As you get more comfortable, feel free to experiment with different settings to see how they affect your results.
