# Issue 3 – “Melting” / Swirled Canopy Artifacts (M3M, P1, Altum PT)

This document explains the **“melting” or swirled vegetation artifacts** that appear in orthomosaics built from DJI Mavic 3M, DJI P1, and Micasense Altum PT data, especially in forest environments.

---

## 1. Symptom

- Tree crowns appear **melted**, swirled, or twisted in the orthomosaic.  
- Some canopy areas look like they are “flowing” or smeared.  
- Artifacts often correlate with high‑contrast canopy, steep geometry, or shadowed areas.

This issue appears consistently across different sensors → it is **not sensor‑specific**.

---

## 2. Root Cause – Noisy Surface / DEM

Agisoft support:

> The quality of orthomosaic depends on the quality of the alignment of the source data and the surface on which you use to build the orthomosaic. We can assume that the surface is noisy in these areas.

So:

- If the **DEM (DSM)** is noisy due to irregular canopy, shadows, or mis‑matches, the projection rays will intersect the surface incorrectly.  
- Trees may be projected partially onto wrong heights, causing **horizontal shifts** and 3D smear in the orthomosaic.

---

## 3. Recommended Fixes (from Agisoft + Best Practice)

Agisoft suggests two main strategies:

1. **Smooth the DEM in noisy areas** – DEM editing tools.  
2. **Edit the orthomosaic** – orthomosaic seamline editing (patching).

Best practice is to **start with DEM**, then refine with orthomosaic editing.

---

## 4. Step‑by‑Step Workflow

### 4.1 Check Alignment First

Before editing DEM:

1. Review camera alignment (look for: misaligned groups, large reprojection errors).  
2. If necessary, optimise camera alignment or remove badly aligned images.  
3. Ensure no gross alignment error is the main cause.

### 4.2 DEM Editing in Noisy Canopy (Geometry Fix)

Refer to `dem_editing_forest.md` for detail. Summary:

1. Switch to DEM view.  
2. Locate melting/swirl areas seen in the orthomosaic.  
3. Draw **small polygons** around local anomalies.  
4. Use **Fill DEM**:
   - Prefer **Natural neighbour interpolation**.  
   - Use **IDW** for smaller holes.  
5. Avoid Constant/Best‑fit plane for actual canopy.  
6. Click **Update DEM**.  
7. Rebuild orthomosaic.

If artifacts were caused by DEM noise, this often **stabilises canopy geometry**.

### 4.3 Orthomosaic Editing (Texture Fix)

After DEM correction:

1. In Ortho view, identify any remaining problematic areas.  
2. Use **Assign Images** or **Draw Patch** to pick the best image(s).  
3. Use **Fill** only where no good image exists or object is unwanted in all images.  
4. Click **Update Orthomosaic** to apply seamline edits.

This step fixes residual visual issues due to image choice or local radiometric differences.

---

## 5. Why This Happens in All Three Sensors (M3M, P1, Altum PT)

The consistent presence of melting artifacts across M3M, P1, and Altum PT indicates:

- It is primarily a **photogrammetric geometry + forest structure** problem, not a specific camera problem.  
- Dense, tall, and complex canopy with shadows creates:
  - Depth map instabilities  
  - Dense cloud noise  
  - DEM noise  
- Once orthomosaic projection uses this noisy DEM, **all sensors** will show similar artifacts.

Correcting DEM + orthomosaic, as described above, is the general solution regardless of sensor.

---

## 6. Summary

- “Melting” canopy = projection onto a noisy DEM (forest DSM).  
- Fix alignment issues first.  
- Then smooth DEM locally using Natural neighbour / IDW.  
- Finally refine visual texture via orthomosaic seamline editing.  
- This workflow is sensor‑agnostic and works for M3M, P1, Altum PT and other cameras in forest environments.

