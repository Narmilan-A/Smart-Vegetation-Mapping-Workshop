# Issue 1 – Mavic 3M Radiometric Calibration & Half Dark / Half Bright Orthomosaics

This document summarises the **Mavic 3 Multispectral (M3M)** calibration issue and provides a recommended workflow based on Agisoft support feedback and forest‑focused experience.

---

## 1. Symptom

- Multispectral orthomosaic appears **half dark / half bright**, typically along the boundary between different flight routes or panels.  
- Looks similar to a giant “shadow” or sharp radiometric step across the scene.  
- Common in forest projects where **multiple calibration panels or flights** are used.

---

## 2. Root Cause (from Agisoft Support)

Agisoft’s response:

> If you have different calibration panel images for each route, you need to process the data separately in 3 different chunks and perform reflectance calibration separately for each route.

In other words:
- Each flight route uses a **different panel instance** (or lighting condition).  
- Using a **single combined radiometric calibration** for all routes causes inconsistent scaling.  
- This manifests as a sudden brightness jump between routes in the final reflectance mosaic.

---

## 3. Recommended Workflow – M3M Radiometric Calibration in Forests

### Step 1 – Separate Chunks per Route

1. Import all images.  
2. Divide them into **separate chunks**, one per route / panel session.  
3. Ensure that each chunk has its own set of calibration panel images.

### Step 2 – Per‑Chunk Reflectance Calibration

For each chunk:

1. Identify the correct calibration panel images.  
2. Run **Tools > Calibrate Reflectance** (or corresponding workflow step).  
3. Verify that the calibration panel region is correctly detected and classified.

Important:
- Do not mix panel images taken under very different lighting into a single calibration step.  
- Each chunk should be internally consistent in illumination + panel usage.

### Step 3 – Build Reflectance Orthomosaic per Chunk

For each chunk (route):

1. Align photos.  
2. Build dense cloud / DEM as appropriate.  
3. Build orthomosaic (reflectance).  
4. Check for smooth brightness across that individual mosaic.

### Step 4 – Merge Results (Optional)

If a single output covering all routes is required:

- Export calibrated orthomosaics per chunk.  
- Mosaic them externally in GIS (QGIS, etc.) using consistent rules.  
- Alternatively, merge chunks in Metashape only after radiometric calibration is correctly separated.

---

## 4. Forest‑Specific Notes

- Forest canopies have highly directional reflectance (BRDF effects). Inconsistent panel handling across routes **amplifies** those differences.  
- Ensure panel captures are:  
  - Clean (no shadows, reflections)  
  - Not saturated  
  - Captured close to flight time and under similar sky conditions

Mismanaged panel selection is a **radiometric problem**, not a geometry or DEM problem. Fix calibration first before adjusting DEM/orthomosaic.

