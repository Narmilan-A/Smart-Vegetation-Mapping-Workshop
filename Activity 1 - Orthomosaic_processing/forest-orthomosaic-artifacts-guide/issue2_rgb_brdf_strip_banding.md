## Issue 2 – RGB Orthomosaic Blurred Strip / Banding Along Flight Path

This document explains the **blurred/bright/dark strip along the flight path** in RGB orthomosaics and practical fixes using color calibration and orthomosaic editing.

---

### 1. Symptom

- A visible **strip or band** runs along the flight direction in the RGB orthomosaic.  
- The band may be slightly blurred or show different brightness/colour compared to neighbouring areas.  
- Appears even when DEM is reasonable and alignment is good.

---

### 2. Root Cause – BRDF and Low Sun Angle

Agisoft support explanation:

> Lines on the orthomosaic seem to be caused by BRDF effect, as due to low sun the brightness of the images is not uniform and one side is darker depending on the relative orientation of the sun and camera.

Key points:
- BRDF = Bidirectional Reflectance Distribution Function.  
- At low sun angles:
  - Image brightness varies strongly with viewing direction.  
  - Adjacent flight lines may have different illumination.  
- Agisoft stitches images with different brightness, creating visible seam lines.

This is a **radiometric/illumination** issue, not solely geometric.

---

### 3. Recommended Fix – Calibrate Colors

Agisoft suggests:

> You can get somewhat improved results if **Calibrate Colors** is used prior to the orthomosaic generation.

Menu:
- `Tools > Calibrate Colors`

#### 3.1 Choosing Source Data

The **Source data** parameter controls which surface is used to estimate overlapping brightness:

- **Tie Points** – fastest, rough estimation.  
- **Model** – more precise, but requires a good mesh (suitable for texture).  
- **DEM** – good compromise for large datasets where mesh is not feasible.

For forest projects:
- If you have a **good DEM** → choose **DEM**.  
- If you have a reliable, detailed mesh → try **Model**.  
- Avoid Tie points except for quick tests.

#### 3.2 Recommended Steps

1. Complete camera alignment, dense cloud, and DEM.  
2. Run `Tools > Calibrate Colors` using **DEM** or **Model** as source.  
3. Only then build the orthomosaic.  
4. Evaluate if striping/banding is reduced.

Note: color calibration can be **computationally expensive** for large projects.

---

### 4. Local Fix – Seamline Editing (Patching)

If the strip or band is present only in **specific areas**, combine color calibration with local orthomosaic editing (see `orthomosaic_seamline_editing.md`):

1. In Ortho view, draw a polygon around the problematic strip.  
2. Use `Edit Orthomosaic > Assign Images...` to choose a better image (with more consistent brightness).  
3. Or use **Draw Patch** tool to quickly assign best images.  
4. Update orthomosaic to apply patches.

This is particularly helpful when a few flight lines are affected by low sun while others are acceptable.

---

### 5. Forest‑Specific Considerations

- Forest canopy reflectance is highly directional; BRDF effects are strong at **low sun angles**.  
- Try to plan flights with:  
  - Higher sun angle where possible.  
  - Consistent acquisition pattern.  
- Avoid big gaps in time between adjacent flight lines.

Even with good planning, BRDF may still cause seam lines. Color calibration + seamline editing is the practical solution.

