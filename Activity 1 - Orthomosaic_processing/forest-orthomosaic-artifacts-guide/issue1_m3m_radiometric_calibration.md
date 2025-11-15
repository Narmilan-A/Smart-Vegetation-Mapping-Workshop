## Issue 1 – Radiometric Calibration & Half Dark / Half Bright Orthomosaics

This document summarises the calibration issue and provides a recommended workflow based on Agisoft support feedback and forest‑focused experience.

---

### 1. Symptom

- Multispectral orthomosaic appears **half dark / half bright**, typically along the boundary between different flight routes or panels.  
- Looks similar to a giant “shadow” or sharp radiometric step across the scene.  
- Common in forest projects where **multiple calibration panels or flights** are used.

---

### 2. Root Cause (from Agisoft Support)

Agisoft’s response:

> If you have different calibration panel images for each route, you need to process the data separately in 3 different chunks and perform reflectance calibration separately for each route.

In other words:
- Each flight route uses a **different panel instance** (or lighting condition).  
- Using a **single combined radiometric calibration** for all routes causes inconsistent scaling.  
- This manifests as a sudden brightness jump between routes in the final reflectance mosaic.

---

## 3. Recommended Strategies (Two Valid Options)

There are two general strategies to handle this problem when working with multiple flights and panel captures.

> **Key principle:** Each image block that experienced different illumination conditions should be **calibrated independently**, and then **merged** in a controlled way.

---

## ✅ Option 1 – Calibrate Each Chunk, Merge Chunks, Then Continue Processing

**Idea:**  
Separate your data into multiple chunks by flight/illumination block, perform **reflectance calibration per chunk**, then **merge chunks** and run the *rest* of the photogrammetry workflow only once.

### 3.1. Workflow

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

### 3.2. Pros & Cons

**Pros**
- Geometry (alignment, DEM, orthomosaic) is solved in one consistent block.  
- Only **one orthomosaic** to manage and export.  
- Radiometry is handled correctly per flight before merging.

**Cons**
- Requires careful chunk management and correct merging order.  
- Assumes that calibration metadata is correctly preserved when merging.

---

## ✅ Option 2 – Calibrate & Process Each Chunk to Orthomosaic, Then Merge Orthomosaics in GIS

**Idea:**  
Each flight/illumination block is treated almost like a separate project:  
You **calibrate and process each chunk all the way to orthomosaic**, then export the orthomosaics and merge them in a GIS (QGIS, ArcGIS, etc.).

### 4.1. Workflow

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

### 4.2. Pros & Cons

**Pros**
- Very robust when flights are very different (lighting, dates, etc.).  
- Minimal complexity inside the photogrammetry software; integration is done in GIS.  
- Easy to re-merge or test different mosaic rules without reprocessing photogrammetry.

**Cons**
- You may end up with slightly different geometric solutions per chunk (small misalignments) if not carefully controlled.  
- Requires sufficient **overlap between orthomosaics** for visually smooth merging.  
- You manage multiple intermediate orthomosaic files.

---

## 5. Important Notes for Both Options

- **Panel usage**
  - Each radiometric block (flight/session) must use panel images from that same block only.
  - Avoid mixing panel captures taken under different sky conditions.

- **Overlap requirement (especially for Option 2)**
  - Plan flight lines and mission design so that:
    - Orthomosaics have adequate overlap (e.g., 20–30% spatial overlap)  
    - This allows GIS tools to merge them smoothly.

- **This is a radiometric problem**
  - DEM editing, seamline editing, and projection tuning **cannot fix** half dark / half bright issues caused by poor calibration.
  - Fix **calibration strategy first**, *then* worry about DEM and orthomosaic refinement.

---

## 6. Summary

To avoid half dark / half bright mosaics in multispectral forest projects:

- Always treat each flight or illumination block as a separate radiometric unit.  
- **Option 1 (Preferred):**  
  - Calibrate each chunk → merge chunks → process once to a final orthomosaic.  
- **Option 2 (Alternative):**  
  - Calibrate and process each chunk to its own orthomosaic → export → merge orthomosaics in GIS (with sufficient overlap).

Both approaches ensure consistent reflectance scaling and remove the characteristic dark/bright split caused by mixing multiple calibration conditions into a single calibration step.
