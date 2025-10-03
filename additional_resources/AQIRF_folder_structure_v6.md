# AQIRF – Folder & File Structure and Naming

## Root layout
```
weeds_scc/
├─ docs/          # Protocols, SOPs, site maps
├─ metadata/                 # Flight logs, GCPs, survey data (GTPs), master summary (Spread sheets)
├─ scripts/                  # Agisoft, ML/DL
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
│  │  │     ├─ aligned_ms/     # Manually aligned MS orthos - using P1 or M3M-RGB
│  │  │     ├─ reports/        # alignment report.pdf
│  │  │     └─ gcps            # GCP exports from QGIS (.points, .csv, .txt)
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

| Folder type           | Format                       | Example                                 | Explanation                                      |
|-----------------------|------------------------------|-----------------------------------------|--------------------------------------------------|
| Raw RGB (P1) folder   | `p1_rgb_<site>_<date>`       | `p1_rgb_maleny_20250614`                | Folder of RGB photos from DJI P1 (site + date)   |
| Raw RGB (M3M) folder  | `m3m_rgb_<site>_<date>`      | `m3m_rgb_buderim_20250407`              | Folder of RGB photos from M3M (oblique camera)   |
| Raw MS (Altum) folder | `altum_ms_<site>_<date>`     | `altum_ms_petrie_20250705`              | Folder of multispectral images from Altum sensor |
| Raw MS (M3M) folder   | `m3m_ms_<site>_<date>`       | `m3m_ms_buderim_20250407`               | Folder of multispectral images from M3M sensor   |

---

## Folder and file naming conventions (Processed imagery)

| File type             | Format                                | Example                                   | Explanation                                                                 |
|-----------------------|---------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------|
| Project folder/file   | `<site>_<date>_<sensor>_<tool>_paramsX.psx`    | `maleny_20250614_p1_agisoft_paramsA.psx`     | Photogrammetry project file, includes site, date, tool, and parameter set   |
| Ortho (RGB)           | `<site>_<date>_<sensor>_rgb_ortho_<res>m.tif`  | `maleny_20250614_p1_rgb_ortho_0.05m.tif`     | Orthomosaic from RGB data, resolution included                              |
| Ortho (MS)            | `<site>_<date>_<sensor>_ms_ortho_<res>m.tif`   | `petrie_20250705_altum_ms_ortho_0.20m.tif`      | Orthomosaic from multispectral data, resolution included                    |
| DEM                   | `<site>_<date>_dem.tif`               | `buderim_20250407_dem.tif`                | Digital Elevation Model generated from processing                           |
| QC report             | `qc_<stage>_<date>.pdf`               | `qc_alignment_report_20250614.pdf`        | QC report: orthomosaic, alignment stats, reprojection error, band histograms|
| Parameter record      | `<site>_PARAMS.json/xml`              | `buderim_PARAMS.json/xml`                  | JSON or XML record of parameters used for this run                          |


---

## File naming conventions (annotation, species-based)

| File type        | Format                                          | Example                                          | Explanation                                           |
|------------------|-------------------------------------------------|--------------------------------------------------|-------------------------------------------------------|
| MS ortho aligned | `<species>_<site>_<sensor>_ms_ortho_modified.tif`        | `petrie_20250614_altum_ms_ortho_modified.tif`  | Manually realigned MS orthomosaic for annotation      |
| ROI shapefile    | `<species>_<site>_vX_rois.shp`                  | `madeira_buderim_v1_rois.shp`                | Shapefile of ROIs (AOIs, training polygons)           |
| Working shapefile| `<species>_<site>_vX_labelling.shp`             | `camphor_maleny_v1_labelling.shp`            | In-progress shapefile for annotation                |
| Final labels     | `<species>_<site>_vX_labels.geojson`            | `catsclaw_petrie_v1_labels.shp`  | Final labelled polygons                               |
| Clusters / VIs   | `<species>_<site>_vX_<cluster/vi-name>.tif`     | `catsclaw_petrie_v2_NDVI.tif`        | Vegetation index or clustering output used in labelling|
| Report document  | `<species>_<site>_vX_report.docx`               | `madeira_buderim_v1_report.docx`             | Labelling , image alignment report in Word pdf format |
| GCP export (text) | `<site>_rgb_gcp_points.txt`  | `maleny_rgb_gcp_points.txt`             | GCP export in `.txt` format from QGIS (RGB alignment) |
| GCP export (CSV)  | `<site>_ms_gcp_points.csv`   | `petrie_ms_gcp_points.csv`       | GCP export in `.csv` format from QGIS (MS alignment) |
| GCP export (QGIS) | `<site>_rgb_gcp_points.points` | `buderim_rgb_gcp_points.points`          | Native `.points` file from QGIS georeferencing |
| Report slides    | `<species>_<site>_vX_slides.pptx`               | `camphor_maleny_v1_slides.pptx`            | Labelling presentation slides (PPTX)                  |
| Screenshot       | `<species>_<site>_vX_screenshot_##.png`         | `catsclaw_petrie_v2_screenshot_01.png`| Screenshots documenting annotation progress          |

