# Image Labelling Using ArcGIS Pro

In the image labelling workflow, we applied a systematic approach to label target features in a high-resolution RGB orthomosaic. Two commonly used labelling methods are demonstrated here, aiming to distinguish between two general classes: the object of interest (e.g., a particular vegetation type or man-made feature) and the background (including all other elements). Label accuracy was ensured through a combination of ground truth information and expert input.

## Method: ArcGIS Pro Image Analyst Extension

The first method utilises the advanced capabilities of ArcGIS Pro (v3.1 or higher), specifically the **Image Analyst** extension. This extension allows for a streamlined, semi-automated image labelling process via tools such as the **Training Samples Manager**, which is optimised for supervised classification workflows.

- This method is efficient and significantly reduces labelling time.
- Requires the **Image Analyst** license (sold separately).
- Ideal for users with access to licensed advanced GIS tools.

####[Figure 1: Screenshot of Licensing details and Training Samples Manager](![image](https://github.com/user-attachments/assets/a52ce1d2-57f8-40c1-af19-5018d7aeba29)

## Method: ArcGIS Pro Feature Class Tool

The second approach uses the **Create Feature Class** tool available in ArcGIS Pro. This method is more manual but does not require any additional licensing beyond a standard ArcGIS Pro installation.

- Suitable for those without access to the Image Analyst extension.
- Requires more time for manual labelling and polygon digitisation.
- Produces labelled vector files (e.g., shapefiles or feature classes) suitable for downstream machine learning model development or analysis.

### Steps (Part 1)

1. Open ArcGIS Pro and start a new project.
2. Load the high-resolution orthomosaic image into the map window.
3. Navigate to the **Catalog** panel > Right-click on your geodatabase > Choose **New > Feature Class**.
4. Define the new feature class name and geometry type (e.g., polygon).
5. Add a field to store label categories (e.g., “Class”: Object / Background).

####[Figure 2: Processing steps for labelling using feature class tool (Part-1)](![image](https://github.com/user-attachments/assets/7abdf953-2c1c-4b25-b7e5-bbbf12cfc41f)

### Steps (Part 2)

6. Use the **Edit** tab > **Create Features** to begin digitising labelled regions.
7. Assign appropriate label values to each polygon using the attribute table.
8. Once labelling is complete, export the labelled features as a shapefile or maintain it as a geodatabase feature class.

####[Figure 3: Processing steps for labelling using feature class tool (Part-2)](![image](https://github.com/user-attachments/assets/05114264-c6d8-471f-b929-4bdc40f19fc9)

## Summary

Both methods provide viable approaches to image labelling within ArcGIS Pro, depending on the tools and licensing available:

- **Image Analyst Extension**: Efficient, advanced functionality; ideal for users with access to licensed tools.
- **Feature Class Tool**: Manual but accessible; suitable for broader use cases with no additional licensing cost.

These labelled datasets can then be exported and used in machine learning workflows, classification models, or other GIS-based analyses.

