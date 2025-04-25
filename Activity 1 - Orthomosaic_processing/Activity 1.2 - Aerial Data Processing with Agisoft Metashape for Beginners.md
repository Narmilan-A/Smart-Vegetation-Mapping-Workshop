# Aerial Data Processing with Agisoft Metashape for Beginners

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Processing Steps in Agisoft Metashape](#processing-steps-in-agisoft-metashape)
   - [Step 1: Add Photos](#step-1-add-photos)
   - [Step 2: Reflectance Panel Calibration (for Multispectral Data)](#step-2-reflectance-panel-calibration-for-multispectral-data)
   - [Step 3: Align Photos](#step-3-align-photos)
   - [Step 4: Import Camera Positions](#step-4-import-camera-positions)
   - [Step 5: Import Ground Control Points (GCPs)](#step-5-import-ground-control-points-gcps)
   - [Step 6: Optimize Camera Alignment](#step-6-optimize-camera-alignment)
   - [Step 7: Build Dense Cloud](#step-7-build-dense-cloud)
   - [Step 8: Build DEM (Digital Elevation Model)](#step-8-build-dem-digital-elevation-model)
   - [Step 9: Build Orthomosaic](#step-9-build-orthomosaic)
4. [Exporting Results](#exporting-results)
   - [Step 10: Export DEM](#step-10-export-dem)
   - [Step 11: Export Orthomosaic](#step-11-export-orthomosaic)
5. [Hyperparameters and Their Explanation](#hyperparameters-and-their-explanation)
6. [Additional Resources](#additional-resources)


---

## Introduction

**Agisoft Metashape** is a photogrammetry software that allows you to process drone images and create 3D models, Digital Elevation Models (DEMs), and orthomosaics. This guide is designed for beginners and explains each step of the processing pipeline, breaking down key concepts and settings to help you achieve accurate results with minimal technical knowledge.

---

## Prerequisites

Before starting, ensure that you have:

- **Agisoft Metashape installed**: Download it from [Agisoft's official website](https://www.agisoft.com/).
- **A set of aerial images and camera position data**: These should ideally have 50-80% overlap between adjacent images to allow for proper feature matching during the alignment step.
- **Reflectance panel images and metadata** (for multispectral processing): Ensure you captured calibration panel images during the field campaign and have access to their known reflectance values or calibration certificates.
- **Ground Control Points (GCPs)**: These are known geographic coordinates that help improve georeferencing accuracy. (This is optional, but highly recommended for precise models).

---

## Processing Steps in Agisoft Metashape

### Step 1: Add Photos

**Purpose**: Import the photos you want to process into the software.

1. Open **Agisoft Metashape**.
2. In the **Workflow** menu on the left, click on **"Add Photos"** / **"Add Folder"**.
3. A dialog will appear asking you to select the folder containing the images. Select the photos/folder and click **Open**.
4. Metashape will load all the images into the project.

#### Notes:
- Ensure the photos are from the same drone flight and that they have proper overlap (50-80%).
- The photos should be in supported formats like JPEG, PNG, or TIFF.

---

### Step 2: Reflectance Panel Calibration (for Multispectral Data)

**Purpose**: To correct for lighting conditions and sensor variability, ensuring accurate reflectance values using reference panels and sun sensor data.

1. Go to **Tools** > **Calibrate Reflectance**.
2. Click **Locate Panels**.
   - Metashape will detect images containing reflectance panels.
   - These images will be moved to a separate folder, and masks will be created to isolate the panel area.
   - If panels are not detected automatically, follow the manual steps in [Activity 1.3](https://github.com/Narmilan-A/Smart-Vegetation-Mapping-Workshop/blob/d1d25aa5c6a86a017e2c22bd57c1e06c17da4d5c/Activity%201%20-%20Orthomosaic_processing/Activity%201.3%20-%20Manual%20Masking%20of%20Calibration%20Images%20with%20the%20Radiometric%20Panel.md).
3. If this is the first time using this panel, you may be prompted to load a **calibration CSV file**.
   - If not available, you can enter calibration values manually.
   - For MicaSense panels, CSV files can be requested from the manufacturer.
4. Input the reflectance values (albedo) for each band based on the panel’s certificate.
   - Use the **Select Panel...** button to load values or enter them manually in the dialog.
   - For thermal bands (LWIR), this step is not required—leave the field empty.
5. In the **Calibrate Reflectance** dialog:
   - Tick **Use reflectance panels**.
   - Tick **Use sun sensor** (Based on exteranl factors like sun light variation).
6. Click **OK** to apply reflectance calibration.

**Notes**:
- If calibration is rerun, the previous settings will be overwritten.
- This step is **crucial for multispectral imagery** where vegetation indices like NDVI or NDRE will be calculated.
- Make sure the panel is clean and fully visible in the photo with no shadows.
- [Tutorial from Agisoft:MicaSense Altum processing workflow including Reflectance Calibration](https://agisoft.freshdesk.com/support/solutions/articles/31000148381)
---

### Step 3: Align Photos

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

### Step 4: Import Camera Positions

**Purpose**: Import the camera positions if available. This step improves the model's accuracy.

1. Go to **Reference** > **Import** > **Import Cameras**.
2. Select your GPS data file (usually in CSV, KML, or XML format) and load it into Metashape.
3. After importing the camera positions, Metashape will assign those positions to the corresponding images.

#### Notes:
- This step is only useful if you have GPS data for the drone flight. It helps to improve the alignment of the photos.
- GPS data should include the camera's latitude, longitude, altitude, and orientation (yaw, pitch, and roll).

---

### Step 5: Import Ground Control Points (GCPs)

Markers can be specified in one of the following ways:
- Imported from a separate text file (using character-separated values format).
- Entered manually in the **Reference** pane.

#### 1. Import from File

1. Click the **Import** toolbar button in the **Reference** pane. (To open the **Reference** pane, use the **Reference** command from the **View** menu.)
2. Browse to the file with Ground Control Points (GCPs) and coordinates, then click the **Open** button.
3. In the **Import CSV** dialog, set the coordinate system if the data contains geographical coordinates.
4. Select the delimiter and specify the column number for each coordinate (e.g., latitude, longitude, and altitude).
5. Click **OK** to import the markers.

#### 2. Manual Entry

- You can also add markers manually in the **Reference** pane by entering the coordinates directly.

#### 3. Filter by Markers

- To filter photos by markers, use the **Filter by Markers** command from the 3D view context menu.

#### 4. Marker Editing

1. Switch to the marker editing mode using the **Edit Markers** toolbar button.
2. To adjust the marker projection, drag it to the desired location using the left mouse button.

#### 5. Types of Markers

- **Control Points**: These are used to reference the model. They are critical for aligning and georeferencing the model to real-world coordinates.
- **Check Points**: These are used to validate the accuracy of the camera alignment and optimization procedures.

#### Notes:
- [Tutorial from Agisoft: Aerial data processing with GCPs](https://agisoft.freshdesk.com/support/solutions/articles/31000153696)
---

### Step 6: Optimize Camera Alignment

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

### Step 7: Build Point Cloud

**Purpose**: Create a dense point cloud that represents the 3D geometry of the scene.

1. Go to **Workflow** > **Build Point Cloud**.
2. Set the following parameters:
   - **Quality**: Choose between **Low**, **Medium**, **High**, or **Ultra High**. Higher quality produces a denser point cloud with more details but takes more time.
   - **Depth Filtering**: Choose the depth filtering method:
     - **Mild**: Removes minimal noise.
     - **Moderate**: Balances between noise removal and data retention.
     - **Aggressive**: Removes more noise but might also discard useful points.

3. Click **OK** to begin building the dense cloud.

---

### Step 8: Build DEM (Digital Elevation Model)

**Purpose**: Create a Digital Elevation Model (DEM), which represents the terrain surface of the study area.

1. Go to **Workflow** > **Build DEM**.
2. Set the following parameters:
   - **Source Data**: Choose **Point Cloud** as the source for building the DEM.
3. Click **OK** to generate the DEM.

#### Notes:
- The **DEM** represents the ground surface and helps you visualise terrain features like hills, valleys, and flat areas. It can also be used for analysis like slope, aspect, and elevation changes.

---

### Step 9: Build Orthomosaic

**Purpose**: Generate a georeferenced orthophoto, which is a geometrically corrected image of the study area.

1. Go to **Workflow** > **Build Orthomosaic**.
2. Set the following parameters:
   - **Projection**: Choose the coordinate system for the orthomosaic (e.g., UTM).
   - **Surface**: Choose between **Height Field** (use the DEM) or **Orthophoto**.
3. Click **OK** to generate the orthomosaic.

#### Notes:
- The **orthomosaic** is a true-to-scale map of the area, created by stitching together the photos while correcting distortions. It is ideal for visual analysis or mapping purposes.

---

## Exporting Results

### Step 10: Export DEM

To export the DEM:

1. Right-click on the DEM in the **"Chunks"** pane.
2. Select **Export** > **Export DEM**.
3. Choose the file format (e.g., GeoTIFF) and specify the location where you want to save the DEM.
4. Click **OK** to export the DEM.

---

### Step 11: Export Orthomosaic

To export the orthomosaic:

1. Right-click on the orthomosaic in the **"Chunks"** pane.
2. Select **Export** > **Export Orthomosaic**.
3. Choose the format (GeoTIFF, JPEG) and set the output location.
4. Click **OK** to export the orthomosaic.

---

## Hyperparameters and Their Explanation

The following are key hyperparameters in **Agisoft Metashape** that influence the processing pipeline. Understanding these parameters will help you optimize the workflow based on the specific requirements of your project (e.g., accuracy, processing time, and resources). 

---

### 1. **Accuracy (Alignment Stage)**

The **accuracy** setting determines the precision of the camera alignment process. It affects how carefully the software matches key points (distinctive features) between images.

- **Low**: 
  - **Description**: The lowest accuracy setting. Faster but less precise.
  - **When to use**: Ideal for quick tests or when processing large datasets where you don’t need high precision.
  - **Impact**: Faster processing but may lead to misalignment or lower-quality 3D models.
  - **Real-world Example**: A drone mapping a large agricultural field where you just need to see the general layout, but high precision is not necessary.

- **Medium**:
  - **Description**: Default setting. Provides a balance between speed and accuracy.
  - **When to use**: Suitable for most regular projects where accuracy is important but time constraints exist.
  - **Impact**: A balance between processing time and alignment quality.
  - **Real-world Example**: A city survey for infrastructure analysis where you want decent precision but need to work within time limits.

- **High**:
  - **Description**: This setting improves accuracy by using more time-consuming calculations to align the photos.
  - **When to use**: Recommended for smaller datasets or when precision is a higher priority than speed.
  - **Impact**: Longer processing time, but results in higher accuracy, which is essential for creating detailed models or when GCPs (Ground Control Points) are used.
  - **Real-world Example**: A topographic survey for creating accurate elevation models of a mountain or hill.

- **Highest**:
  - **Description**: The highest level of accuracy, used for the most detailed and precise camera alignment.
  - **When to use**: When the absolute accuracy of the camera positions is critical (e.g., for topographic surveys or scientific projects).
  - **Impact**: Extremely slow processing time, but it provides the highest possible accuracy.
  - **Real-world Example**: A legal survey where land boundaries need to be mapped with the utmost precision for property disputes.

---

### 2. **Key Point Limit (Alignment Stage)**

Key points are unique, identifiable features within an image, such as corners, edges, or texture patterns. The **key point limit** controls how many of these features Metashape will try to detect and match across images.

- **Low Limit (e.g., 10,000)**:
  - **Description**: Restricts the number of key points detected in each image.
  - **When to use**: Ideal for fast processing or when working with low-resolution or poor-quality images.
  - **Impact**: Fewer points to match means faster processing, but this could lead to lower alignment accuracy.
  - **Real-world Example**: An initial test flight where you’re experimenting with the settings to get a rough model without the need for high detail.

- **High Limit (e.g., 40,000-50,000)**:
  - **Description**: Increases the number of key points detected in each image, improving the chance of finding matching features between images.
  - **When to use**: For projects where the images have high resolution or complex terrain, more key points will improve accuracy.
  - **Impact**: More points mean higher accuracy but slower processing and increased memory usage.
  - **Real-world Example**: Mapping a large complex urban area with dense buildings, where fine details and accuracy are important.

- **Very High Limit (e.g., 100,000 or more)**:
  - **Description**: Detects a very large number of key points.
  - **When to use**: For small-scale projects with very high-resolution images or when every detail of the scene is critical.
  - **Impact**: Provides the best alignment results, but processing can take a long time and consume a significant amount of memory.
  - **Real-world Example**: A drone survey of a historical building, where every detail of the structure needs to be captured and aligned accurately.

---

### 3. **Tie Point Limit (Alignment Stage)**

After identifying key points, **tie points** are the matched features across different images. The **tie point limit** controls how many of these matched points Metashape will use during alignment.

- **Low Limit (e.g., 10,000-20,000)**:
  - **Description**: Limits the number of tie points used to align photos.
  - **When to use**: When the alignment process needs to be fast, and you are not focused on ultra-high accuracy.
  - **Impact**: Faster processing, but reduced precision and potential misalignments in complex scenes.
  - **Real-world Example**: A quick scan of a large open field where accuracy isn't the top priority, and speed is important.

- **High Limit (e.g., 50,000-100,000)**:
  - **Description**: Increases the number of tie points used, enhancing the precision of the alignment.
  - **When to use**: For better accuracy in the final model. Suitable for most normal projects.
  - **Impact**: Improved alignment accuracy with a slightly increased processing time.
  - **Real-world Example**: Mapping a park with trees and paths, where good accuracy is needed but the project is still relatively simple.

- **Very High Limit (e.g., 200,000 or more)**:
  - **Description**: Uses a very high number of tie points for the most accurate alignment.
  - **When to use**: For extremely detailed models or scientific applications where precision is paramount.
  - **Impact**: Very slow processing, but results in extremely accurate 3D models.
  - **Real-world Example**: A botanical survey of a complex forest where you need to capture every detail of the environment for research purposes.

---

### 4. **Depth Filtering (Dense Cloud Generation)**

**Depth filtering** removes points that don't fit the expected model, such as noisy or erroneous points. It affects the quality of the dense point cloud generated after photos are aligned.

- **Mild**:
  - **Description**: A light filtering process that keeps most of the points while removing minor noise.
  - **When to use**: Ideal for projects where the point cloud needs to retain as many points as possible while filtering out low-level noise.
  - **Impact**: Preserves details in the point cloud but may leave some noise behind.
  - **Real-world Example**: Mapping a large area of farmland where you want to preserve the maximum amount of information despite minor noise from vegetation or clouds.

- **Moderate**:
  - **Description**: Strikes a balance between removing noise and preserving important details.
  - **When to use**: When you need a good quality point cloud without excessive noise but don’t want to lose too many details.
  - **Impact**: A balanced approach that works for most projects.
  - **Real-world Example**: Mapping an urban area where some minor noise is acceptable, but you still want to capture the key features of the landscape.

- **Aggressive**:
  - **Description**: Filters out a significant amount of noise but also reduces the number of points.
  - **When to use**: When working with noisy datasets or when you need a cleaner model and can afford to lose some detail.
  - **Impact**: The point cloud will be much cleaner, but it may miss some fine details.
  - **Real-world Example**: A survey of a building after a storm where debris and noise need to be removed, and you are focused more on the structure than the finer landscape details.

---

### 5. **Point Confidence (Dense Cloud Generation)**

The **point confidence** setting adjusts how much confidence Metashape has in the points detected during dense cloud generation.

- **Low Confidence**:
  - **Description**: Metashape uses points that it’s less confident in detecting.
  - **When to use**: Suitable for large, open landscapes where point accuracy is less critical.
  - **Impact**: Results in a faster point cloud generation process but may contain some inaccurate points.
  - **Real-world Example**: Mapping a large rural area where detail accuracy is not as critical.

- **Medium Confidence**:
  - **Description**: A balanced approach that uses a reasonable level of confidence for points.
  - **When to use**: Ideal for most standard projects.
  - **Impact**: Balanced between accuracy and processing time.
  - **Real-world Example**: A park survey where moderate accuracy is required but time constraints exist.

- **High Confidence**:
  - **Description**: Only points with a high level of certainty are used.
  - **When to use**: For projects where accuracy is critical, such as detailed terrain or infrastructure modeling.
  - **Impact**: Slower processing but more accurate results.
  - **Real-world Example**: A mapping project for creating 3D models of a historical monument where every point needs to be accurately placed.

---

This detailed explanation of hyperparameters with real-world examples will help you make more informed decisions about your Agisoft Metashape project settings, allowing you to balance processing time, memory usage, and accuracy according to your specific needs.

## Agriculture and Vegetation Mapping Studies

When conducting agricultural or vegetation mapping studies, the primary goal is to capture detailed and accurate representations of plant life, land cover, and environmental features. The following hyperparameters from **Agisoft Metashape** are particularly suited for these types of studies:

---

### 1. **Accuracy (Alignment Stage)**

For vegetation mapping, **accuracy** is crucial, especially when working with detailed imagery of vegetation structure, plant types, or soil conditions. A higher accuracy setting will ensure that the model aligns properly with the ground features.

- **High**:
  - **When to use**: Ideal for smaller agricultural fields or vegetation surveys where precision in capturing plant details and land features is necessary.
  - **Real-world Example**: Mapping a specific plant species in a controlled environment, like a farm or botanical garden, where the exact positioning of plants relative to one another is important for analysis.

- **Highest**:
  - **When to use**: If vegetation health or small-scale changes (e.g., drought stress, growth patterns) need to be assessed with high precision.
  - **Real-world Example**: Vegetation stress analysis for agricultural crops, where precise camera alignment ensures that subtle variations in plant health are captured.

---

### 2. **Key Point Limit (Alignment Stage)**

In agricultural and vegetation mapping, the number of key points detected in each image directly affects the accuracy of identifying plants, soil types, and terrain features.

- **High Limit (e.g., 40,000-50,000)**:
  - **When to use**: For detailed vegetation mapping where higher-resolution imagery is available, ensuring that enough points are captured for accurate model alignment.
  - **Real-world Example**: Mapping the canopy of trees in a forest or plantation, where the terrain is complex and many features need to be identified.

- **Very High Limit (e.g., 100,000 or more)**:
  - **When to use**: For high-resolution imagery of small-scale vegetation (e.g., crops or individual trees), ensuring the best accuracy for detailed mapping.
  - **Real-world Example**: High-resolution mapping of a vineyard or orchard where the accuracy of individual plant positions is crucial for managing the crop.

---

### 3. **Depth Filtering (Dense Cloud Generation)**

In agriculture and vegetation mapping, **depth filtering** helps to remove noisy points that might be caused by dynamic elements like wind or changes in light, as well as irrelevant features such as cloud shadows.

- **Moderate**:
  - **When to use**: Suitable for large areas of agricultural land where some noise is present but not excessive.
  - **Real-world Example**: Aerial mapping of a large farming area where the soil or crop health needs to be assessed but the model must retain most features for analysis.

- **Aggressive**:
  - **When to use**: For dense vegetation or areas with lots of texture, like forests, where noise can obscure finer details.
  - **Real-world Example**: A dense forest mapping project, where the model needs to focus on the canopy structure, removing unnecessary noise that might come from other vegetation types.

---

### 4. **Resolution (Orthomosaic Generation)**

In agriculture and vegetation mapping, the **resolution** of the final orthomosaic determines how much detail you can extract from the images. Higher resolutions will capture more detail, which is essential for assessing plant health, species types, or crop conditions.

- **Medium (e.g., 2 cm/pixel)**:
  - **When to use**: For general vegetation surveys or crop monitoring, where moderate detail is enough to assess plant health and coverage.
  - **Real-world Example**: Mapping the distribution of crops across a farm, where the individual plants are not as important as the overall distribution.

- **High (e.g., 0.5 cm/pixel or finer)**:
  - **When to use**: For detailed vegetation studies where precise plant measurements or individual tree/crop assessments are required.
  - **Real-world Example**: High-resolution analysis of a garden, vineyard, or a small crop field where the goal is to study individual plants and their health status.

---

### 5. **Point Confidence (Dense Cloud Generation)**

In vegetation studies, **point confidence** helps ensure that only the most reliable points are used in the dense cloud generation. This is especially important when assessing the structure of vegetation, as any inaccurate points can lead to incorrect conclusions.

- **Medium Confidence**:
  - **When to use**: A balanced approach for standard vegetation mapping projects where a good level of point confidence is needed without overly slowing down processing.
  - **Real-world Example**: Mapping a forest or agricultural field where enough detail is needed for analysis, but the priority is on moderate accuracy.

- **High Confidence**:
  - **When to use**: For precise measurements of vegetation, such as studying tree height, canopy structure, or crop health, where the data quality is essential for accurate results.
  - **Real-world Example**: Assessing the health of individual trees or crops in a plantation where minor errors could impact the analysis of vegetation stress or growth.

---

By adjusting these hyperparameters appropriately, you can optimise your **Agisoft Metashape** workflow to suit the specific needs of agricultural and vegetation mapping studies. Whether you’re mapping large fields, individual crops, or dense forests, these settings will help balance processing time with the level of detail required for accurate analysis.

---

## Additional Resources

For further learning, refer to these helpful resources:

- [Agisoft Metashape Documentation](https://www.agisoft.com/downloads/user-manuals/)
- [Metashape User Forum](https://www.agisoft.com/forum/index.php)
- [Agisoft Metashape Tutorials on YouTube](https://www.youtube.com/results?search_query=agisoft+metashape+tutorial)

---

This guide should help you understand the basics of processing aerial images with **Agisoft Metashape**. As you get more comfortable, feel free to experiment with different settings to see how they affect your results.
