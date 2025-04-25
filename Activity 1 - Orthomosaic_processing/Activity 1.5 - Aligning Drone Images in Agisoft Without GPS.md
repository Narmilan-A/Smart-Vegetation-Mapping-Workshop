# 🚁 Aligning Drone Images in Agisoft Without GPS

Welcome! 📸  
This guide shows how to align drone images **without GPS data** in **Agisoft Metashape** — step-by-step, beginner-friendly, and perfect for RGB images from non-GPS drones.

---

## 🧭 Can I Make an Orthomosaic Without GPS?

> **Short answer:** Yes, you can! 🙌

Agisoft Metashape can:
- Align images using **visual features** (Structure from Motion)
- Build point clouds, meshes, and orthomosaics  
- Do all this **without any GPS data**

But — your output will be in **local coordinates** (not real-world positions) unless you add extra data like GCPs or scale bars.

---

<details>
<summary>📌 Limitations (click to expand)</summary>

- ❌ No real-world coordinates
- ❌ No proper scale unless:
  - You use **Ground Control Points (GCPs)**
  - Or define **known distances** in the scene

</details>

---

## ✨ Pro Tips Before You Start

- 🔁 Ensure **70–80% front overlap** and **60–70% side overlap**
- 🔍 Use **sharp, clear images** with consistent lighting
- ⚠️ Avoid blurry or overexposed frames
- 📏 Include **measurable objects** if you want to scale later

---

## ⚙️ Recommended Alignment Settings

Use these when going to `Workflow → Align Photos`.

| Setting                        | Value         | Why It Matters |
|-------------------------------|---------------|----------------|
| **Accuracy**                  | `High`        | Good detail without being too slow. `Medium` is fine on low-end PCs. |
| **Generic Preselection**      | ✅ `Enabled`   | Helps Metashape skip bad matches. Faster and smarter. |
| **Reference Preselection**    | ❌ `Disabled`  | You don’t have GPS — turn this off. |
| **Key Point Limit**           | `40,000`      | Default is great. Only raise if things don’t align well. |
| **Tie Point Limit**           | `10,000`      | Good balance. Raise to 20–50k if you have complex terrain. |
| **Exclude Stationary Tie Points** | ✅ `Enabled` | Filters out noise like shadows or lens dust. |
| **Guided Image Matching**     | ❌ `Disabled`  | Requires GPS — skip it. |
| **Adaptive Camera Model Fitting** | ✅ `Enabled` | Auto-optimizes camera settings. Super helpful with non-calibrated drones. |

---

<details>
<summary>🤓 What Do These Settings Actually Do? (Click to explore)</summary>

### Accuracy
- Controls image resolution for matching.
- `High` is the sweet spot.
- `Highest` is slow with minimal gains.

### Generic Preselection
- Speeds up processing by comparing only promising image pairs.

### Reference Preselection
- Relies on GPS — disable it for non-GPS datasets.

### Key & Tie Points
- Key = features per image  
- Tie = matched features between overlapping images  
- More points = better results, but slower

### Stationary Tie Points
- Prevents false matches from static patterns (e.g., sky, dust, repeating terrain)

### Guided Matching
- Only works if GPS is available — not needed here.

### Adaptive Camera Model Fitting
- Lets Agisoft choose the best camera parameters automatically.

</details>

---

## ✅ Step-by-Step: Aligning Without GPS

1. 🔄 **Import your drone images** into Metashape  
2. ⚙️ Go to `Workflow → Align Photos`  
3. 🎯 Apply the recommended settings (see table above)  
4. 🧩 Wait for tie points to generate  
5. 🔍 Inspect the sparse cloud  
6. ✅ If all looks good → move on to build the **dense cloud**  
7. 🗺️ Then create a **DEM** and **orthomosaic**

---

## 🛠️ What If Alignment Fails?

Don’t panic. Try this:

- ⬆️ Increase `Key Point Limit` and `Tie Point Limit`
- ➕ Manually add tie points to connect problem areas
- 🔁 Check for missing overlap in your flight pattern

---
