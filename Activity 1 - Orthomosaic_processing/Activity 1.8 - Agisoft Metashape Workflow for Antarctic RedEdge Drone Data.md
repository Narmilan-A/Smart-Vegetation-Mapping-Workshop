# Agisoft Metashape Workflow for RedEdge Drone Data

## 📦 Input Requirements

- **Sensor:** MicaSense RedEdge (5-band multispectral)
- **Images:** Geo-tagged TIFFs (from drone flight)
- **Positioning:** RTK-enabled GNSS with centimeter-level accuracy
- **Image Structure:** Maintain MicaSense folder structure (per-capture folders)

---

## 🛠 Recommended System Specs

- **RAM:** 64 GB or more
- **GPU:** NVIDIA RTX A6000 or similar
- **CPU:** 8+ cores
- **Software:** Agisoft Metashape Pro 2.0.x+

---

## 📁 Project Setup

1. **Create New Project** in Metashape.
2. **Import Images via:**  
   `File > Import > Import MicaSense Dataset`  
   (Preserves band stacking and GPS metadata.)

---

## 🧭 Step 1: Image Alignment

```
Accuracy:               Medium
Generic Preselection:   Enabled
Reference Preselection: Disabled (see RTK note below)
Key Point Limit:        40,000
Tie Point Limit:        20,000
Exclude Stationary Tie Points: Off
Guided Matching:        Enabled (optional for problematic datasets)
```

> Use "Medium" accuracy to increase alignment success in low-texture areas.

---

### 📍 RTK Note (Important)

Even with high-precision **RTK GNSS**, it is often better to **disable reference preselection** in Antarctic or multispectral workflows due to:

- **Band-wise GPS variance** in RedEdge captures
- **Visual overlap not always matching GPS proximity**, especially in low-texture terrain
- **Small RTK drift or temporary fix loss** that can disrupt image pair filtering

✅ **Best Practice:**  
- Leave **Generic Preselection ON** (uses image content)  
- Set **Reference Preselection to OFF** to ensure no valid matches are skipped

---

## ☁️ Step 2: Depth Maps

```
Quality:            High
Filtering Mode:     Mild
Max Neighbors:      32
```

> "High" quality captures more detail for terrain; "Mild" filtering keeps sharp features like crevasses or rock edges.

| Aspect                     | Medium Quality                                                                                        | High Quality                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| **Processing Time**        | Faster (significantly quicker)                                                                      | Much slower (can be 2-3x longer)                         |
| **Memory Usage**           | Moderate                                                                                            | High                                                     |
| **Point Cloud Detail**     | Good detail but fewer points in complex areas                                                       | Denser and more detailed point cloud                     |
| **Noise**                  | Moderate noise filtering                                                                            | Cleaner with better small feature representation         |
| **Final DEM & Ortho**      | Slightly less detailed surface model; minor loss in fine details                                    | More precise DEM, sharper edges, better texture in ortho |
| **Orthomosaic Resolution** | Same pixel resolution (based on input images) but spatial accuracy and sharpness may degrade slightly | Best possible spatial accuracy and sharpness             |

---

## 🌐 Step 3: Dense Point Cloud

```
Source:             Depth Maps
Classes:            Not classified
```

> Expect 10M–40M points depending on image overlap and surface features.

---

## 🏔 Step 4: DEM Generation

```
Source:             Dense Point Cloud
Interpolation:      Enabled
```

> DEM resolution will match the density of the point cloud. Use WGS84 or reproject to UTM/Polar Stereographic for GIS analysis.

---

## 🗺 Step 5: Orthomosaic

```
Surface:            DEM
Blending Mode:      Mosaic
Ghosting Filter:    Enabled
Hole Filling:       Enabled
Export Resolution:  Match native GSD (~5–6 cm/pixel typical)
```

> Final orthophoto will be full 5-band multispectral, 16-bit depth.

---

## 📤 Export Recommendations

- **Orthomosaic:** GeoTIFF (5-band), 16-bit
- **DEM:** GeoTIFF, float32 or int16
- **Point Cloud:** LAS/LAZ if needed for GIS/CAD
- **Projection:** EPSG:4326 (WGS 84) or EPSG:3031 (Antarctic Polar Stereographic)

---

## 🧪 QA & Troubleshooting

| Issue                        | Fix                                                                  |
|-----------------------------|----------------------------------------------------------------------|
| Some photos show "N/A"      | Use Medium accuracy + disable reference preselection                |
| Sparse point cloud          | Increase depth map quality to High or Ultra                         |
| Artifacts in orthomosaic    | Enable ghosting filter + check for moving features (snow, shadows)  |
| DEM looks flat or noisy     | Use Mild filtering + High quality depth maps                        |


---
