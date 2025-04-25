
# 🛰️ Orthomosaic Outputs from Multispectral and RGB Image Processing

****This repository documents the different types of orthomosaic outputs generated during multispectral and RGB imagery processing using Agisoft Metashape. It provides detailed explanations of reflectance correction, transparency (alpha channel), and best practices for scientific and machine learning workflows.****
---

## 🧠 Key Concepts

### 1. Band Reflectance Orthomosaic

- **Description:** Orthomosaic generated after radiometric calibration.
- **Pixel Values:** Surface reflectance (typically normalized to 0–1 or 0–100%).
- **Purpose:** Scientific analysis, vegetation indices (e.g., NDVI), temporal change detection.
- **Software:** Exported from Agisoft with `Reflectance` mode enabled.

### 2. Band Mosaic (Raw) Orthomosaic

- **Description:** Raw stitched image of a single band (e.g., Blue) without reflectance correction.
- **Pixel Values:** Raw digital numbers (DN) or brightness values.
- **Purpose:** Visualization, manual labeling, or input for deep learning pipelines.
- **Software:** Exported in `Mosaic` mode (no calibration applied).

---

## 🟣 What is the Alpha Channel?

The **alpha channel** is an additional image channel used to encode **transparency** (or "no-data" areas) in the orthomosaic.

### 🔍 How it works:

| Alpha Value | Meaning               |
|-------------|------------------------|
| 255         | Fully visible pixel    |
| 0           | Fully transparent (no data) |
| 1–254       | Semi-transparent (rare in orthomosaics) |

Agisoft automatically includes an alpha channel during orthomosaic export when you check the option:
```plaintext
[✓] Write alpha channel
```

### 📌 Why it's useful:

- Masks invalid or missing data (e.g., image edges, shadows, poor overlap).
- Helps avoid training machine learning models on meaningless data.
- Useful in GIS software and deep learning libraries to filter non-informative pixels.

---

## 📊 Example Table

| Output Type                    | Reflectance Corrected | Alpha Channel | Use Case                                |
|-------------------------------|------------------------|---------------|-----------------------------------------|
| `...reflectance_blue.tif`     | ✅ Yes                 | ✅ Yes        | Scientific analysis, NDVI, monitoring   |
| `...mosaic_blue.tif`          | ❌ No                  | ✅ Yes        | Visualisation, DL preprocessing         |

---

## 🧰 Using Alpha Channel in Python

```python
from PIL import Image
import numpy as np

# Load image
img = Image.open("AgMs_CG_D1F2to6_MR_step2_transparent_mosaic_blue.tif")
img_array = np.array(img)

# Extract RGB/Band and Alpha
band_data = img_array[:, :, 0]       # Blue band (or R/G/NIR, depending on file)
alpha_mask = img_array[:, :, 3]      # Alpha channel (transparency)

# Masking no-data areas
valid_pixels = band_data[alpha_mask == 255]
```

---

## 📌 Recommended Workflow in Agisoft Metashape

1. Import raw RGB or multispectral images.
2. Run alignment, dense cloud, and mesh generation.
3. Perform **radiometric calibration** (for reflectance outputs).
4. Build orthomosaic.
5. Export:
   - Enable **"Write alpha channel"**
   - Choose either **Mosaic** (raw) or **Reflectance** (calibrated)

---

## 🤖 Machine Learning Tip

When using orthomosaics in deep learning (e.g., U-Net, DeepLabV3+), apply the alpha channel mask to:

- Exclude invalid pixels from training.
- Improve generalization by ignoring edge artifacts.

---

## 🔗 Related Topics
- [Alpha Channel in TIF Images](https://en.wikipedia.org/wiki/Alpha_compositing)

---
