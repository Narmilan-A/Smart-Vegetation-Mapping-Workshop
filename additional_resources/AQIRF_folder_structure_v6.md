# AQIRF – Folder & File Structure

Root folder for UAV RGB + Multispectral data across different sites (**Maleny**, **Petrie Creek**, **Buderim**). Structure separates **raw vs processed**, then **RGB vs MS**, then by **sensor type**. Additional root folder `annotation/` is included for labelling work.

---

## Root layout
```
AQIRF-Drone/
├─ docs/                     # Protocols, SOPs, site maps
├─ metadata/                 # Flight logs, GCPs, survey data (GTPs), master summary (Spread sheets)
├─ scripts/                  # Agisoft, ML/DL
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
   │  │  ├─ p1/              # DJI P1 M300
   │  │  └─ m3m/             # M3M RGB
   │  └─ ms/
   │     ├─ altum/           # Altum PT M300
   │     └─ m3m/             # M3M MS
   ├─ processed/
   │  ├─ rgb/
   │  │  ├─ agisoft/
   │  │  │  ├─ params_A/
   │  │  │  │  ├─ project_file/   # Photogrammetry project file (.psx, etc.)
   │  │  │  │  ├─ qc/             # QC reports
   │  │  │  │  ├─ products/       # Final mosaics, other (DEM, Mesh, VIs)
   │  │  │  │  └─ logs/           # Processing logs, PARAMS.json - Batch processing (XMl files)
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

## Annotation layout (species-based)
```
annotation/
├─ camphor_laurel/
│  ├─ maleny/
│  │  ├─ orthos/              # Copies of RGB + MS orthomosaics (common to all versions)
│  │  │  ├─ rgb/
│  │  │  └─ ms/
│  │  ├─ v1/
│  │  │  ├─ rois/             # ROI shapefiles (AOIs, training polygons)
│  │  │  ├─ working_shp/      # In-progress shapefiles (draft labelling)
│  │  │  ├─ labels/           # Finalised labels (geojson/shp/masks)
│  │  │  ├─ vi/               # Vegetation indices (NDVI, GNDVI, etc.)
│  │  │  ├─ clusters/         # Clustering outputs
│  │  │  └─ reports/          # Reports (docx, pptx, screenshots)
│  │  └─ v2/
│  │     └─ ...
│  ├─ petrie_creek/
│  │  ├─ orthos/
│  │  └─ v1/...
│  └─ buderim/
│     ├─ orthos/
│     └─ v1/...
├─ cats_claw_creeper/
│  └─ <site>/orthos + v1, v2...
└─ madeira_vine/
   └─ <site>/orthos + v1, v2...

```

---

## File naming conventions (core imagery)

| File type             | Format                              | Example                                        | Explanation                                                                 |
|-----------------------|-------------------------------------|------------------------------------------------|-----------------------------------------------------------------------------|
| Raw RGB (P1)          | `RGB-P1_<site>_<date>_IMG####.jpg`  | `RGB-P1_Maleny_20250614_IMG0001.jpg`           | RGB photo from DJI P1 sensor, site + date + image number                    |
| Raw RGB (M3M)         | `RGB-M3M_<site>_<date>_IMG####.jpg` | `RGB-M3M_Buderim_20250407_IMG0234.jpg`         | RGB photo from M3M oblique camera                                           |
| Raw MS (Altum)        | `MS-Altum_<site>_<date>_B#.tif`     | `MS-Altum_Petrie_20250705_B1.tif`              | Multispectral band file from Altum sensor, with band number                 |
| Raw MS (M3M)          | `MS-M3M_<site>_<date>_B#.tif`       | `MS-M3M_Buderim_20250407_B3.tif`               | Multispectral band file from M3M sensor, with band number                   |
| Project file          | `<site>_<date>_<tool>_paramsX.psx`  | `Maleny_20250614_agisoft_paramsA.psx`          | Photogrammetry project file, includes date, site, tool, and parameter set   |
| Ortho (RGB)           | `<site>_<date>_rgb_ortho_<res>m.tif`| `Maleny_20250614_rgb_ortho_0.05m.tif`          | Orthomosaic from RGB data, resolution included                              |
| Ortho (MS)            | `<site>_<date>_ms_ortho_<res>m.tif` | `Petrie_20250705_ms_ortho_0.10m.tif`           | Orthomosaic from multispectral data, resolution included                    |
| DEM                   | `<site>_<date>_dem.tif`             | `Buderim_20250407_dem.tif`                     | Digital Elevation Model generated from processing                           |
| Mesh (OBJ)            | `<site>_<date>_rgb_mesh_<level>.obj`| `Maleny_20250614_rgb_mesh_high.obj`            | 3D mesh model, with resolution level (low/medium/high)                      |
| QC report             | `qc_<stage>_<date>.txt`             | `qc_alignment_report_20250614.txt`             | QC report: alignment stats, reprojection error, band histograms             |
| Log file              | `<tool>_<stage>_<date>_<time>.log`  | `metashape_densecloud_20250614_1530.log`       | Log from photogrammetry software, includes step and timestamp               |
| Parameter record      | `PARAMS.json`                       | `PARAMS.json`                                  | JSON record of parameters used for this run                                 |

---

## File naming conventions (annotation, species-based)

| File type           | Format                                        | Example                                                   | Explanation                                               |
|---------------------|-----------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| RGB ortho copy      | `<species>_<site>_vX_rgb_ortho.tif`           | `camphorlaurel_maleny_v1_rgb_ortho.tif`                   | Copy of RGB orthomosaic for annotation (safe to edit)     |
| MS ortho copy       | `<species>_<site>_vX_ms_ortho.tif`            | `catsclawcreeper_petriecreek_v1_ms_ortho.tif`             | Copy of MS orthomosaic for annotation                     |
| ROI shapefile       | `<species>_<site>_vX_rois.shp`                | `madeiravine_buderim_v1_rois.shp`                         | Shapefile of ROIs (AOIs, training polygons)               |
| Working shapefile   | `<species>_<site>_vX_working.shp`             | `camphorlaurel_maleny_v1_working.shp`                     | In-progress shapefile for annotation                      |
| Final labels        | `<species>_<site>_vX_labels.shp`              | `catsclawcreeper_petriecreek_v1_labels.shp`               | Final labelled polygons                                   |
| Clusters/VIs            | `<species>_<site>_vX_<cluster_name>/<VI_name>.tif`            | `catsclawcreeper_petriecreek_v2_NDVI.tif`             | VIs/ Clustering outputs to guide labelling                     |
| Report document     | `<species>_<site>_vX_report.docx`             | `madeiravine_buderim_v1_report.docx`                      | Labelling report (Word)                                   |
| Report slides       | `<species>_<site>_vX_slides.pptx`             | `camphorlaurel_maleny_v1_slides.pptx`                     | Labelling presentation slides (PPTX)                      |
| Screenshot          | `<species>_<site>_vX_screenshot_##.png`       | `catsclawcreeper_petriecreek_v2_screenshot_01.png`        | Screenshots documenting annotation                        |

---

## Notes
- `raw/` = unprocessed UAV imagery separated into RGB vs MS, then by sensor.  
- `processed/` = outputs by tool + parameter set, with `project_file/`, `qc/`, `products/`, and `logs/` inside each param folder.  
- `annotation/` = species-based labelling sandbox with site + version control. Annotators copy orthos here and generate labels, ROIs, indices, and reports without altering master data.  
- **QC reports** = stats, plots, or checks proving alignment quality, reflectance scaling, or DEM/ortho quality.  
- `metadata/summaries/data_summary_weeds_scc16052025.xlsx` is the master summary.  
