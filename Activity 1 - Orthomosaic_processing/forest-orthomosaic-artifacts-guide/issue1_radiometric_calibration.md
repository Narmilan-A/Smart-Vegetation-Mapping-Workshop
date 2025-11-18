## Issue 1 – Radiometric Calibration & Half Dark / Half Bright Orthomosaics

### Symptom

- Multispectral orthomosaic appears **half dark / half bright**, typically along the boundary between different flight routes or panels.  
- Looks similar to a giant “shadow” or sharp radiometric step across the scene.  
- Common in forest projects where **multiple calibration panels or flights** are used.

---

### Root Cause (from Agisoft Support)

- Using a **single combined radiometric calibration** for all routes causes inconsistent scaling.  
- This manifests as a sudden brightness jump between routes in the final reflectance mosaic.

---

### Recommended Strategies (Two Valid Options)

There are two general strategies to handle this problem when working with multiple flights and panel captures.

> **Key principle:** Each image block that experienced different illumination conditions should be **calibrated independently**, and then **merged** in a controlled way.

---

### ✅ Option 1 – Calibrate Each Chunk, Merge Chunks, Then Continue Processing

**Idea:**  
Separate your data into multiple chunks by flight/illumination block, perform **reflectance calibration per chunk**, then **merge chunks** and run the *rest* of the photogrammetry workflow only once.

#### 3.1. Workflow

1. **Split into chunks by flight / illumination block**
   - Create one chunk per flight or per group of images sharing:
     - The same calibration panel exposure(s)
     - Similar lighting conditions

2. **Run reflectance calibration in each chunk**
   - In each chunk:
     - Select that chunk’s calibration panel image(s)
     - Run the reflectance calibration step
     - Ensure the panel region is correctly detected and not shadowed/saturated

3. **Merge calibrated chunks**
   - Merge the chunks after calibration so that all calibrated images are together in a single chunk.
   - At this stage, each image already has the **correct per-block radiometric scaling**, but all images now live in a unified project.

4. **Run the rest of the workflow once (on the merged chunk)**
   - Align photos
   - (Optional) Build depth maps
   - Build dense cloud
   - Build DEM
   - Build **a single reflectance orthomosaic**

---

### ✅ Option 2 – Calibrate & Process Each Chunk to Orthomosaic, Then Merge Orthomosaics in GIS

**Idea:**  
Each flight/illumination block is treated almost like a separate project:  
You **calibrate and process each chunk all the way to orthomosaic**, then export the orthomosaics and merge them in a GIS (QGIS, ArcGIS, etc.).

#### 4.1. Workflow

1. **Split into chunks by flight / illumination block**
   - Same as in Option 1:
     - One chunk per flight or per illumination group
     - Each chunk gets its own calibration panel(s)

2. **For each chunk, perform full processing**
   - Per chunk:
     - Calibrate reflectance (using the correct panel image(s))
     - Align photos
     - Build dense cloud
     - Build DEM (if needed)
     - Build reflectance orthomosaic

3. **Export each orthomosaic**
   - Export each reflectance orthomosaic to GeoTIFF (or equivalent), ensuring:
     - Same projection/CRS
     - Correct georeferencing
     - Meaningful filenames (e.g. `route_A_ortho.tif`, `route_B_ortho.tif`, etc.)

4. **Merge orthomosaics in GIS**
   - Use a GIS like QGIS or ArcGIS:
     - Load all exported orthomosaics
     - Use raster mosaic / merge tools to create one continuous mosaic
   - **Important:**  
     - Each orthomosaic must **overlap spatially** with neighbouring orthomosaics to allow:
       - Seamless blending  
       - Proper edge handling
       - Requires sufficient **overlap between orthomosaics** for visually smooth merging.  

---
