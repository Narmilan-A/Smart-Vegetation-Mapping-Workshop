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
   │  │  └─ geonadir/ Pix4D
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
   │     └─ terra/ Pix4D / geonadir
   │        ├─ params_A/
   │        │  ├─ project_file/
   │        │  ├─ qc/
   │        │  ├─ products/
   │        │  └─ logs/
```

---

## Annotation layout (species-based)
```
## Annotation Layout (Species-based)

annotation/
├─ camphor_laurel/
│  ├─ maleny/
│  │  ├─ orthos/               # Baseline imagery for annotation
│  │  │  ├─ rgb/               # RGB orthomosaics (copied from processed)
│  │  │  ├─ ms/                # MS orthomosaics (copied from processed)
│  │  │  └─ image_alignment/   # Modified orthos + GCP exports
│  │  │     ├─ aligned_rgb/    # Manually aligned RGB orthos
│  │  │     ├─ aligned_ms/     # Manually aligned MS orthos
│  │  │     └─ gcp/            # GCP exports from QGIS (.points, .csv, .txt)
│  │  ├─ v1/
│  │  │  ├─ rois/              # ROI shapefiles (AOIs, training polygons)
│  │  │  ├─ working_shp/       # In-progress shapefiles
│  │  │  ├─ labels/            # Final labels (geojson/shp/masks)
│  │  │  ├─ vi/                # Vegetation indices (NDVI, GNDVI, etc.)
│  │  │  ├─ clusters/          # Clustering outputs
│  │  │  └─ reports/           # Reports (docx, pptx, screenshots)
│  │  └─ v2/
│  │     └─ ...
│  ├─ petrie_creek/
│  │  ├─ orthos/
│  │  │  └─ image_alignment/
│  │  └─ v1/...
│  └─ buderim/
│     ├─ orthos/
│     │  └─ image_alignment/
│     └─ v1/...
├─ cats_claw_creeper/
│  └─ <site>/orthos + v1, v2...
└─ madeira_vine/
   └─ <site>/orthos + v1, v2...
