# Orthomosaic Seamline Editing & Fill (Agisoft Metashape)

This document describes how to **manually improve orthomosaics** by controlling which source images are used in specific areas and how to fill gaps or unavoidable objects.

Reference:  
- Agisoft Orthomosaic seamline editing (patching): https://agisoft.freshdesk.com/support/solutions/articles/31000165496-orthomosaic-seamline-editing-patching

---

## 1. When to Use Orthomosaic Editing

Use orthomosaic editing when:
- A specific object looks wrong (car, building, tree crown) even though DEM is acceptable.  
- There is a **blurred strip along the flight path** only in certain regions.  
- You see shadows, ghosting, or mixed textures that appear image‑choice related.  
- You want to choose a **different image** (e.g., better sun angle, less motion blur) for a region.

DEM editing fixes **geometry**; orthomosaic editing fixes **which image textures** are used.

---

## 2. Enabling Seamline Visualization

To see how Agisoft automatically stitched images:

1. Open **Ortho view** (double‑click the orthomosaic in Workspace).  
2. Click **Show Seamlines** button in the Ortho toolbar.

This shows all automatically generated seamlines.

---

## 3. Manual Patching with “Assign Images”

### Step 1 – Draw a Polygon

In Ortho view:
- Use **Draw Polygon** tool.  
- Delineate the exact area that needs re‑texturing (e.g., a blurred tree cluster, a car, a house).

### Step 2 – Assign Images

Right‑click the polygon →  
`Edit Orthomosaic > Assign Images...`

In the **Assign Images** dialog:
- Select the best image from the list.  
- Inspect the preview to confirm that the artifact is resolved.

Options:
- **Allow multiple selection** – assign several images to patch area.  
- **Exclude selected images** – block specific images from texturing that region (preview shows excluded image, not final result).

### Step 3 – Confirm and Mark Patch

- Click **OK**.  
- Polygon area will be displayed with a **blue mesh** overlay, indicating pending changes.

### Step 4 – Apply Changes

To commit all patches:
- Click **Update Orthomosaic** (toolbar or orthomosaic context menu).

The Ortho view will refresh and display the patched region.

---

## 4. Faster Patching with “Draw Patch”

When you need to apply many similar patches (for example along a blurred strip):  

1. In Ortho view, select **Draw Patch** tool from the Ortho menu or toolbar.  
2. Draw polygon around an artifact area.  
3. Metashape automatically assigns what it considers the **best image**, based on the position of the **first vertex** you clicked.

Then:
- Click **Update Orthomosaic** to apply all patches.

This is faster than manually opening Assign Images each time.

---

## 5. Fill Orthomosaic Tool

The **Fill** tool is used when:
- The object exists in **all** photos and cannot be replaced by another image (e.g., permanent structure you want visually removed).  
- There is a **data gap** – an area not covered by any images.  

### Steps:

1. Draw polygon around the area to fill.  
2. Right‑click → `Edit Orthomosaic > Fill`.  
3. Click **Update Orthomosaic** to apply the fill.

This replaces the interior of the polygon with a neutral texture that doesn’t come from a single specific image, suitable for hiding unavoidable artefacts or filling holes.

### Disabling Fill for a Polygon

If you decide not to use fill for a polygon:

- Right‑click polygon → `Edit Orthomosaic > Delete Patch`  
- Then **Update Orthomosaic** to clear it from pending edits.

⚠ **Important:**  
- Edits only become permanent after **Update Orthomosaic**.  
- After Update, you cannot “undo” individual fills—you would need to regenerate the orthomosaic.

---

## 6. Overlapping Polygons – Best Practice

Agisoft recommends:
- Avoid overlapping polygons where Fill will be used.  
- If overlap cannot be avoided, draw a **single larger polygon** that encompasses all relevant objects.

This ensures a clean, consistent fill region.

---

## 7. Combining DEM Editing and Orthomosaic Editing

For complex forest artifacts (e.g., “melting” canopy):

1. **First fix geometry** via DEM editing (see `dem_editing_forest.md`).  
   - Smooth noisy canopy with Natural neighbour/IDW.  
   - Update DEM and rebuild orthomosaic.

2. Then apply **orthomosaic seamline editing**:
   - Use Assign Images or Draw Patch to select the best images in remaining problematic areas.  
   - Use Fill only where no clean images exist.

This combined workflow yields a geometrically sound and visually stable forest orthomosaic.

