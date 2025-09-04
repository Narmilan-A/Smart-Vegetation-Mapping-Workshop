## 📷 Drone Data and Height Examples

### Example 1: Drone Camera Height (from EXIF)
- Ellipsoid height from GPS = `55.0 m`
- Geoid height at location = `43.5 m`
- ➤ Orthometric height (approx. sea level) = `55.0 - 43.5 = 11.5 m`

### Example 2: GCP Collected with RTK GNSS
- Ellipsoid height = `11.674 m` (from WGS84)
- This is your absolute location with high accuracy
- You can correct the drone data using this point in software like **DJI Terra** or **Agisoft Metashape**

---

## 🛰️ Key Software That Uses Coordinate Systems

| Software        | Use Case                         | Coordinate Support |
|----------------|----------------------------------|--------------------|
| **DJI Terra**      | Drone data post-processing        | Supports WGS84, local, UTM, etc. |
| **Pix4D / Metashape** | Photogrammetry and GCP correction | Supports ellipsoid/MSL heights |
| **QGIS / ArcGIS** | GIS mapping and analysis          | Full coordinate system transformation |
| **RTK GPS Systems** | GCP and base station collection | Outputs WGS84 ellipsoid coordinates |

---

## 🧰 Best Practices for Drone-Based Data Collection

✅ Always check what height reference your drone is using (ellipsoid vs relative).  
✅ Make sure GCPs use the same coordinate system as your drone imagery.  
✅ Use a **known geodetic point** to correct your base station for cm-level accuracy.  
✅ Apply coordinate transformations if combining datasets with different systems.  
✅ Document your EPSG code (e.g., WGS84 = EPSG:4326) in your metadata.

---

## 📚 Glossary

- **WGS84**: Global standard ellipsoid used by GPS (EPSG:4326)
- **Geoid**: Surface representing global mean sea level (used for orthometric height)
- **GCP**: Ground Control Point, used to georeference drone imagery
- **RTK**: Real-Time Kinematic GPS correction system for high-precision location
- **EPSG Code**: Code identifying a specific coordinate system (e.g., EPSG:32659 for UTM Zone 59S)

---

