# **Complete DEM Editing & Orthomosaic Workflow Guide (Beginner → Expert)**  
Author: Dr. Narmilan Amarasingam  
Reference link (Agisoft official DEM editing tools):  
https://agisoft.freshdesk.com/support/solutions/articles/31000164388-dem-editing-tools

---

# 🗂️ **Table of Contents**
1. What Is a DEM?  
2. How DEM Is Produced in Agisoft  
3. How an Orthomosaic Is Generated  
4. Full Workflow (Align → Dense Cloud → DEM → Ortho)  
5. How Each Step Connects (Expert‑Level Explanation)  
6. Why DEM Errors Cause Blur in Forest Orthomosaics  
7. What Is a Projection “Ray”?  
8. Why Wrong DEM Elevation Causes Horizontal Displacement  
9. DEM Editing Methodology — *Full A/B/C/1/2/3 Steps Directly from Agisoft + Expert Expansion*  
   - A. Fill DEM Tools  
     - 1. Constant Filling  
     - 2. Best‑Fit Plane  
     - 3. IDW  
     - 4. Natural Neighbour  
   - B. Create Breakline Tool  
   - C. Applying Changes to DEM  
10. Forest‑Specific Best DEM Editing Strategy  
11. Small vs Large Polygons — Which Is Proper for Forest Canopy?  
12. Final Recommendations  

---

# 📌 **1. What Is a DEM?**
A **Digital Elevation Model (DEM)** is a raster in which each pixel stores the **elevation (Z height)** of the surface.

- In forest: DEM = **dense canopy surface**, full of noise and spikes.  
- In open land: DEM is smoother and more stable.

DEM is foundational for orthorectification.

---

# 🏗️ **2. How Agisoft Produces a DEM**
1. Photos are aligned → camera positions, sparse cloud  
2. Depth maps are generated  
3. Dense point cloud is constructed  
4. DEM is interpolated from the dense cloud

DEM = the geometric surface for orthomosaic projection.

---

# 🛰️ **3. How an Orthomosaic Is Generated**
Agisoft projects each source image pixel onto the DEM using camera geometry.

Key idea:
```
Camera → Pixel → Ray → DEM → Ortho
```

If DEM is wrong → Ray hits wrong place → displaced/blurry orthomosaic.

---

# 🔗 **4. Workflow Connections**
| Step | Output | Feeds Into | Notes |
|------|--------|-----------|-------|
| Align Photos | camera positions | Dense Cloud | errors here propagate forward |
| Dense Cloud | 3D geometry | DEM | noisy forest = noisy DEM |
| DEM | 2.5D surface | Orthomosaic | DEM quality directly controls ortho clarity |
| Orthomosaic | final map | — | artefacts almost always caused by DEM issues |

---

# 🌲 **5. Why Forest DEMs Cause Ortho Blur**
Forest canopies produce:
- Many height spikes  
- Parallax effects  
- Shadows (missing points)  
- Irregular 3D shapes  

These generate *local DEM errors*.  
DEM errors distort pixel projection → blur patches appear.

---

# 🔦 **6. What Is a “Ray”?**
A **ray** is a line from:
```
Camera Center → Through Pixel → Downward → DEM Surface
```

Agisoft finds where that ray intersects the DEM.  
That becomes the pixel’s map location.

If DEM height is wrong, the ray hits the surface at the wrong point.

---

# ↔️ **7. Why Wrong DEM Elevation Causes Horizontal Displacement**
If DEM is *too high*:  
Ray intersects earlier → pixel shifts backward.

If DEM is *too low*:  
Ray intersects later → pixel shifts forward.

Although DEM error is **vertical**, projection creates **horizontal shift** → blur, ghosting, smearing.

---

# 🛠️ **8. DEM Editing Methodology (Full A/B/C + 1/2/3 from Agisoft Docs + Expert Explanation)**  
Official reference:  
https://agisoft.freshdesk.com/support/solutions/articles/31000164388-dem-editing-tools

Below is the **complete expanded methodology** for your GitHub guide.

---

# 🅐 **A. Fill DEM Tools (4 Methods)**

These tools let you correct faulty DEM regions.

## **1. Constant Filling**
- Fills selected polygon area with ONE constant elevation value.  
- Good for:  
  - Water bodies  
  - Flat concrete  
  - Carparks  
- **Not for forest** → produces fake flat canopy → causes strong distortions.

---

## **2. Best‑Fit Plane Filling**
Agisoft computes a flat plane that best matches surrounding DEM, then fills polygon.

- Good for flat ground  
- Not suitable for tree canopy  
- Will oversimplify complex shapes

---

## **3. IDW (Inverse Distance Weighting)**
Interpolates height using nearby DEM values; closer values weigh more.

- Good for:  
  - Small canopy gaps  
  - Small missing patches  
- Produces local smooth/original geometry  
- Works well in forest DEM correction

---

## **4. Natural Neighbour (Recommended for Forest)**
High-quality interpolation using Voronoi neighbours.

- Best for irregular surfaces  
- Smooth but realistic  
- Avoids sudden jumps  
- Ideal for forest canopy

**→ This is the recommended fill method for most forest DEM corrections.**

---

# 🅑 **B. Create Breakline Tool**
Purpose:
- Draw linear constraints (e.g., ridge, ditch, road edge)
- Force DEM to respect those lines as elevation boundaries

In forests:
- Sometimes useful along forest/road boundary  
- Helps avoid DEM collapsing into road or deep holes

Steps:
1. Draw polyline  
2. Assign elevation values  
3. Agisoft reshapes DEM to follow line

---

# 🅒 **C. Applying Changes to DEM**
After selecting polygons or breaklines:
1. Choose fill method  
2. Press **Apply**  
3. DEM regenerates locally  
4. Rebuild orthomosaic to see improvements

*Important:* Orthomosaic MUST be rebuilt after DEM editing.

---

# 📘 **9. Forest‑Specific Full DEM Editing Workflow**
Use this exact procedure:

1. Open DEM view  
2. Identify noisy canopy spikes, holes, warped crowns  
3. Draw **small polygons** around each artefact  
4. Fill with **Natural Neighbour**  
5. For medium gaps: use **IDW**  
6. Avoid flattening large forest areas  
7. Use breaklines along roads if needed  
8. Apply DEM changes  
9. Rebuild orthomosaic  
10. Evaluate → repeat for next noisy patch  

---

# 🟩 **10. Small vs Large Polygons (Critical)**

### ✔ Small Polygons (Recommended)
Edit only noisy areas.

**Advantages:**
- True canopy shape preserved  
- Minimises distortions  
- Best orthomosaic clarity  
- Most accurate representation  

### ❌ Large Polygon Over Entire Forest
**Never do this.**

Why:
- Flattens canopy  
- Removes natural 3D variation  
- Rays intersect incorrectly everywhere  
- Massive displacement → worse orthomosaic

---

# 🧩 **11. Final Recommendations**
- For forest: **Natural Neighbour** is always safest  
- Use many small local edits  
- Keep canopy geometry natural  
- Breaklines optional  
- Never flatten entire canopy  
- Always rebuild ortho after DEM editing  

---

# ✔️ END OF GUIDE  
You may now add screenshots to the `.md` and push to GitHub.  