```
---
## Metadata layout

Central, read-only store for site-specific metadata (flight logs, GCPs, ground-truth plots) and global master summaries.  
Dates use `YYYY-MM-DD`. Sites: `maleny`, `petrie_creek`, `buderim`.

```text
metadata/
├─ maleny/
│  ├─ flight_logs/                     # Drone/controller GNSS & telemetry
│  │  ├─ <YYYY-MM-DD>/                 # Per-flight
│  │  │  ├─ mrk/                       # DJI *.MRK (P1) or equivalent
│  │  │  ├─ ulog/                      # UAV flight logs (*.ULG)
│  │  │  ├─ controller/                # RC logs, screenshots
│  │  │  ├─ kml_gpx/                   # KML/GPX flight paths
│  │  │  └─ exports/                   # CSV summaries from logs
│  ├─ gcp/                             # Ground Control Points
│  │  ├─ <YYYY-MM-DD>/
│  │  │  ├─ raw_survey/                # Field sheets, raw rover/base files
│  │  │  ├─ processed/                  # Adjusted coords, CRS, QA
│  │  │  └─ exports/                   # CSV/GeoJSON for processing tools
│  └─ gtp/                             # Ground-Truth Plots
│     ├─ <YYYY-MM-DD>/
│     │  ├─ forms/                     # Field datasheets (species cover, notes)
│     │  ├─ gps_tracks/                # GPX/KML centroid/transects
│     │  ├─ photos/                    # Plot photographs
│     │  └─ processed/exports/         # Clean CSVs ready for analysis
│
├─ petrie_creek/
│  ├─ flight_logs/
│  ├─ gcp/
│  └─ gtp/
│
├─ buderim/
│  ├─ flight_logs/
│  ├─ gcp/
│  └─ gtp/
├─ calibration/
│  ├─ panels/                           # Reflectance panel definitions
│  │  └─ factory/                       # Factory CSVs
├─ permissions/                         # Permits, landholder letters
├─ summaries/                           # Global master spreadsheets
│  └─ data_summary_weeds_<date>.xlsx
└─ README.md
```
---

## Folder naming conventions (Raw imagery)

| Folder/File type      | Format                       | Example                                 | Explanation                                      |
|-----------------------|------------------------------|-----------------------------------------|--------------------------------------------------|
| Raw RGB (P1) folder   | `RGB-P1_<site>_<date>`       | `RGB-P1_Maleny_20250614`                | Folder of RGB photos from DJI P1 (site + date)   |
| Raw RGB (M3M) folder  | `RGB-M3M_<site>_<date>`      | `RGB-M3M_Buderim_20250407`              | Folder of RGB photos from M3M (oblique camera)   |
| Raw MS (Altum) folder | `MS-Altum_<site>_<date>`     | `MS-Altum_Petrie_20250705`              | Folder of multispectral images from Altum sensor |
| Raw MS (M3M) folder   | `MS-M3M_<site>_<date>`       | `MS-M3M_Buderim_20250407`               | Folder of multispectral images from M3M sensor   |

---

## Folder and file naming conventions (Processed imagery)

| File type             | Format                                | Example                                   | Explanation                                                                 |
|-----------------------|---------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------|
| Project folder/file   | `<site>_<date>_<tool>_paramsX.psx`    | `Maleny_20250614_agisoft_paramsA.psx`     | Photogrammetry project file, includes site, date, tool, and parameter set   |
| Ortho (RGB)           | `<site>_<date>_rgb_ortho_<res>m.tif`  | `Maleny_20250614_rgb_ortho_0.05m.tif`     | Orthomosaic from RGB data, resolution included                              |
| Ortho (MS)            | `<site>_<date>_ms_ortho_<res>m.tif`   | `Petrie_20250705_ms_ortho_0.10m.tif`      | Orthomosaic from multispectral data, resolution included                    |
| DEM                   | `<site>_<date>_dem.tif`               | `Buderim_20250407_dem.tif`                | Digital Elevation Model generated from processing                           |
| QC report             | `qc_<stage>_<date>.pdf`               | `qc_alignment_report_20250614.pdf`        | QC report: orthomosaic, alignment stats, reprojection error, band histograms|
| Parameter record      | `<site>_PARAMS.json/xml`              | `<site>_PARAMS.json/xml`                  | JSON or XML record of parameters used for this run                          |


---

## File naming conventions (annotation, species-based)

| File type        | Format                                          | Example                                          | Explanation                                           |
|------------------|-------------------------------------------------|--------------------------------------------------|-------------------------------------------------------|
| RGB ortho copy   | `<species>_<site>_rgb_ortho.tif`                | `camphor_maleny_rgb_ortho.tif`             | Copy of RGB orthomosaic for annotation (safe to edit) |
| MS ortho copy    | `<species>_<site>_ms_ortho.tif`                 | `catsclaw_petrie_ms_ortho.tif`       | Copy of MS orthomosaic for annotation                 |
| RGB ortho aligned| `<species>_<site>_rgb_ortho_modified.tif`            | `camphor_maleny_rgb_ortho_modified.tif`         | Manually realigned RGB orthomosaic for annotation     |
| MS ortho aligned | `<species>_<site>_ms_ortho_modified.tif`             | `catsclaw_petrie_ms_ortho_modified.tif`   | Manually realigned MS orthomosaic for annotation      |
| ROI shapefile    | `<species>_<site>_vX_rois.shp`                  | `madeira_buderim_v1_rois.shp`                | Shapefile of ROIs (AOIs, training polygons)           |
| Working shapefile| `<species>_<site>_vX_labelling.shp`             | `camphor_maleny_v1_labelling.shp`            | In-progress shapefile for annotation                |
| Final labels     | `<species>_<site>_vX_labels.geojson`            | `catsclaw_petrie_v1_labels.geojson`  | Final labelled polygons                               |
| Clusters / VIs   | `<species>_<site>_vX_<cluster/vi-name>.tif`     | `catsclaw_petrie_v2_NDVI.tif`        | Vegetation index or clustering output used in labelling|
| Report document  | `<species>_<site>_vX_report.docx`               | `madeira_buderim_v1_report.docx`             | Labelling , image alignment report in Word pdf format |
| GCP export (text) | `<species>_<site>_rgb_gcp_points.txt`  | `camphor_maleny_rgb_gcp_points.txt`             | GCP export in `.txt` format from QGIS (RGB alignment) |
| GCP export (CSV)  | `<species>_<site>_ms_gcp_points.csv`   | `catsclaw_petrie_ms_gcp_points.csv`       | GCP export in `.csv` format from QGIS (MS alignment) |
| GCP export (QGIS) | `<species>_<site>_rgb_gcp_points.points` | `madeira_buderim_rgb_gcp_points.points`          | Native `.points` file from QGIS georeferencing |
| Report slides    | `<species>_<site>_vX_slides.pptx`               | `camphor_maleny_v1_slides.pptx`            | Labelling presentation slides (PPTX)                  |
| Screenshot       | `<species>_<site>_vX_screenshot_##.png`         | `catsclaw_petrie_v2_screenshot_01.png`| Screenshots documenting annotation progress          |

