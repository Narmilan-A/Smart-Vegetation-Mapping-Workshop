
# Estimation of Vegetation Indices (VIs)

## Purpose
VIs quantify plant health and stress by combining spectral bands from multispectral imagery. These indices support manual annotation by highlighting vegetation vigor, stress, or bare ground.

---
## Common VIs

| Index Name | Formula | Description |
|------------|---------|-------------|
| **MSAVI** (Modified Soil-Adjusted Vegetation Index) | (2 × NIR + 1 - sqrt((2 × NIR + 1)² - 8 × (NIR - Red))) / 2 | Reduces soil brightness effect, improves vegetation detection in sparse areas |
| **GNDVI** (Green NDVI) | (NIR - Green) / (NIR + Green) | More sensitive to chlorophyll concentration and canopy structure |
| **TVI** (Transformed Vegetation Index) | sqrt(((NIR - Red) / (NIR + Red)) + 0.5) | Transformation of NDVI; helps highlight vegetation presence |
| **DVI** (Difference Vegetation Index) | NIR - Red | Simple difference between NIR and Red; useful for raw vegetation signal |
| **LCI** (Leaf Chlorophyll Index / Chlorophyll Index Red Edge) | (NIR / RedEdge) - 1 | Estimates chlorophyll content using NIR and Red Edge bands |

---
### Estimating VIs in QGIS

1. Load your multispectral image into QGIS.
2. Open **Raster > Raster Calculator**.
3. Copy and paste the desired formula from above.
4. Save the output raster.
5. Apply a color ramp (e.g., green, spectral, RdYlGn) to interpret vegetation health.

#### QGIS Raster Calculator – Copy/Paste Ready

**Layer & band mapping:**  
`ASPA131_2018_MS_ROI_for_Demo@1 = Blue`  
`ASPA131_2018_MS_ROI_for_Demo@2 = Green`  
`ASPA131_2018_MS_ROI_for_Demo@3 = Red`  
`ASPA131_2018_MS_ROI_for_Demo@4 = RedEdge`  
`ASPA131_2018_MS_ROI_for_Demo@5 = NIR`  

##### MSAVI
```qgis
( 2*"ASPA131_2018_MS_ROI_for_Demo@5" + 1 
  - sqrt( (2*"ASPA131_2018_MS_ROI_for_Demo@5" + 1)^2 
          - 8*("ASPA131_2018_MS_ROI_for_Demo@5" - "ASPA131_2018_MS_ROI_for_Demo@3") ) 
) / 2
```

##### GNDVI
```qgis
("ASPA131_2018_MS_ROI_for_Demo@5" - "ASPA131_2018_MS_ROI_for_Demo@2") 
/ 
("ASPA131_2018_MS_ROI_for_Demo@5" + "ASPA131_2018_MS_ROI_for_Demo@2")
```

##### TVI (Transformed Vegetation Index)
```qgis
sqrt(
  ( "ASPA131_2018_MS_ROI_for_Demo@5" - "ASPA131_2018_MS_ROI_for_Demo@3" )
  /
  ( "ASPA131_2018_MS_ROI_for_Demo@5" + "ASPA131_2018_MS_ROI_for_Demo@3" )
  + 0.5
)
```

##### DVI (Difference Vegetation Index)
```qgis
"ASPA131_2018_MS_ROI_for_Demo@5" - "ASPA131_2018_MS_ROI_for_Demo@3"
```

##### LCI (Leaf Chlorophyll Index / Chlorophyll Index Red Edge)
```qgis
("ASPA131_2018_MS_ROI_for_Demo@5" / "ASPA131_2018_MS_ROI_for_Demo@4") - 1
```
---

### Estimating VIs in ArcGIS Pro

#### Option 1: Using Raster Calculator

1. Add your multispectral raster to the map.
2. Open **Analysis > Tools > Geoprocessing > Raster Calculator > Map Algebra expression**.
3. Enter the formula for your index, e.g.,  
   `("NIR_band" - "Red_band") / Float("NIR_band" + "Red_band")`
4. Run and save the output raster.
5. Visualise with color ramps.

#### Option 2: Using the Built-in 'Indices' Tool

1. Open the **Imagery** tab in ArcGIS Pro.
2. Click on **Indices** pane.
3. Choose the desired index function (e.g., NDVI).
5. Select the input raster bands from your image.
6. The tool will generate the index raster instantly without manual formula entry.

---

## How VIs Assist Annotation

- Highlight vegetation vigor and stress to aid accurate labelling.
- Reveal subtle differences not obvious in RGB imagery.
- Support consistency and objectivity in manual annotation decisions.

---

📌 **Tips:**
- Verify band assignments before calculation (e.g., confirm which band is NIR).
- Use indices alongside RGB images, not as a standalone classification.
- Check raster metadata.

---

## Further Reading

- [ArcGIS Pro Raster Calculator](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/raster-calculator.htm)  
- [ArcGIS Pro Indices gallery](https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/indices-gallery.htm)  
- [QGIS Raster Calculator](https://docs.qgis.org/3.40/en/docs/user_manual/working_with_raster/raster_analysis.html)

---
<div style="text-align: right;">
  <a href="Activity_05_Annotation_Guidelines.md" style="background-color:#4CAF50; color:white; padding:6px 12px; text-decoration:none; border-radius:4px;">
    Next ➡
  </a>
</div>
