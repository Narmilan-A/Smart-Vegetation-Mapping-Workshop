# 🧭 What is Reference Preselection in Agisoft Metashape?

**Reference Preselection** is a setting used during photo alignment in Agisoft Metashape.  
It helps the software decide **which image pairs** should be checked for overlap, based on available **metadata** like GPS coordinates or camera angles.

> 📌 TL;DR: It speeds up processing — **but only works well if you have good metadata**!

---

## ⚙️ Where to Find It

You’ll see it when you go to:  
**`Workflow → Align Photos` → Reference Preselection**

You’ll find 3 options:

- `Source`
- `Estimated`
- `Sequential`

Let’s break each one down 👇

---

## 🔹 1. Source

> Uses original GPS/camera metadata from your image files.

- Checks which photos are spatially close based on metadata (e.g., latitude, longitude, yaw).
- Skips unnecessary matches between distant or non-overlapping images.
- **Fastest** if metadata is accurate.

| Use it when... | Avoid it when... |
|----------------|------------------|
| ✅ You have reliable GPS or drone data | ❌ No GPS, or metadata is wrong/inaccurate |

---

## 🔹 2. Estimated

> Uses previously estimated camera positions from a **prior alignment** or import.

- Helpful in multi-stage workflows.
- Uses past data to predict matches.
- Useful in large or multi-session projects.

| Use it when... | Avoid it when... |
|----------------|------------------|
| ✅ You’ve already done a rough alignment | ❌ This is your first alignment step |

---

## 🔹 3. Sequential

> Matches images **based on file order** — assumes they were taken in a logical flight path.

- Designed for **linear or strip-based surveys** (e.g., road or corridor mapping).
- Can work **without GPS** if images are ordered properly.
- Fast and simple, but can miss overlaps in complex patterns.

| Use it when... | Avoid it when... |
|----------------|------------------|
| ✅ Your image sequence follows a clean path | ❌ Images are jumbled or multiple flight paths mixed |

---

<details>
<summary>💬 So... Which One Should I Use?</summary>

| You Have...               | Use This Mode         |
|---------------------------|------------------------|
| ✅ Accurate GPS in EXIF    | `Source`               |
| 🚫 No GPS or metadata     | `Disable preselection` |
| 🔁 Already aligned data   | `Estimated`            |
| 📷 Ordered flight images  | `Sequential` (optional) |

If you're **missing GPS data**, it's usually best to **disable Reference Preselection entirely**.  
Let Agisoft match everything visually — it's slower, but much more reliable in that case.

</details>

---

## 🧠 Final Tips

- **Check your metadata** before enabling Reference Preselection.
- If in doubt, **disable it** — alignment may take longer, but you'll avoid missed overlaps.
- Use `Sequential` if your image files are **neatly ordered and flown consistently**.

---
