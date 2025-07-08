# 📸 Beginner’s Guide: UAV Photogrammetry Orthomosaic Resolution and Camera Geometry

This guide summarises key practical Q&A concepts about **Agisoft Metashape orthomosaic processing, GSD estimation, and camera geometry**, structured based on real processing queries for quick reference.

---

## ✨ **1. What is Camera Geometry?**

**Question:** What does camera geometry mean in photogrammetry?

**Answer:**

Camera geometry defines the **mathematical relationship between 3D real-world points and their 2D projections onto an image sensor**.

### ➡️ **Key Components**

1. **Intrinsic Parameters (Internal)**
   - Focal length
   - Principal point (cx, cy)
   - Sensor size and pixel size
   - Lens distortion parameters (radial, tangential)

2. **Extrinsic Parameters (External)**
   - Camera position (X, Y, Z)
   - Camera orientation (Roll, Pitch, Yaw)

### 🔬 **Why is it important?**
- Enables transformation between **2D image pixels and real-world 3D coordinates**.
- Forms the basis for **bundle adjustment**, dense reconstruction, and orthomosaic generation in Metashape.

---

## 📏 **2. How does Metashape estimate GSD without GPS data?**

**Question:** I processed images without geotags. How does Metashape estimate PGSD or GSD in this case?

**Answer:**

✅ **Metashape uses internal camera geometry and relative tie points.**

### ➡️ **How it works:**

1. Uses **camera intrinsic parameters** (focal length, sensor size) to define field of view.
2. Uses **relative image positions and tie points** to build an internally consistent 3D model.
3. Calculates PGSD (Projected GSD) based on the internal model scale.

⚠️ **However:**
- Without **GPS or GCPs**, the model has **no absolute scale**.
- Reported PGSD is **only relative**, not tied to real-world distances.

---

## 🔍 **3. Why does my processing report show resolution for one project but not another?**

**Question:** Both my RGB projects used untagged images in local coordinates. One report shows resolution (e.g. 6.37 mm/px), the other does not. Why?

**Answer:**

### ✅ **Possible reasons:**

1. **Surface type used for orthomosaic:**
   - **Point Cloud Surface:**  
     Uses dense cloud with assumed units (treated as meters) → **Metashape calculates and reports resolution**.
   - **Mesh Surface:**  
     Treated as **dimensionless geometry with texture mapping**, without defined real-world units → **resolution not reported**.

2. **Processing report settings:**
   - If orthomosaic build step is skipped or fails, resolution section is omitted.

3. **Alignment quality differences:**
   - Poor alignment results in unstable model scales → resolution calculation omitted.

---

## 🏔️ **4. Why does mesh surface processing omit resolution while point cloud surface shows it?**

**Question:** I processed with mesh surface – no resolution info; with point cloud surface – resolution appears. Why?

**Answer:**

✔ **Point Cloud Surface:**
- Dense cloud has spacing interpreted as meters in local CRS.
- Metashape calculates GSD from this spacing and camera parameters.

❌ **Mesh Surface:**
- Treated as a **3D model with no defined metric scale** in unscaled projects.
- Orthomosaic becomes a texture projection without calculable GSD in real-world units.

---

## 🛰️ **5. How does Metashape estimate correct GSD with geotagged images?**

**Question:** If my raw images have GPS data, how does Metashape calculate accurate GSD?

**Answer:**

✅ **Steps:**

1. Reads **camera intrinsic parameters** from EXIF or calibration:
   - Focal length
   - Sensor size
2. Uses **GPS altitude (ASL or AGL)** to estimate camera height above ground.
3. Calculates GSD using:

\[
GSD = \frac{H \times S}{f \times I}
\]

Where:
- **H** = Flight altitude above ground (mm)
- **S** = Sensor width (mm)
- **f** = Focal length (mm)
- **I** = Image width (pixels)

4. Refines GSD during **bundle adjustment** for final accurate reporting.

⚠️ **Note:** If GPS altitude is ASL (Above Sea Level), a DEM or GCPs improves true ground elevation and GSD accuracy.

---

## ✅ **6. Final Key Takeaways**

- **Always include scale constraints (GPS or GCPs)** for meaningful resolution and measurements.
- **Point cloud surfaces** provide resolution reporting even for unscaled projects.
- **Mesh surfaces** require scale bars or georeferencing for metric resolution reporting.

---

### 💡 **Next Steps**

For consistent Antarctic UAV processing:

- Add **scale bars or GCPs** even in untagged datasets.
- Document all processing settings for reproducibility.
- Consider exporting both **mesh-based and point-cloud-based orthomosaics** depending on analysis needs.

---

_Compiled for UAV photogrammetry beginner training and documentation._

