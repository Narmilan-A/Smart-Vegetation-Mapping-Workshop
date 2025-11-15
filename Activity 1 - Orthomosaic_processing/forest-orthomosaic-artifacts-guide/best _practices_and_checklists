# **Best Practices & Checklist to Prevent Orthomosaic Artifacts in Forest UAV Projects**  
### *Image Quality • Field Workflow • Agisoft Settings • Processing Strategy • Troubleshooting*  
Author: **Dr. Narmilan Amarasingam**  

---

# 🌳 **Purpose of This Guide**  
This document provides a **professional, beginner-friendly checklist and workflow** to avoid common forest UAV processing problems such as:

- Swirled / melted canopy  
- Orthomosaic blur  
- BRDF striping  
- Noisy DEM / DSM  
- Radiometric mis-matches  
- Poor alignment or unstable reconstruction  

These errors almost always start from **image quality**, **illumination**, and **processing settings.**

Use this guide *before and during* processing.

---

# -------------------------------------------------------
# 📸 **1. IMAGE QUALITY – FIELD CHECKLIST (MOST IMPORTANT)**

### ✔ 1.1 Maintain stable exposure  
- Avoid strong alternation between bright sunlight and deep shadows.  
- Try to fly under **consistent sky conditions**.  
- Overcast skies produce the **best forest multispectral data** (diffuse light).  

### ✔ 1.2 Avoid overexposure and underexposure  
- Bright yellow flowers, wet leaves, bark highlights → can easily overexpose.  
- Deep shadows under canopy → underexposure leads to noisy depth maps.  

**Rule:** Histogram must be balanced. No clipping on either side.

### ✔ 1.3 Check image sharpness  
- No motion blur  
- No aggressive noise reduction (many sensors do this automatically)  
- Use highest possible shutter speed for forest flights  

### ✔ 1.4 Set consistent flight height & overlap  
- Recommended: **75–85% overlap** (both directions)  
- Higher overlap = more stable canopy reconstruction  
- Lower overlap = melted tree crowns  

### ✔ 1.5 Capture calibration targets correctly (for multispectral sensors)  
- Panel fully visible  
- No shadows  
- Sensor perpendicular to panel  
- Capture before and after flight  

---

# -------------------------------------------------------
# 🖥️ **2. IMAGE QUALITY – PRE-PROCESSING BEFORE AGISOFT**

### ✔ 2.1 Run Agisoft Image Quality Estimation  
In **Tools → Image Quality**  
- Values below **0.5** are problematic  
- Values **< 0.3** should be removed  

### ✔ 2.2 (Optional but recommended) Lightroom / RawTherapee Batch Enhancement  
For RGB images:  
- Adjust **Exposure** (small corrections only)  
- Correct **Highlights & Shadows**  
- Improve **Contrast** gently  
- Optional: Remove colour cast  

⚠ Never over-edit.  
⚠ Keep tonal relationships realistic or depth mapping will degrade.

---

# -------------------------------------------------------
# 🎛️ **3. CAMERA CHANNEL / PRIMARY CHANNEL SETUP**

Before alignment, set:  
**Tools → Camera Calibration → Primary Channel**  

For RGB:  
- Choose **Green** or **Luminance** (best for feature detection).  

For Multispectral:  
- Choose **highest resolution band**  
- Usually **Green or Red** (depending on sensor)  

This improves alignment stability dramatically.

---

# -------------------------------------------------------
# ⚙️ **4. DO NOT USE THE SAME HYPER-PARAMETERS FOR ALL FLIGHTS**

Even in the same site, forest reflectance changes with:  
- Time of day  
- Clouds  
- Flowering events (yellow, white blooming → high reflectance)  
- Soil moisture  
- Leaf wetness  

Agisoft recommends **adaptive settings**, not fixed presets.  

### Review in Agisoft Manual:  
- Depth Maps settings  
- Filtering settings  
- Tie point accuracy  
- Confidence thresholds  

---

# -------------------------------------------------------
# 🧪 **5. TWO PROCESSING STRATEGIES FOR BEGINNERS**

## ⭐ **Method A: Small Subset Test (Highly Recommended)**  
The workflow:  
1. Import ALL raw images.  
2. Select **20–50 images** from one section of the forest.  
3. Run the ENTIRE pipeline:  
   - Align  
   - Depth Maps  
   - Dense Cloud  
   - DEM  
   - Orthomosaic  
4. Evaluate quality carefully.  
5. If happy → apply same pipeline to full dataset.  

### Why?  
- Saves massive time  
- Helps detect unsuitable parameters early  
- Prevents reprocessing full dataset multiple times  

---

## ⭐ **Method B: Full Processing → Identify Artifacts → Re-process Only Problem Area**  

1. Process the **entire raw dataset** normally.  
2. Inspect final orthomosaic.  
3. If only **certain areas** have melting/blur:  
   - Extract that spatial area (using masks or chunk duplication)  
   - Re-process with different parameters  
4. Once you find optimal parameters, re-run full dataset using improved settings.

---

# -------------------------------------------------------
# 🛑 **6. COMMON FIELD MISTAKES TO AVOID**

### ❌ Flying near sunrise/sunset  
- Long shadows → depth errors  
- Low-angle sun → BRDF striping  

### ❌ Changing exposure mid-mission  
- Creates brightness jumps  

### ❌ Not overlapping orthomosaics when planning multi-mission merges  
- Chunks cannot be merged reliably  
- Causes strong seams  

### ❌ Very dark images  
- Low contrast → weak alignment  
- High noise → depth map corruption  

### ❌ Yellow flower patches not handled  
These areas often cause:  
- Reflectance saturation  
- Depth instability  
- Blurred canopy  
Fix: increase overlap + avoid noon harsh sunlight.

---

# -------------------------------------------------------
# 🗂️ **7. AGISOFT PROCESSING CHECKLIST**

## ✔ 7.1 Alignment  
- High Accuracy  
- Adaptive camera calibration enabled  
- Remove images with low quality scores  

## ✔ 7.2 Depth Maps  
- Use **Medium** quality first (test)  
- For final run: High or Ultra (only if GPU RAM allows)  
- Reduce noise: **Mild filtering** for forests  
- Use “pair preselection = Reference + Generic”  

## ✔ 7.3 Dense Cloud  
- Inspect for holes and spikes  
- Clean aggressively before DEM generation  

## ✔ 7.4 DEM  
- Inspect canopy DSM  
- Patch locally using Natural Neighbour  
  Reference:  
  https://agisoft.freshdesk.com/support/solutions/articles/31000164388-dem-editing-tools

## ✔ 7.5 Orthomosaic  
- Check seamlines  
- Patch texture using Assign Images  
  Reference:  
  https://agisoft.freshdesk.com/support/solutions/articles/31000148853-orthomosaic-seamline-editing-patching-

---

# -------------------------------------------------------
# 🧭 **8. ADVANCED STRATEGIES TO REDUCE MELTING / BLUR**

### ✔ Increase side overlap  
More overlap = more stable canopy height = less swirling.

### ✔ Fly cross-hatch pattern (double grid)  
Critical for forest structure.

### ✔ Avoid windy conditions  
Tree movement creates reconstruction ambiguity.

### ✔ Use lower altitude for dense canopy  
Improves parallax → reduces DEM errors.

### ✔ Bright flowering patches  
Capture under **diffuse light** to avoid oversaturation.

---

# -------------------------------------------------------
# 📦 **9. Summary – Beginner-Friendly Workflow**