---
## File naming conventions (Metadata)

| File type                    | Format                                           | Example                                                   | Explanation                                                      |
|-------------------------------|--------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------------------|
| Flight log (MRK)              | `<site>_<date>_p1.mrk`                           | `maleny_20250614_p1.mrk`                                  | DJI P1 *.MRK file for photo geotags                              |
| Flight log (UAV raw)          | `<site>_<date>_flight.ulg`                       | `petriecreek_20250705_flight.ulg`                         | UAV onboard flight log                                           |
| Flight path (KML/GPX)         | `<site>_<date>_path.kml`                         | `maleny_20250614_path.kml`                                | Exported flight trajectory                                       |
| Flight log export (CSV)       | `<site>_<date>_flight_summary.csv`               | `petriecreek_20250705_flight_summary.csv`                 | Processed flight log summary in CSV                              |
| GCP raw survey                | `<site>_<date>_gcp_raw.csv`                      | `buderim_20250407_gcp_raw.csv`                            | Raw rover/base outputs                                           |
| GCP processed                 | `<site>_<date>_gcp_processed.csv`                | `maleny_20250614_gcp_processed.csv`                       | Adjusted GCP coordinates (corrected CRS, QA checked)             |
| GCP export (GeoJSON)          | `<site>_<date>_gcp.geojson`                      | `petriecreek_20250705_gcp.geojson`                        | Final GCP file for GIS/photogrammetry                           |
| GCP export (SHP)              | `<site>_<date>_gcp.shp`                          | `maleny_20250614_gcp.shp`                                 | GCP shapefile export for QGIS/ArcGIS                            |
| GCP export (GPKG)             | `<site>_<date>_gcp.gpkg`                         | `buderim_20250407_gcp.gpkg`                               | GCP geopackage for GIS workflows                                |
| GCP export (GDB)              | `<site>_<date>_gcp.gdb`                          | `petriecreek_20250705_gcp.gdb`                            | GCP file geodatabase (ArcGIS)                                   |
| GTP datasheet (field form)    | `<site>_<date>_gtp_field.xlsx`                   | `maleny_20250614_gtp_field.xlsx`                          | Survey datasheet (species cover, notes)                         |
| GTP GPS track                 | `<site>_<date>_gtp_track.gpx`                    | `petriecreek_20250705_gtp_track.gpx`                      | GPX/KML file marking centroid and transects                     |
| GTP photos                    | `<site>_<date>_gtp_photo_##.jpg`                 | `buderim_20250407_gtp_photo_01.jpg`                       | Photographs of ground-truth plot                                |
| GTP export (CSV)              | `<site>_<date>_gtp_summary.csv`                  | `maleny_20250614_gtp_summary.csv`                         | Cleaned CSV of ground-truth plot data ready for analysis         |
| GTP export (SHP)              | `<site>_<date>_gtp.shp`                          | `petriecreek_20250705_gtp.shp`                            | Ground-truth plots in shapefile format                          |
| GTP export (GPKG)             | `<site>_<date>_gtp.gpkg`                         | `buderim_20250407_gtp.gpkg`                               | Ground-truth plots in geopackage format                         |
| GTP export (GDB)              | `<site>_<date>_gtp.gdb`                          | `maleny_20250614_gtp.gdb`                                 | Ground-truth plots in file geodatabase format                   |
| Data Master summary (spreadsheet)| `data_summary_<project>.xlsx`               | `data_summary_AQIRF.xlsx`                     | Global Excel summary             |
| AI Master summary (spreadsheet)| `ml_summary_<project>.xlsx`               | `ml_summary_AQIRF.xlsx`                     | Global Excel summary             |

---
