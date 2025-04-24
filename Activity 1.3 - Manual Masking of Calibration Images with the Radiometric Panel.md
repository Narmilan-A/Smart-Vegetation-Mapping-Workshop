## Manual Masking for Reflectance Panel Calibration in Agisoft Metashape

This guide explains how to **manually mask reflectance panel images** in Agisoft Metashape for accurate **radiometric calibration** — especially useful when using sensors like MicaSense or Parrot Sequoia.

---

## 📌 Goal

To **mask out everything except the white reflectance panel** in calibration images, ensuring Metashape uses only valid regions for reflectance correction.

---

## 🧰 Requirements

- Agisoft Metashape (any version with radiometric calibration support)
- A set of **calibration images** containing the reflectance panel
- Known **reflectance values** for the panel (typically ~0.99 for white)
- A multispectral or RGB sensor

---

## 🪜 Step-by-Step Instructions

### ✅ 1. Create a Camera Group for Calibration Images
If the `Calibration images` folder is not automatically created:

1. In the **Workspace** pane, select the images containing the calibration panel.
2. Right-click on the selected images and choose:  
   `Move Cameras > New Camera Group`
3. Right-click on the newly created folder and rename it to:  
   `Calibration images`
4. Move all relevant calibration images into this folder.
5. **Disable** the calibration cameras by right-clicking and selecting **Disable Cameras**.

### ✅ 2. Open Calibration Image
- In the **Photos** pane, double-click a calibration image to open it.
- This image should contain your white reflectance panel.

### ✅ 3. Draw a Polygon Around the Panel
- Use the **Intelligent scissors Tool** from the toolbar.
- Carefully draw a selection **around only the white panel**, avoiding shadows and borders.

### ✅ 4. Invert the Selection
- Go to:  
  `Toolbar` → `Mask` → `Invert Selection`  
  _or press_ `Ctrl + Shift + I`

> Now everything **except the panel** is selected.

### ✅ 5. Add Selection to Mask
- Go to:  
  `Toolbar` → `Mask` → `Add Selection`  
  _or right-click and choose_ **"Add Selection to Mask"**

> 🔒 The masked area will appear shaded. The **unmasked (clear)** area should be **only the white panel**.

### ✅ 6. Repeat for All Bands
- In multispectral images, each band is treated separately.
- Use the **band switcher** (panel on the right side when image is opened) to switch between bands (e.g., Red, Green, NIR).
- Repeat the masking process for **each band** of **each calibration image**.

### ✅ 7. Input Reflectance Values
Once all bands are masked:

- Go to:  
  `Tools` → `Calibrate Reflectance Panels...`
- Select your calibration image.
- Enter known reflectance values for each band (e.g., 0.99 for white).
- Example: Mavic 3M - Multispectral Camera Band
   -Green (G): 560 ± 16 nm;-->0.474
   -Red (R): 650 ± 16 nm;-->0.473
   -Red Edge (RE): 730 ± 16 nm;-->0.47
   -Near infrared (NIR): 860 ± 26 nm;-->0.466

---

## 📸 Tips & Notes

- Use high zoom for precision when masking the panel edges.
- You can apply the same polygon shape across bands by using the **"Copy Masks"** feature.
- Always **double-check that only the panel is unmasked** before calibration.

---

## 💬 Definitions

| Term | Description |
|------|-------------|
| **Add Selection** | Adds selected area to mask (marks as excluded). |
| **Subtract Selection** | Removes selected area from existing mask (makes it usable again). |
| **Invert Selection** | Flips selected and unselected regions. Useful when selecting the panel only. |

---

## ✅ Summary

To prepare for manual reflectance calibration:
- Create a **Camera Group** for calibration images if necessary.
- **Mask all calibration images** and leave only the panel **unmasked**.
- Repeat the process for **each band**.
- Calibrate using known reflectance values.

---

## 🔗 Related

- [Agisoft Metashape Manual](https://www.agisoft.com/support/downloads/manuals/)
- [Generate and Edit Masks Manually (Agisoft)](https://agisoft.freshdesk.com/support/solutions/articles/31000153479#Generate-and-edit-masks-manually%C2%A0)
- [MicaSense Panel Reference](https://support.micasense.com)
