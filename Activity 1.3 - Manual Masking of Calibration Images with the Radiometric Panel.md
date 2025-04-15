# Manual Masking of Calibration Images with the Radiometric Panel

In some cases, panels may not be automatically detected (e.g., unsupported or non-MicaSense panels). When this occurs:

### 1. Create a Camera Group for Calibration Images
If the `Calibration images` folder is not automatically created:

1. In the **Workspace** pane, select the images that contain the calibration panel.
2. Right-click on the selected images and choose:  
   `Move Cameras > New Camera Group`
3. Right-click on the newly created folder and rename it to:  
   `Calibration images`
4. Move all relevant calibration images into this folder.
5. **Disable** the calibration cameras by right-clicking and selecting **Disable Cameras**.

### 2. Apply Manual Masks
For each image in the `Calibration images` group:

- Manually **mask everything except the calibration plate**.
- Ensure only the **panel area** is unmasked.
- Masks must be created **for each calibration image and for each spectral band**.

To switch between bands:

- Use the **Photos pane** panel displayed to the right when an image is opened.

### 3. Continue with Reflectance Calibration
After masking:

- Proceed to **Step 3** of the reflectance calibration process.
- Input the reflectance values for each band of the calibration panel.

📘 Refer to the official guide for more details:  
[Agisoft Reflectance Calibration Tutorial – Appendix A](https://agisoft.freshdesk.com/support/solutions/articles/31000148381#Appendix-A.-Manual-masking-of-the-calibration-images-with-the-radiometric-panel)

---

## Appendix B. Reflectance Panel Database

Metashape stores previously used reflectance panel information and can auto-fill values when the same panel is detected.

### Accessing and Editing the Reflectance Panel Database

To access the panel database:

- Open the **Calibrate Reflectance** dialog.
- Click the **Select panel** button.

Within the **Select Reflectance Panel** dialog, you can:

- Load reflectance information from a `.csv` file.
- Save the current reflectance table (wavelength / reflectance factor).
- Edit the panel name (used in Calibrate Reflectance dialog).
- Remove existing panel information from the database.

📘 Official documentation:  
[Agisoft Reflectance Calibration Tutorial – Appendix B](https://agisoft.freshdesk.com/support/solutions/articles/31000148381#Appendix-B.-Reflectance-panel-database)

---

## Appendix C. Controlling Reflectance Calculation

Reflectance calculation can be enabled/disabled per sensor in the **Camera Calibration** dialog.

### Ensuring Calibration Is Used in Orthomosaic Generation

To apply calibration in the final orthomosaic:

1. Open **Camera Calibration**.
2. Check the option:  
   `Normalize band sensitivity`
   
If this option is **unchecked**, the orthomosaic will use **default color values**, ignoring reflectance panel calibration and metadata (including sun sensor info).

### Note on Thermal (LWIR) Bands

- Thermal (LWIR) bands are **not** included in the reflectance calibration process.
- Keep the `Normalize band sensitivity` option **unchecked** for LWIR bands.

📘 Additional reference:  
[Agisoft Reflectance Calibration Tutorial – Appendix C](https://agisoft.freshdesk.com/support/solutions/articles/31000148381#Appendix-C.-Controlling-reflectance-calculation)

---

> For a complete guide, visit the [Agisoft Reflectance Calibration Tutorial](https://agisoft.freshdesk.com/support/solutions/articles/31000148381)
