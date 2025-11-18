## **Best Practices & Checklist to Prevent Orthomosaic Artifacts in Forest**  
---

### **Purpose of This Guide**  
This document provides a ** workflow** to avoid common forest UAV processing problems such as:

- Swirled / melted canopy  
- Orthomosaic blur  
- BRDF striping  
- Noisy DEM / DSM  
- Radiometric mis-matches  
- Poor alignment or unstable reconstruction  

These errors almost always start from **image quality**, **illumination**, and **processing settings.**

Use this guide *before and during* processing.

---

### **1. IMAGE QUALITY – FIELD CHECKLIST (MOST IMPORTANT)**

#### ✔ 1.1 Maintain stable exposure  
- Avoid strong alternation between bright sunlight and deep shadows.  
- Try to fly under **consistent sky conditions**.  
- Overcast skies produce the **best forest multispectral data** (diffuse light).  

#### ✔ 1.2 Avoid overexposure and underexposure  
- Bright yellow flowers, wet leaves, bark highlights → can easily overexpose.  
- Deep shadows under canopy → underexposure leads to noisy depth maps.  

**Rule:** Histogram must be balanced. No clipping on either side.

#### ✔ 1.3 Check image sharpness  
- No motion blur  
- No aggressive noise reduction (many sensors do this automatically)  
- Use highest possible shutter speed for forest flights  

#### ✔ 1.4 Set consistent flight height & overlap  
- Recommended: **75–85% overlap** (both directions)  
- Higher overlap = more stable canopy reconstruction  
- Lower overlap = melted tree crowns  

#### ✔ 1.5 Capture calibration targets correctly (for multispectral sensors)  
- Panel fully visible  
- No shadows  
- Sensor perpendicular to panel  
- Capture before and after flight  

---

### **2. IMAGE QUALITY – PRE-PROCESSING BEFORE AGISOFT**

#### ✔ 2.1 Run Agisoft Image Quality Estimation  
In **Tools → Image Quality**  
- Values below **0.5** are problematic  
- Values **< 0.3** should be removed  

#### ✔ 2.2 (Optional but recommended) Lightroom / RawTherapee Batch Enhancement  
For RGB images:  
- Adjust **Exposure** (small corrections only)  
- Correct **Highlights & Shadows**  
- Improve **Contrast** gently  
- Optional: Remove colour cast  

---

### **3. CAMERA CHANNEL / PRIMARY CHANNEL SETUP**

Before alignment, set:  
**Tools → Camera Calibration → Primary Channel**  

For RGB:  
- Choose **Green** or **Luminance** (best for feature detection).  

For Multispectral:  
- Choose **highest resolution band** (depending on sensor)  

---

### **4. DO NOT USE THE SAME HYPER-PARAMETERS FOR ALL FLIGHTS**

Even in the same site, forest reflectance changes with:  
- Time of day  
- Clouds  
- Flowering events (yellow, white blooming → high reflectance)  
- Soil moisture  
- Leaf wetness  

Agisoft recommends **adaptive settings**, not fixed presets.  

#### Review in Agisoft Manual:  
- Depth Maps settings  
- Filtering settings  
- Tie point accuracy  
- Confidence thresholds  

---

### **5. TWO PROCESSING STRATEGIES FOR BEGINNERS**

#### **Method A: Small Subset Test (Highly Recommended)**  
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

#### Why?  
- Saves massive time  
- Helps detect unsuitable parameters early  
- Prevents reprocessing full dataset multiple times  

---

#### **Method B: Full Processing → Identify Artifacts → Re-process Only Problem Area**  

1. Process the **entire raw dataset** normally.  
2. Inspect final orthomosaic.  
3. If only **certain areas** have melting/blur:  
   - Extract that spatial area (using masks or chunk duplication)  
   - Re-process with different parameters  
4. Once you find optimal parameters, re-run full dataset using improved settings.

---

### **6. AGISOFT PROCESSING CHECKLIST**

#### ✔ 6.1 Alignment  
- High Accuracy  
- Adaptive camera calibration enabled  
- Remove images with low quality scores  

#### ✔ 6.2 DEM  
- Inspect canopy DSM  
- Patch locally using Natural Neighbour  
  Reference:  
  https://agisoft.freshdesk.com/support/solutions/articles/31000164388-dem-editing-tools

#### ✔ 6.3 Orthomosaic  
- Check seamlines  
- Patch texture using Assign Images  
  Reference:  
  https://agisoft.freshdesk.com/support/solutions/articles/31000148853-orthomosaic-seamline-editing-patching-

---
### **6. RECOVER POOR ALIGNMENT**
#### Why Poor Alignment Happens (Forest Projects)**
- Wind → canopy movement → inconsistent features  
- Very dark images → low contrast → unstable feature detection  
- Excessive shadows → repeated patterns → false matches  
- Flying too low or too high → lack of parallax or insufficient texture  
- Flight lines not overlapping enough  
- Bad weather → haze, fog, low-light  
- Motion blur due to aggressive UAV speed  

#### **8. Tools in Agisoft to Recover Poor Alignment**

##### **A. Manually Placed Markers (Highly Effective)**  
###### 🔍 *When to use:*  
- Images refuse to align  
- Small cluster of photos won't register  
- Alignment has holes / empty pockets  
- GPS/RTK is missing or inaccurate  

###### **What markers do:**  
Markers tell Agisoft:  
> “These image pixels correspond to the same physical point on the ground.”

This forces the software to fix alignment even when the automatic feature matching fails.

#### **Step-by-Step – Adding Markers to Fix Alignment**

##### **1. Open the "Photos" or "Workspace" panel**
- Double-click an image to open it  

##### **2. Choose a strong, stable feature**
Good candidate features:
- Rock edges  
- Large logs  
- Road markings  
- Building edges  
- Distinct tree trunks  
- Unmoving man-made objects  

##### **3. Right-click → Add Marker**
Metashape will place a marker in that image.

##### **4. Now switch to another overlapping image**
- The marker will appear faint (estimated location)
- Drag it to the exact matching pixel

##### **5. Repeat across 6–10 images**
- Each marker should be placed in **at least 6 images**
- More = stronger geometry

##### **6. Add 5–20 markers total**
- Spread markers throughout the affected area  

##### **7. Run "Optimize Cameras"**
---