---
## File naming conventions (Metadata)

| File type                  | Format                                           | Example                                                   | Explanation                                                      |
|-----------------------------|--------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------------|
| Flight log (MRK)            | `<site>_<date>_p1.mrk`                           | `maleny_20250614_p1.mrk`                                  | DJI P1 *.MRK file for photo geotags                              |
| Flight log (UAV raw)        | `<site>_<date>_flight.ulg`                       | `petriecreek_20250705_flight.ulg`                         | UAV onboard flight log                                           |
| Flight log (controller)     | `<site>_<date>_controller.log`                   | `buderim_20250407_controller.log`                         | Remote controller flight log                                     |
| Flight path (KML/GPX)       | `<site>_<date>_path.kml`                         | `maleny_20250614_path.kml`                                | Exported flight trajectory                                       |
| Flight log export (CSV)     | `<site>_<date>_flight_summary.csv`               | `petriecreek_20250705_flight_summary.csv`                 | Processed flight log summary in CSV                              |
| GCP raw survey              | `<site>_<date>_gcp_raw.csv`                      | `buderim_20250407_gcp_raw.csv`                            | Raw rover/base outputs                                           |
| GCP processed               | `<site>_<date>_gcp_processed.csv`                | `maleny_20250614_gcp_processed.csv`                       | Adjusted GCP coordinates (corrected CRS, QA checked)             |
| GCP export (GeoJSON)        | `<site>_<date>_gcp.geojson`                      | `petriecreek_20250705_gcp.geojson`                        | Final GCP file for GIS/photogrammetry                           |
| GTP datasheet (field form)  | `<site>_<date>_gtp_field.xlsx`                   | `maleny_20250614_gtp_field.xlsx`                          | Survey datasheet (species cover, notes)                         |
| GTP GPS track               | `<site>_<date>_gtp_track.gpx`                    | `petriecreek_20250705_gtp_track.gpx`                      | GPX/KML file marking centroid and transects                     |
| GTP photos                  | `<site>_<date>_gtp_photo_##.jpg`                 | `buderim_20250407_gtp_photo_01.jpg`                       | Photographs of ground-truth plot                                |
| GTP export (CSV)            | `<site>_<date>_gtp_summary.csv`                  | `maleny_20250614_gtp_summary.csv`                         | Cleaned CSV of ground-truth plot data ready for analysis         |
| Master register             | `master_register.csv`                            | `master_register.csv`                                     | Cross-site register of metadata and survey dates                 |
| Data Master summary (spreadsheet)| `data_summary_<project>_<date>.xlsx`               | `data_summary_AQIRF_16052025.xlsx`                     | Global Excel summary             |
| AI Master summary (spreadsheet)| `AI_summary_<project>_<date>.xlsx`               | `AI_summary_AQIRF_16052025.xlsx`                     | Global Excel summary             |

---
## Notes
- `raw/` = unprocessed UAV imagery separated into RGB vs MS, then by sensor.  
- `processed/` = outputs by tool + parameter set, with `project_file/`, `qc/`, `products/`, and `logs/` inside each param folder.  
- `annotation/` = species-based labelling sandbox with site + version control. Annotators copy orthos here and generate labels, ROIs, indices, and reports without altering master data.  
- `metadata/summaries/data_summary_weeds_scc16052025.xlsx` is the master summary.  
