## **Forest Orthomosaic Artifact Correction**  

### 🌳 **Purpose of This Guide**
Forest environments generate the *most severe* photogrammetry distortions.

### File Structure
```
forest-orthomosaic-artifacts-guide/
    README.md   ← THIS FILE
    dem_editing_forest.md
    orthomosaic_seamline_editing.md
    issue1_m3m_radiometric_calibration.md
    issue2_rgb_brdf_strip_banding.md
    issue3_vegetation_melting_artifacts.md
```

---

### 🧭 **1. DEM Editing Theory – Forest Environments**
#### 🌲 Why Forest DEM == DSM (Not Ground DEM)
In forests:

- Drone sees **tree canopy**, not ground  
- Photogrammetry reconstructs **whatever surface is visible**  
- Dense cloud = canopy geometry  
- DEM = interpolated canopy DSM  

Thus:

```
DEM in forest = DSM canopy surface ≠ Bare-earth DEM
```

Forest DEMs contain:
- Height spikes  
- Voids under shadows  
- Parallax distortions  
- Mixed canopy heights  

These errors **distort orthomosaic geometry** when pixels are projected onto this noisy surface.

---

### 🏗️ **2. How Agisoft Creates a DEM**

1. **Align Photos**  
   - Identify matching features  
   - Solve camera positions + orientations  

2. **Build Depth Maps**  
   - Per-image depth estimation  

3. **Build Dense Cloud**  
   - Millions of 3D canopy points  

4. **Interpolate DEM**  
   - Convert dense point cloud → 2.5D raster  
   - Height for every DEM pixel  

5. **Use DEM for orthomosaic projection**

**If dense cloud is noisy → DEM is noisy → orthomosaic is distorted.**

---

### 🛰️ **3. How Orthomosaic Projection Works (Critical)**

For each pixel of every image:

1. A **ray** is generated from the **camera centre**  
2. The ray passes through that specific **image pixel**  
3. The ray intersects the **DEM surface**  
4. The X/Y location of the ray–DEM intersection becomes the pixel’s position in the orthomosaic  
5. Metashape selects the *best* image to texture that pixel  

If the DEM is incorrect → ray intersection is incorrect → pixel placed in wrong position → **blur, smear, ghosting**.

---

### 🔦 **4. What Exactly Is a Projection Ray? (Expert Explanation)**

A projection ray is:

```
A straight 3D line going:
Camera centre → through a pixel → downward → until it hits the DEM surface
```

Where the ray hits determines:
- Pixel's true ground position  
- Pixel's alignment relative to neighbours  
- Mosaic accuracy  

Noise in DEM = wrong ray intersection = wrong pixel position.

---

### ↔️ **5. Why Vertical DEM Errors Cause Horizontal Blur**

DEM height error → ray intersects at wrong place horizontally.

#### If DEM is too high  
Ray hits surface **sooner** → pixel shifts **backwards**

#### If DEM is too low  
Ray hits surface **later** → pixel shifts **forwards**

Thus:

```
Vertical error → Horizontal displacement → Melted canopy
```

This is why forest orthomosaics often show:
- Swirled branches  
- Double tree crowns  
- Sliding textures  
- Local blur patches  

Fixing DEM fixes projection.

---

### 🌲 **5. Forest-Specific DEM Best Practices**

✔ Use many **small polygons**  
✔ Always use **Natural Neighbour first**  
✔ Use **IDW** for micro-gaps  
✔ Avoid Constant/Plane unless non-vegetation  
✔ Rebuild orthomosaic after each DEM update  
✔ Review canopy stability after each patch  
✔ Only patch what is broken  

---
