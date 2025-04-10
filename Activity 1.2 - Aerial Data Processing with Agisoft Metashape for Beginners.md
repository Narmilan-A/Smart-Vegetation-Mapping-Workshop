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

The following are key hyperparameters in **Agisoft Metashape** that influence the processing pipeline. Understanding these parameters will help you optimize the workflow based on the specific requirements of your project (e.g., accuracy, processing time, and resources). 

### 1. **Accuracy (Alignment Stage)**
The **accuracy** setting determines the precision of the camera alignment process. It affects how carefully the software matches key points (distinctive features) between images.

- **Low**: 
  - **Description**: The lowest accuracy setting. Faster but less precise.
  - **When to use**: Ideal for quick tests or when processing large datasets where you don’t need high precision.
  - **Impact**: Faster processing but may lead to misalignment or lower-quality 3D models.
  
- **Medium**:
  - **Description**: Default setting. Provides a balance between speed and accuracy.
  - **When to use**: Suitable for most regular projects where accuracy is important but time constraints exist.
  - **Impact**: A balance between processing time and alignment quality.
  
- **High**:
  - **Description**: This setting improves accuracy by using more time-consuming calculations to align the photos.
  - **When to use**: Recommended for smaller datasets or when precision is a higher priority than speed.
  - **Impact**: Longer processing time, but results in higher accuracy, which is essential for creating detailed models or when GCPs (Ground Control Points) are used.
  
- **Highest**:
  - **Description**: The highest level of accuracy, used for the most detailed and precise camera alignment.
  - **When to use**: When the absolute accuracy of the camera positions is critical (e.g., for topographic surveys or scientific projects).
  - **Impact**: Extremely slow processing time, but it provides the highest possible accuracy.

---

### 2. **Key Point Limit (Alignment Stage)**

Key points are unique, identifiable features within an image, such as corners, edges, or texture patterns. The **key point limit** controls how many of these features Metashape will try to detect and match across images.

- **Low Limit (e.g., 10,000)**:
  - **Description**: Restricts the number of key points detected in each image.
  - **When to use**: Ideal for fast processing or when working with low-resolution or poor-quality images.
  - **Impact**: Fewer points to match means faster processing, but this could lead to lower alignment accuracy.
  
- **High Limit (e.g., 40,000-50,000)**:
  - **Description**: Increases the number of key points detected in each image, improving the chance of finding matching features between images.
  - **When to use**: For projects where the images have high resolution or complex terrain, more key points will improve accuracy.
  - **Impact**: More points mean higher accuracy but slower processing and increased memory usage.
  
- **Very High Limit (e.g., 100,000 or more)**:
  - **Description**: Detects a very large number of key points.
  - **When to use**: For small-scale projects with very high-resolution images or when every detail of the scene is critical.
  - **Impact**: Provides the best alignment results, but processing can take a long time and consume a significant amount of memory.

---

### 3. **Tie Point Limit (Alignment Stage)**

After identifying key points, **tie points** are the matched features across different images. The **tie point limit** controls how many of these matched points Metashape will use during alignment.

- **Low Limit (e.g., 10,000-20,000)**:
  - **Description**: Limits the number of tie points used to align photos.
  - **When to use**: When the alignment process needs to be fast, and you are not focused on ultra-high accuracy.
  - **Impact**: Faster processing, but reduced precision and potential misalignments in complex scenes.
  
- **High Limit (e.g., 50,000-100,000)**:
  - **Description**: Increases the number of tie points used, enhancing the precision of the alignment.
  - **When to use**: For better accuracy in the final model. Suitable for most normal projects.
  - **Impact**: Improved alignment accuracy with a slightly increased processing time.

- **Very High Limit (e.g., 200,000 or more)**:
  - **Description**: Uses a very high number of tie points for the most accurate alignment.
  - **When to use**: For extremely detailed models or scientific applications where precision is paramount.
  - **Impact**: Very slow processing, but results in extremely accurate 3D models.

---

### 4. **Depth Filtering (Dense Cloud Generation)**

**Depth filtering** removes points that don't fit the expected model, such as noisy or erroneous points. It affects the quality of the dense point cloud generated after photos are aligned.

