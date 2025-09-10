# AQIRF – Folder & File Structure

Root folder for UAV RGB + Multispectral data across three sites (**Maleny**, **Petrie Creek**, **Buderim**). Structure separates **raw vs processed**, then **RGB vs MS**, then by **sensor type**. Additional root folder `annotation/` is included for labelling work.

---

## Root layout
```
AQIRF-Drone/
├─ docs/                     # Protocols, SOPs, site maps
├─ metadata/                 # Flight logs, GCPs, survey data, master summary
├─ scripts/                  # Agisoft, Terra, Geonadir, utilities
├─ templates/                # Naming templates, metadata forms, checklists
├─ sites/                    # Site-specific data (raw + processed)
└─ annotation/               # Labelling outputs
```

---

## Site layout
Each site folder has subfolders per survey date (`YYYY-MM-DD`):

```
sites/<site>/
└─ <YYYY-MM-DD>/
   ├─ raw/
   │  ├─ rgb/
   │  │  ├─ p1/              # DJI P1 M300 (RGB nadir)
   │  │  └─ m3m/             # M3M RGB (oblique)
   │  └─ ms/
   │     ├─ altum/           # Altum PT M300
   │     └─ m3m/             # M3M MS (oblique)
   ├─ processed/
   │  ├─ rgb/
   │  │  ├─ agisoft/
   │  │  │  ├─ params_A/
   │  │  │  │  ├─ project_file/   # Photogrammetry project file (.psx, etc.)
   │  │  │  │  ├─ qc/             # QC reports, thumbnails
   │  │  │  │  ├─ products/       # Final mosaics, masks
   │  │  │  │  └─ logs/           # Processing logs, PARAMS.json
   │  │  │  ├─ params_B/
   │  │  │  │  ├─ project_file/
   │  │  │  │  ├─ qc/
   │  │  │  │  ├─ products/
   │  │  │  │  └─ logs/
   │  │  │  └─ params_C/
   │  │  │     ├─ project_file/
   │  │  │     ├─ qc/
   │  │  │     ├─ products/
   │  │  │     └─ logs/
   │  │  ├─ terra/
   │  │  │  ├─ params_A/
   │  │  │  │  ├─ project_file/
   │  │  │  │  ├─ qc/
   │  │  │  │  ├─ products/
   │  │  │  │  └─ logs/
   │  │  └─ geonadir/
   │  │     ├─ params_A/
   │  │     │  ├─ project_file/
   │  │     │  ├─ qc/
   │  │     │  ├─ products/
   │  │     │  └─ logs/
   │  └─ ms/
   │     ├─ agisoft/
   │     │  ├─ params_A/
   │     │  │  ├─ project_file/
   │     │  │  ├─ qc/
   │     │  │  ├─ products/
   │     │  │  └─ logs/
   │     │  └─ params_B/
   │     │     ├─ project_file/
   │     │     ├─ qc/
   │     │     ├─ products/
   │     │     └─ logs/
   │     └─ terra/
   │        ├─ params_A/
   │        │  ├─ project_file/
   │        │  ├─ qc/
   │        │  ├─ products/
   │        │  └─ logs/
```

---

## Annotation layout
```
annotation/
├─ <site>/
│  └─ <YYYY-MM-DD>/
│     ├─ rgb/
│     │  ├─ labels/          # Vector (shp/geojson) or raster masks (tif)
│     │  └─ qc/              # Annotation QC (who labelled, % checked)
│     └─ ms/
│        ├─ labels/
│        └─ qc/
```

---

## File naming conventions (core imagery)

| File type             | Format                              | Example                                        | Explanation                                                                 |
|-----------------------|-------------------------------------|------------------------------------------------|-----------------------------------------------------------------------------|
| Raw RGB (P1)          | `RGB-P1_<site>_<date>_IMG####.jpg`  | `RGB-P1_Maleny_20250614_IMG0001.jpg`           | RGB photo from DJI P1 sensor, site + date + image number                    |
| Raw RGB (M3M)         | `RGB-M3M_<site>_<date>_IMG####.jpg` | `RGB-M3M_Buderim_20250407_IMG0234.jpg`         | RGB photo from M3M oblique camera                                           |
| Raw MS (Altum)        | `MS-Altum_<site>_<date>_B#.tif`     | `MS-Altum_Petrie_20250705_B1.tif`              | Multispectral band file from Altum sensor, with band number                 |
| Raw MS (M3M)          | `MS-M3M_<site>_<date>_B#.tif`       | `MS-M3M_Buderim_20250407_B3.tif`               | Multispectral band file from M3M sensor, with band number                   |
| Project file          | `<date>_<site>_<tool>_paramsX.psx`  | `20250614_Maleny_agisoft_paramsA.psx`          | Photogrammetry project file, includes date, site, tool, and parameter set   |
| Ortho (RGB)           | `<site>_<date>_rgb_ortho_<res>m.tif`| `Maleny_20250614_rgb_ortho_0.05m.tif`          | Orthomosaic from RGB data, resolution included                              |
| Ortho (MS)            | `<site>_<date>_ms_ortho_<res>m.tif` | `Petrie_20250705_ms_ortho_0.10m.tif`           | Orthomosaic from multispectral data, resolution included                    |
| DEM                   | `<site>_<date>_dem.tif`             | `Buderim_20250407_dem.tif`                     | Digital Elevation Model generated from processing                           |
| Mesh (OBJ)            | `<site>_<date>_rgb_mesh_<level>.obj`| `Maleny_20250614_rgb_mesh_high.obj`            | 3D mesh model, with resolution level (low/medium/high)                      |
| QC report             | `qc_<stage>_<date>.txt`             | `qc_alignment_report_20250614.txt`             | QC report: alignment stats, reprojection error, band histograms             |
| Log file              | `<tool>_<stage>_<date>_<time>.log`  | `metashape_densecloud_20250614_1530.log`       | Log from photogrammetry software, includes step and timestamp               |
| Parameter record      | `PARAMS.json`                       | `PARAMS.json`                                  | JSON record of parameters used for this run                                 |

---

## File naming conventions (annotation)

| File type         | Format                                       | Example                                         | Explanation                                                   |
|-------------------|----------------------------------------------|-------------------------------------------------|---------------------------------------------------------------|
| Vector labels     | `<site>_<date>_<sensor>_labels.geojson`      | `Maleny_20250614_rgb_labels.geojson`            | Polygon/GeoJSON annotations for one site/date/sensor          |
| Raster mask       | `<site>_<date>_<sensor>_mask_multiclass.tif` | `Petrie_20250705_ms_mask_multiclass.tif`        | Multiclass raster mask aligned with imagery                   |
| QC log            | `annotation_qc_<site>_<date>.csv`            | `annotation_qc_Buderim_20250407.csv`            | Who labelled, % checked, reviewer notes                       |
| Training split    | `<site>_<date>_<sensor>_train_test_split.csv`| `Maleny_20250614_rgb_train_test_split.csv`      | Records which labels/masks went to train/val/test sets        |

---

## Notes
- `raw/` = unprocessed UAV imagery separated into RGB vs MS, then by sensor.  
- `processed/` = outputs by tool + parameter set, with `project_file/`, `qc/`, `products/`, and `logs/` inside each param folder.  
- **QC reports** = stats, plots, or checks proving alignment quality, reflectance scaling, or DEM/ortho quality.  
- **Annotation** is stored in its own root for AI training, with labels and QC logs.  
- `metadata/summaries/data_summary_weeds_scc16052025.xlsx` is the master summary.  
