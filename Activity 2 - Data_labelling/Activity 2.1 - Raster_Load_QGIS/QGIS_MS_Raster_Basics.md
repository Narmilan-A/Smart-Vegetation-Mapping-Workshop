
# QGIS Beginner Guide: Multispectral Raster Basics

**Audience:** Beginners  
**Software:** QGIS 3.22+  
**Data type:** Multispectral rasters (e.g., GeoTIFF, VRT, JP2)

---

## 🎯 What You’ll Learn
- Load multispectral raster imagery in QGIS
- Understand bands and change band order
- Adjust brightness, contrast, and stretching
- Apply transparency using NoData values or Alpha band
- Build pyramids (overviews) for faster rendering
- Save and reuse visualization styles

---

## 1) Loading a Raster
**Option A – Drag & Drop**  
Drag the raster file (e.g., `image.tif`) into the **Layers** panel.

**Option B – Browser Panel**  
Enable via `View → Panels → Browser` → Navigate to folder → Double-click the raster.

**Option C – Menu**  
`Layer → Add Layer → Add Raster Layer` → Select file → **Add**.

> If your data comes as separate band files (e.g., B1.tif, B2.tif…), build a **Virtual Raster (VRT)**:  
> `Raster → Miscellaneous → Build Virtual Raster`. This creates a stacked file without duplicating data.

---

## 2) Inspect Raster Information
Right-click the layer → **Properties → Information**.  
Check:
- Number of bands
- Band names (B1, B2, NIR, etc.)
- Data type (UInt16, Float32)
- CRS (Coordinate Reference System)
- Presence of an Alpha band

---

## 3) Display a Color Composite (Band Order)
**Layer Properties → Symbology → Render type: Multiband color**  
Assign channels:
- **True Color:** (R = Red, G = Green, B = Blue) → Landsat 8 = 4–3–2, Sentinel-2 = 4–3–2
- **False Color (CIR):** (R = NIR, G = Red, B = Green) → Landsat 8 = 5–4–3
- **Custom composites:** assign any three bands

Click **Apply** to view.

---

## 4) Adjust Brightness & Contrast
In **Symbology** panel:
- **Contrast enhancement:** `Stretch to MinMax`
- **Min/Max values:** use `Cumulative count cut (2%)` for better contrast
- Adjust **Brightness / Contrast / Saturation** sliders as needed

---

## 5) Transparency & the Alpha Band

### 5.1 What is an Alpha Band?
An **Alpha band** is a special raster band that stores **transparency information**.  
- `0 = fully transparent` (invisible)  
- `255 = fully opaque` (visible)  
- Intermediate values = semi-transparent  

Think of it as a **built-in mask layer**. Many modern GeoTIFFs include an Alpha band to automatically hide NoData areas (e.g., black borders).

### 5.2 Using Transparency in QGIS
- **Option A – NoData Value:**  
  Go to **Properties → Transparency → Additional no data values**.  
  Add values such as `0` or `65535` if they represent empty pixels.

- **Option B – Use Alpha Band (Preferred):**  
  If the raster has an Alpha band, simply enable **Use Alpha Band**.  
  This is more precise than manually setting NoData values.

✅ **Recommendation:** Use the **Alpha band** if available; otherwise, set a NoData value.

---

## 6) Build Pyramids (Overviews)
Large rasters load slowly. **Pyramids** create downsampled versions for faster zooming.

Steps: Right-click raster → **Properties → Overviews**
1. Select resampling method:  
   - `Nearest` (sharp edges, classification)  
   - `Average` (imagery)  
2. Tick overview levels (default suggested is fine)  
3. Store internally (preferred) or as external `.ovr` file  
4. Click **Build Overviews**

---

## 7) Save & Reuse Styles
After configuring symbology:
- Right-click raster → **Properties → Style → Save Style → QGIS Layer Style File (.qml)**
- To reuse: **Load Style** from another raster

---

## 8) Singleband Rendering (Optional)
For inspecting one band:
- **Render type:** `Singleband gray`
- Choose band (e.g., NIR)
- Apply stretch and optional color ramps

---

## 9) CRS & Reprojection
- Check project CRS (bottom-right in QGIS)  
- To reproject raster: `Raster → Projections → Warp (Reproject)`

---

## ✅ Beginner Checklist
- [ ] Load raster (drag & drop)  
- [ ] Set symbology to Multiband color  
- [ ] Assign band order (True/False color)  
- [ ] Apply MinMax stretch (2% cut recommended)  
- [ ] Apply transparency (Alpha or NoData)  
- [ ] Build pyramids for speed  
- [ ] Save style for reuse  

---

*This guide is designed for GitHub repositories and course handouts. Feel free to reuse with attribution.*
