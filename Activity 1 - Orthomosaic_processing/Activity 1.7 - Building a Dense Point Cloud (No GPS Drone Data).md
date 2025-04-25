# 🧱 Building a Dense Point Cloud (No GPS Drone Data)

Welcome to the next step in your drone image workflow!  
In this guide, we’ll cover how to build a **dense point cloud** in **Agisoft Metashape** when working **without GPS data**.

> 🎯 Goal: Create a high-quality 3D point cloud from aligned RGB drone images using visual features only.

---

## ✅ Where to Start

In Metashape, go to:  
**`Workflow → Build Dense Cloud`**

You'll see several parameters. Here’s how to set them for best results 👇

---

## ⚙️ Recommended Settings

| Parameter                       | Value                  | Why? |
|--------------------------------|------------------------|------|
| **Source Data**                | `Depth Maps` (default) | Uses your aligned images and tie points |
| **Quality**                    | `High` _(or Medium)_   | Best detail without excessive memory use |
| **Depth Filtering**            | `Moderate`             | Balances detail and noise removal |
| **Calculate Point Colors**     | ✅ `Enabled`            | Adds image-based color to your 3D points |
| **Calculate Point Confidence** | ✅ `Enabled`            | Helps you detect noisy or low-confidence areas later |
| **Replace Default Point Cloud**| ✅ `Enabled`            | Updates sparse view with dense cloud — better visuals |

---

## 📖 What Each Setting Means

<details>
<summary><strong>🧠 Source Data</strong></summary>

- Use the default: `Depth Maps`
- This means Metashape uses depth info calculated from image alignment — no GPS needed.
</details>

<details>
<summary><strong>🎚️ Quality</strong></summary>

- `High` = best balance of detail and speed  
- `Medium` = faster, good for testing  
- `Ultra` = super detailed, very slow and memory-intensive

> 🧪 Tip: Start with `Medium` to test, then reprocess at `High` for final output.
</details>

<details>
<summary><strong>🌊 Depth Filtering</strong></summary>

- Removes noise from the dense cloud
- `Moderate` = best balance for most natural surfaces
- `Mild` = more detail, more noise  
- `Aggressive` = very clean, may remove small features  
- `Disabled` = keep everything (not recommended for messy datasets)

> Best choice for vegetation, terrain, and mossy surfaces: **Moderate**
</details>

<details>
<summary><strong>🎨 Point Colors</strong></summary>

- ✅ Enable this to **color your 3D points** using the source images
- Makes visual inspection and presentations much clearer
</details>

<details>
<summary><strong>📊 Point Confidence</strong></summary>

- Adds confidence scores (0–255) to each point
- Useful if you want to **filter out unreliable areas** later (like sky, shadows, moving objects)

> Pro tip: You can color the dense cloud by confidence in the viewer.
</details>

<details>
<summary><strong>🔁 Replace Default Point Cloud</strong></summary>

- ✅ Recommended: updates your 3D view to show the new dense cloud instead of the sparse one
- Easier for visual checks and further processing
</details>

---

## 💡 Final Tips

- 📦 Save your project before building the cloud — it can take time!
- 🧪 Test at `Medium` quality first to preview results
- 🔍 Use `Point Confidence` later to clean up noisy areas
- 📊 Use `Moderate` filtering for most natural terrain types (rocks, moss, etc.)

---

## 🔗 Next Steps

Once your dense cloud looks good, you’re ready to:

- Build a **DEM (Digital Elevation Model)**  
- Generate an **Orthomosaic**  
- Export the point cloud for 3D use

> Want interactive guides for those too? Just ask!

---
