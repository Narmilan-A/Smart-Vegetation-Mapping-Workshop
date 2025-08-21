# 🎨 QGIS Raster Rendering Guide for Beginners

This guide helps you understand how **raster rendering** works in QGIS, and how to fix issues like:
- Raster appears **flat or one-colored** when zoomed out
- Colors look **inconsistent** when zooming in/out
- Your raster visualization doesn't match what you expect

Whether you're visualising vegetation indices (NDVI, MSAVI), DEMs, classification maps, or any raster data — this guide will help!

---

## 📸 What’s Going On?

QGIS uses **dynamic rendering** to speed up performance and improve appearance. By default, it:

- Resamples rasters when zoomed out (to speed things up)
- Auto-adjusts color contrast based on the current zoom window
- Tries to guess useful min/max values — which isn’t always accurate

This can lead to:
- Flat, low-contrast rasters at full view
- Beautiful detail only visible when zoomed in
- Inconsistent color rendering across views

---

## 🔧 Solutions to Improve Raster Visualization

Here are 3 powerful techniques you can apply — choose based on your needs:

---

### 🟡 Option 1: Use Fixed Min/Max for Consistent Colors

Good for: **Map making**, **consistent view across zoom levels**

#### 🔹 Steps:
1. Right-click your raster layer → **Properties**
2. Go to the **Symbology** tab
3. Under **Min / Max values**, change from:
   - `Cumulative count cut` ➜ **`Actual (Full extent)`**
4. Click **"Load"** to apply real min/max values
5. Choose a **color ramp** (e.g., `Viridis`, `RdYlGn`, or `Spectral`)
6. Click **OK**

📌 Tip: Use **"Stretch to MinMax"** under contrast enhancement for better results.

#### ⚠️ Limitation:
- Doesn't adapt to local variations when zoomed in — may hide subtle details.

---

### 🔵 Option 2: Turn Off On-the-Fly Resampling

Good for: **Detailed inspection**, **high-resolution rasters**, **pixel-perfect viewing**

#### 🔹 Steps:
1. Go to `Settings` → `Options` → **Rendering** tab
2. In the **Rasters** section:
   - ❌ Uncheck **"Zoomed-out resampling"**
   - ❌ Uncheck **"Use multi-threaded rendering"** (optional)
3. Click **OK**

🎯 This tells QGIS: *"Always show the full-resolution raster, even when zoomed out."*

#### ⚠️ Limitation:
- Can slow down QGIS, especially with large rasters or multiple layers.

---

### 🟢 Option 3: Create a Preview Raster for Faster Overview

Good for: **Quick browsing**, **interactive maps**, or **large area overview**

#### 🔹 Steps:
1. Go to `Raster` → `Conversion` → **Translate (Convert format)**
2. Input your original raster
3. Click **"… Advanced Parameters"**
4. Set a **larger output resolution** (e.g., 5–10x pixel size)
5. Save as `*_preview.tif`

✅ Now you can switch between your full-resolution raster (for analysis) and the preview raster (for fast viewing).

#### ⚠️ Limitation:
- You lose fine detail. Don’t use for analysis or measurements!

---

## 🧠 Understanding Min/Max Modes in QGIS

QGIS uses various **Min/Max modes** to decide how to stretch values into colors.

### 🎨 Min/Max Value Calculation Modes

| Mode                         | What It Does                                                                 | When to Use                             |
|------------------------------|-------------------------------------------------------------------------------|------------------------------------------|
| **User Defined**             | You manually enter the min/max values.                                       | When you know the exact value range (e.g., 0–1 for NDVI). |
| **Min / Max**                | Uses the absolute minimum and maximum pixel values from the raster.          | Best if raster values are clean and meaningful. |
| **Cumulative count cut**     | Ignores outliers. Uses e.g., 2–98% of values for better contrast.            | Ideal for rasters with noise or outliers. |
| **Mean +/- standard deviation** | Uses the mean ± N × standard deviation (e.g., ±2σ).                          | Good for normally distributed data like temperatures. |

---

## 🌐 Extent and Accuracy Settings

Located just under the Min/Max options in Symbology.

### 📍 Extent Options

| Option              | What It Uses                                     | Best For                           |
|---------------------|--------------------------------------------------|------------------------------------|
| **Current extent**  | Only uses what’s visible on screen               | Fast preview, not consistent       |
| **Updated canvas**  | Updates min/max as you move or zoom              | Avoid for consistent styling       |
| **Full raster**     | Uses *all pixels* in the raster file             | ✅ Recommended for stable visuals  |
| **Static extent**   | Locks current view as reference                  | Freezes symbology when panning     |

---

### 🧮 Accuracy Options

Affects how QGIS samples values for statistics:

| Option       | Description                               | Speed       |
|--------------|-------------------------------------------|-------------|
| **Exact**    | Reads every pixel — most accurate          | 🐢 Slow     |
| **Estimate** | Uses metadata/stats from file             | ⚡ Fast     |
| **Sampled**  | Reads a subset of pixels                  | 🚀 Medium   |

---

## 🧪 Cheat Sheet: Choosing the Right Settings

| Goal / Situation                         | Suggested Settings                                     |
|------------------------------------------|--------------------------------------------------------|
| NDVI or MSAVI (range 0–1)                | `User Defined` min/max + `Full raster` + `Exact`       |
| DEM or raster with extreme values        | `Cumulative count cut` + `Full extent` + `Sampled`     |
| General viewing                          | `Mean ± Std Dev` + `Sampled` + `Full extent`           |
| High-quality map export                  | `User Defined` + `Exact` + consistent color ramp       |
| Fast exploration                         | `Estimate` + `Current extent` (temporary only)         |

---

## 🧩 Interactive Tips

| Problem You See                         | Likely Cause                      | Try This                                   |
|----------------------------------------|-----------------------------------|--------------------------------------------|
| Raster looks like 1 color when zoomed out | Auto resampling + auto stretch   | Use Fixed Min/Max + Turn off resampling    |
| Raster shows details only when zoomed in | Dynamic contrast based on view   | Use Full Extent Min/Max                    |
| Very slow raster rendering              | Large rasters + full resolution  | Use preview raster for navigation          |
| Weird color shifts when panning         | Zoom-based color recalculation   | Set fixed Min/Max + consistent color ramp  |

---

## 🎯 Best Practices

✅ Use **Option 1** for map styling  
✅ Use **Option 2** for pixel-accurate analysis  
✅ Use **Option 3** for lightweight overviews  

🔁 You can even **combine them**! For example:
- Turn off resampling for your analysis layers
- Use a downsampled preview layer in the background

---

## 🙋 Need Help?

Still confused about raster rendering or performance? Here are some extra ideas:
- 💬 Use the **QGIS Help Forum**
- 🧠 Check raster statistics (`Raster` → `Miscellaneous` → `Information`)
- 🔍 Use `Identify Features` tool to inspect pixel values

---

_This guide is part of a beginner series on using remote sensing and raster data in QGIS. Contributions welcome!_
