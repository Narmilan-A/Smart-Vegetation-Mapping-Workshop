# **DEM Editing Workflow Guide**  
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
# **Agisoft DEM Editing Tools – Full Documentation (Converted to Markdown)**

Source: Official Agisoft Helpdesk Article (converted for GitHub use)  
Original link: https://agisoft.freshdesk.com/support/solutions/articles/31000164388-dem-editing-tools

---

# **DEM Editing Tools – Agisoft Metashape Professional**

Starting from **Agisoft Metashape Professional 2.0.0**, DEM editing tools are available.  
DEM editing applies **directly to the surface**, allowing you to:

- Edit roof edges  
- Remove objects (cars, structures)  
- Fill holes or missing regions (water, forest canopy gaps)  
- Smooth noisy surfaces  

The following sections describe the **complete workflow**, all fill methods, and breakline tools.

---

# 📘 **Main Steps in DEM Editing**
1. Fill DEM tools  
   - Constant Filling  
   - Best‑Fit Plane  
   - IDW Interpolation  
   - Natural Neighbour Interpolation  
2. Create Breakline  
3. Resetting DEM Patches  
4. Applying Changes to DEM  

---

# ✏️ **Entering the DEM Edit Menu**
To edit the DEM, you must first **draw a polygon or polyline** covering the area to modify.

Example use case:  
A polygon is drawn around cars on a road so they can be removed and replaced with a smooth DEM surface.

---

# 🏷️ **Showing Labels**
To enable/disable shape labels in Ortho view:

```
Ortho > Show/Hide Items > Show Labels
```

---

# 📌 **Tool Availability**
- **Fill DEM** → works only on **polygons**
- **Create Breakline** → works on **polygons and polylines**

Right‑click a selected shape to access the editing tools menu.

---

# 🎛️ **Fill DEM Tools**

Four interpolation/filling methods are available:

1. Constant  
2. Best‑Fit Plane  
3. IDW  
4. Natural Neighbour  

Each method is detailed below.

---

# 1️⃣ **Constant Filling Method**

Fills the polygon area with **one constant elevation value**.

### Workflow:
- Select polygon  
- Open *Fill DEM*  
- Enter elevation manually **or** click **Pick** to sample elevation from the DEM  
- Apply

### Exclude Nested Polygons
If you want to exclude an internal region (such as a building):
1. Draw a second polygon **inside** the first  
2. Enable **Exclude nested polygons**

### Notes:
After any Fill or Breakline operation:
- Shape border becomes **dotted**  
- Border can still be edited  
- DEM patch will update accordingly

---

# 2️⃣ **Best‑Fit Plane Method**

Automatically computes a **plane** based on polygon vertices.

Useful for:
- Sloped roofs  
- Surfaces that are flat but not horizontal  

### Parameters:
- **Sample edges**: Uses entire polygon boundary for plane estimation  
- Works best when **Vertex Snap** is enabled  
  - After enabling Vertex Snap, **hold SHIFT** while drawing polygons  

---

# 3️⃣ **IDW (Inverse Distance Weighting) Interpolation**

Interpolation method where closer DEM points influence the output more strongly.

### Power Parameter:
- Default = **2**  
- Higher value (>2): closer points dominate → **more detailed surface**  
- Lower value (<2): smoother → **more homogeneous surface**

Useful for:
- Small canopy gaps  
- Areas with partial missing data  
- Forest DEM patches

---

# 4️⃣ **Natural Neighbour Interpolation (Recommended)**

A very high‑quality interpolation method based on **Voronoi neighbourhoods**.

Best for:
- Irregular surfaces  
- Forest canopy  
- Complex geometry  
- Smoother, more natural results

This is the **recommended default choice** for most DEM corrections in forests.

---

# 🪢 **Create Breakline Tool**

Breaklines enforce **linear elevation constraints**.

Uses:
- Roof edges  
- Road boundaries  
- Ditches or ridges  
- DEM transitions requiring sharp definition

How it works:
- Algorithm approximates left/right neighbouring regions with planes  
- Forces DEM to respect line boundaries

Orthomosaics built with breaklines show **crisper edges** compared to surfaces without them.

---

# 🗑️ **How to Reset DEM Editing**

## Delete Patch
To undo a patch **before applying updates**:
```
Edit DEM > Delete Patch
```

Important:
- Works ONLY **before** DEM Update is applied  
- After DEM Update → cannot undo  

To revert after applying updates:
- Rebuild DEM from dense cloud  
- Start DEM editing again

---

# 🔄 **How to Apply Changes to DEM**

Two ways to update DEM:

### 1. Toolbar Button
Click **Update** button on DEM toolbar.

### 2. Menu Path
```
Tools > DEM > Update DEM
```

Updating DEM finalises all pending patches and prepares DEM for orthomosaic generation.

---

# 📂 **Related Topics**
- Orthomosaic & DEM generation with GCPs  
- New features in Metashape 2.2.x  
- Vectorization tools  
- Transform DEM functionality  
- Point Cloud Classification  
- Thermal imagery processing  
- Processing R‑JPEG  
- Cloud processing guide

---

# **End of Document**  
This Markdown version is prepared for GitHub documentation and team training.
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
