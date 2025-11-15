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

### 📌 3. Recommended Workflow – Forest‑Optimised (Preferred Method)

This is the **best workflow** when flying forests under variable light.

---

#### ✅ **STEP 1 — Split Images Into Per‑Route Chunks**

Example:

```
Chunk 1 → Route A + Panel A  
Chunk 2 → Route B + Panel B  
Chunk 3 → Route C + Panel C
```

Rules:
- Never mix panel images between chunks.  
- Never calibrate multiple routes together.  
- Keep each chunk internally consistent.

---

#### ✅ **STEP 2 — Perform Reflectance Calibration PER CHUNK**

For each chunk:

1. Go to **Tools → Calibrate Reflectance**  
2. Select that route’s calibration panel image(s)  
3. Confirm auto‑detected panel region  
4. Apply calibration  

⚠ DO NOT use panel images from another route  
⚠ DO NOT calibrate all routes together  
⚠ DO NOT mix sun conditions  

---

#### ✅ **STEP 3 — Process Each Chunk Fully (Until Orthomosaic)**  

For each chunk:

1. **Align Photos**  
2. **Build Depth Maps**  
3. **Build Dense Cloud**  
4. **Build DEM**  
5. **Build Reflectance Orthomosaic**

Each orthomosaic should appear:
- Evenly lit  
- Same reflectance scale  
- No jumps inside that chunk  

---

#### ✅ **STEP 4 — Merge Orthomosaics (HIGHLY RECOMMENDED)**  
##### ⭐ Preferred: Merge orthomosaics in GIS (QGIS / ArcGIS)

Why GIS mosaic?
- Avoids mixing radiometric models  
- Allows smooth blending  
- Keeps reflectance values stable  
- Robust for forests  

Requires:
- Orthomosaics must **overlap**  
- Same CRS for all chunks  

##### Workflow in QGIS:
```
Raster → Miscellaneous → Merge  
(or use Raster → Build Virtual Raster)
```

##### Alternative: Merge chunks inside Metashape  
Only acceptable if illumination was identical across routes.

---

### 📌 4. Forest‑Specific Notes

### 🌲 High BRDF Sensitivity  
Forest canopy reflectance varies dramatically with:
- Sun angle  
- View angle  
- Sky conditions  

Panel inconsistencies amplify BRDF differences.

### ☁ Lighting Stability Is Critical  
Panel images must be:
- Clean  
- Shadow‑free  
- Not overexposed  
- Captured closely before/after each flight line  

### 🎯 Radiometric Errors Cannot Be Fixed Using  
❌ DEM Editing  
❌ Seamline Editing  
❌ Orthomosaic Patching  

You must fix calibration FIRST.

---

## 📦 **Forest‑Optimised Deliverable Workflow Summary**

```
Split routes → Calibrate each chunk →  
Process each chunk →  
Export orthos →  
Merge in GIS →  
(then perform vegetation analysis)
```

Produces:
- No brightness jumps  
- No dark/bright splits  
- Clean spectral values  
- Correct NDVI/NDRE/GNDVI  
- Stable reflectance across the forest  

---
