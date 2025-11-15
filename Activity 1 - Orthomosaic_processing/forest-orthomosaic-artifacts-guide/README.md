# Forest UAV Orthomosaic Artifacts – Agisoft Metashape Workflow & Fixes

This repository documents **common artifacts in forest UAV projects** (Mavic 3M, DJI P1, Micasense Altum PT) and provides **practical, step‑by‑step workflows in Agisoft Metashape** to diagnose and fix them.

The material is based on:
- Real support case: *“Assistance needed: Mavic 3M radiometric calibration (panel selection), RGB seam blur, and vegetation ‘melting’ artifacts (M3M, P1, Altum PT)”*
- Agisoft official documentation
- Forest‑specific interpretation of DEM and orthomosaic behaviour

## 🎯 Scope

This repo focuses on forest and complex natural environments where orthomosaics commonly suffer from:

1. **Multispectral radiometric calibration issues**  
   - Mavic 3M panel handling  
   - Half dark / half bright orthomosaics

2. **RGB orthomosaic striping / blurred band along flight path**  
   - BRDF / low sun angle effects  
   - Color calibration strategies  
   - Local seamline fixes

3. **“Melting” / swirled canopy artifacts**  
   - Noisy DEM (DSM) in forest  
   - DEM editing vs orthomosaic patching

4. **DEM editing in forest environments**  
   - Why DEM ≈ DSM in forests  
   - How DEM drives orthomosaic quality  
   - Best practice for DEM editing

5. **Orthomosaic seamline editing (patching)**  
   - Assigning better images to artifacts  
   - Fill tools to handle missing data or unavoidable objects

---

## 📁 Repository Structure

```text
forest-orthomosaic-artifacts-guide/
├── README.md
└── docs/
    ├── dem_editing_forest.md
    ├── orthomosaic_seamline_editing.md
    ├── issue1_m3m_radiometric_calibration.md
    ├── issue2_rgb_brdf_strip_banding.md
    └── issue3_vegetation_melting_artifacts.md
```

You can add your own screenshots under a `figures/` folder and link them inside each `.md` file.

---

## 🚀 How to Use This Repository

1. **New team member?**  
   - Start with: `docs/dem_editing_forest.md`  
   - Then: `docs/orthomosaic_seamline_editing.md`

2. **Working on Mavic 3M multispectral data?**  
   - See: `docs/issue1_m3m_radiometric_calibration.md`

3. **Seeing blurred stripes along flight path in RGB orthos?**  
   - See: `docs/issue2_rgb_brdf_strip_banding.md`

4. **Vegetation looks “melted” or swirled in the orthomosaic?**  
   - See: `docs/issue3_vegetation_melting_artifacts.md`

5. **Editing workflow in Agisoft?**  
   - Use DEM editing + orthomosaic seamline editing together, as described in the docs.

---

## 🔗 Key Agisoft Documentation

- DEM editing tools (official):  
  https://agisoft.freshdesk.com/support/solutions/articles/31000164388-dem-editing-tools

- Orthomosaic seamline editing (patching):  
  https://agisoft.freshdesk.com/support/solutions/articles/31000165496-orthomosaic-seamline-editing-patching

You can reference these links directly from the Markdown files when published to GitHub.