- **Mild**:
  - **Description**: A light filtering process that keeps most of the points while removing minor noise.
  - **When to use**: Ideal for projects where the point cloud needs to retain as many points as possible while filtering out low-level noise.
  - **Impact**: Preserves details in the point cloud but may leave some noise behind.

- **Moderate**:
  - **Description**: Strikes a balance between removing noise and preserving important details.
  - **When to use**: When you need a good quality point cloud without excessive noise but don’t want to lose too many details.
  - **Impact**: A balanced approach that works for most projects.

- **Aggressive**:
  - **Description**: Filters out a significant amount of noise but also reduces the number of points.
  - **When to use**: When working with noisy datasets or when you need a cleaner model and can afford to lose some detail.
  - **Impact**: The point cloud will be much cleaner, but it may miss some fine details.

---

### 5. **Point Confidence (Dense Cloud Generation)**

The **point confidence** setting adjusts how much confidence Metashape has in the points detected during dense cloud generation.

- **Low Confidence**:
  - **Description**: Metashape uses points that it’s less confident in detecting.
  - **When to use**: Suitable for large, open landscapes where point accuracy is less critical.
  - **Impact**: Results in a faster point cloud generation process but may contain some inaccurate points.

- **Medium Confidence**:
  - **Description**: A balanced approach that uses a reasonable level of confidence for points.
  - **When to use**: Ideal for most standard projects.
  - **Impact**: Balanced between accuracy and processing time.

- **High Confidence**:
  - **Description**: Only points with a high level of certainty are used.
  - **When to use**: For projects where accuracy is critical, such as detailed terrain or infrastructure modeling.
  - **Impact**: Slower processing but more accurate results.

---

### 6. **Interpolation Method (DEM Generation)**

The interpolation method determines how the DEM is created from the 3D point cloud.

- **Average**:
  - **Description**: Uses an average of surrounding points to estimate the elevation at each pixel.
  - **When to use**: Ideal for general terrain modeling when detail isn’t paramount.
  - **Impact**: Produces a smooth DEM but may lose some fine details.
  
- **Min**:
  - **Description**: Uses the minimum elevation of surrounding points for each pixel.
  - **When to use**: Best for capturing depressions or lower terrain features such as valleys or ditches.
  - **Impact**: Captures lower terrain features but may overemphasize the lower parts of the landscape.
  
- **Max**:
  - **Description**: Uses the maximum elevation of surrounding points.
  - **When to use**: Useful for applications that focus on capturing the highest features, like mountain peaks.
  - **Impact**: Emphasizes higher terrain features but might lose low-lying areas.

---

### 7. **Resolution (Orthomosaic Generation)**

Resolution defines the level of detail in the final orthomosaic. The higher the resolution, the more detailed the image, but it will also take longer to generate.

- **Low (e.g., 5 cm/pixel)**:
  - **Description**: Low resolution, resulting in a smaller file size and faster processing.
  - **When to use**: Ideal for large areas where fine detail is not necessary.
  - **Impact**: Faster processing but lower image detail.

- **Medium (e.g., 2 cm/pixel)**:
  - **Description**: Balanced resolution, offering a good compromise between quality and processing time.
  - **When to use**: Suitable for most general surveying projects.
  - **Impact**: Produces a high-quality image that is detailed enough for most applications.

- **High (e.g., 0.5 cm/pixel or finer)**:
  - **Description**: High resolution, offering the finest detail.
  - **When to use**: For projects requiring detailed analysis, such as vegetation or infrastructure inspection.
  - **Impact**: Extremely high image quality but significantly longer processing time and larger file sizes.

---

These hyperparameters allow you to fine-tune your project settings to suit your specific needs. By adjusting the settings carefully, you can control the balance between **accuracy**, **processing time**, and **memory usage**, ensuring the best possible results for your drone survey or photogrammetry project.


---

## Additional Resources

For further learning, refer to these helpful resources:

- [Agisoft Metashape Documentation](https://www.agisoft.com/support/documentation/)
- [Metashape User Forum](https://www.agisoft.com/forum/)
- [Agisoft Metashape Tutorials on YouTube](https://www.youtube.com/results?search_query=agisoft+metashape+tutorial)

---

This guide should help you understand the basics of processing aerial images with **Agisoft Metashape**. As you get more comfortable, feel free to experiment with different settings to see how they affect your results.
