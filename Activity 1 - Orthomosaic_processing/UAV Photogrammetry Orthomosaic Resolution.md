# 📸 Beginner’s Guide to UAV Photogrammetry in Agisoft Metashape

This guide summarises practical Q&A topics on **orthomosaic pixel size estimation, camera geometry, processing settings, and resolution reporting** to support your UAV remote sensing workflows.

---

## ✨ **1. How does Metashape estimate PGSD without GPS data?**

### ❓ **Question:**
I developed an RGB orthomosaic using Agisoft, but raw images lacked geotags. I produced an orthomosaic, and in the export and processing report found pixel size in meters. **How is it possible to estimate PGSD without GPS info?**

### ✅ **Answer:**

Even without GPS or external scale, **Metashape estimates PGSD (Projected Ground Sample Distance)** using:

1. **Camera intrinsic parameters**
   - Sensor pixel size + image width/height.
   - Focal length (from EXIF or calibration).

2. **Relative tie points**
   - Matching features between overlapping images.
   - Builds an internally consistent 3D model with relative dimensions.

3. **Estimated scene depth**
   - Approximate distance from camera to ground based on internal bundle adjustment.

🔬 **Key note:**
- The reported PGSD is **only relative**, not real-world accurate, because:
  - The model has no absolute scale.
  - E.g. Orthomosaic may report **5 cm/px**, but the map could be arbitrarily small or large in reality.

### 💡 **Why does it appear in the report?**

Because Metashape **automatically calculates PGSD** from:

- Scene depth
- Camera sensor size + image resolution

**Even if units are arbitrary** in local coordinates.

---

## 🛠️ **2. What is Camera Geometry?**

### ❓ **Question:**
What does camera geometry mean in photogrammetry?

### ✅ **Answer:**

**Camera geometry describes the mathematical relationship between 3D real-world points and their 2D projections onto the camera image plane.**

### ➡️ **Key Components:**

1. **Intrinsic Parameters (Internal)**
   - Focal length (f)
   - Principal point (cx, cy)
   - Sensor size and pixel size
   - Lens distortion parameters (radial, tangential)

2. **Extrinsic Parameters (External)**
   - Camera position (X, Y, Z)
   - Camera orientation (Roll, Pitch, Yaw)

### 🔬 **Importance in Photogrammetry:**

- Converts between **2D image pixels and 3D real-world coordinates**.
- Enables bundle adjustment, dense reconstruction, and orthomosaic generation.

---

## 🏔️ **3. Processing Parameter Effects: Alignment Quality, Surface Type, and Depth Map Quality**

### ❓ **Question:**
I processed RGB data for two sites with different parameters:

| Step | Site 1 | Site 2 |
|---|---|---|
| **Align Photos** | High | Highest |
| **Build Surface** | Point Cloud | Mesh |
| **Depth Map Quality** | - | High |

I got better quality images with **Highest alignment and Mesh surface** with high depth map quality. **Why?**

### ✅ **Answer:**

#### ✔ **a) Alignment Accuracy**
- **Highest alignment** uses maximum key points → better camera pose estimation → more accurate models.

#### ✔ **b) Surface Type: Point Cloud vs Mesh**
- **Point Cloud:** Orthomosaic projected onto dense cloud; may show noise if points are sparse.
- **Mesh:** Generates a triangulated continuous surface; produces smoother, higher-quality orthomosaics, especially in low-texture areas.

#### ✔ **c) Depth Map Quality**
- **Higher quality depth maps → denser, more accurate dense clouds and meshes**, leading to sharper orthomosaics.

---

### 💡 **Best Practice Workflow**

1. **Align Photos:** Highest
2. **Optimize Cameras**
3. **Build Depth Maps:** High or Ultra-high
4. **Build Dense Cloud**
5. **Build Mesh:** Prefer mesh for smooth surfaces
6. **Build Orthomosaic:** Use mesh as surface

⚠️ **Trade-off:** Higher settings = longer processing time and higher GPU memory demand.

---

## 📏 **4. Why does resolution appear in some processing reports but not others?**

### ❓ **Question:**
For the same untagged RGB dataset in local coordinates:
- Processing with **point cloud surface** shows resolution (e.g. 6.37 mm/px).
- Processing with **mesh surface** shows no resolution.

**Why?**

### ✅ **Answer:**

✔ **Point Cloud Surface**
- Dense cloud has internal unit spacing (interpreted as meters in local CRS).
- Metashape calculates GSD from this spacing + camera parameters → reports resolution.

❌ **Mesh Surface**
- Treated as dimensionless geometry for texture mapping.
- Without external scale (GPS/GCPs/scale bar), mesh units have no real-world meaning → resolution not reported.

---

## 🛰️ **5. How does Metashape estimate correct GSD with geotagged images?**

### ❓ **Question:**
If my raw images have GPS data, how does Metashape calculate accurate GSD?

### ✅ **Answer:**

Metashape uses:

1. **Camera intrinsics**
   - Focal length, sensor size (from EXIF or calibration)

2. **GPS altitude**
   - Provides camera height above ground (AGL or ASL)

3. **Standard GSD formula:**

\[
GSD = \frac{H \times S}{f \times I}
\]

Where:

- **H** = Flight altitude above ground (mm)
- **S** = Sensor width (mm)
- **f** = Focal length (mm)
- **I** = Image width (pixels)

4. **Bundle adjustment refinement**
   - Optimises camera positions/orientations, correcting GPS errors for final accurate GSD reporting.

---

### ⚠️ **Note:**
- If GPS altitude is ASL, integrating a **DEM or GCPs** ensures correct ground elevation for GSD accuracy.

---

## ✅ **6. Final Takeaways**

- **Without GPS or scale:** PGSD is relative, not real-world accurate.
- **Point cloud surfaces** → resolution reported; **mesh surfaces** → resolution omitted unless scaled.
- **Higher processing settings** (alignment, depth map, mesh) → better orthomosaic quality.
- Always include **GPS, GCPs, or scale bars** for meaningful resolution and measurements.

---

_Compiled for UAV photogrammetry beginner training and Antarctic processing documentation._
