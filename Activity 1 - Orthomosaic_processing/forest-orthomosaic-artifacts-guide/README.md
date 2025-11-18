## **Forest Orthomosaic Artifact Correction**  

### **DEM Editing Theory – Forest Environments**
#### Why Forest DEM == DSM (Not Ground DEM)
In forests:

- Drone sees **tree canopy**, not ground  
- Photogrammetry reconstructs **whatever surface is visible**  
- Dense cloud = canopy geometry  
- DEM = interpolated canopy DSM  

Thus:

```
DEM in forest = DSM canopy surface ≠ Bare-earth DEM
```

Forest DEMs contain:
- Height spikes  
- Voids under shadows  
- Parallax distortions  
- Mixed canopy heights  

> These errors **distort orthomosaic geometry** when pixels are projected onto this noisy surface.
---

### ** How Orthomosaic Projection Works**

For each pixel of every image:

1. A **ray** is generated from the **camera centre**  
2. The ray passes through that specific **image pixel**  
3. The ray intersects the **DEM surface**  
4. The X/Y location of the ray–DEM intersection becomes the pixel’s position in the orthomosaic  
5. Metashape selects the *best* image to texture that pixel  

If the DEM is incorrect → ray intersection is incorrect → pixel placed in wrong position → **blur, smear, ghosting**.

---

### ** What Exactly Is a Projection Ray?**

A projection ray is:

```
A straight 3D line going:
Camera centre → through a pixel → downward → until it hits the DEM surface
```

Where the ray hits determines:
- Pixel's true ground position  
- Pixel's alignment relative to neighbours  
- Mosaic accuracy  

Noise in DEM = wrong ray intersection = wrong pixel position.

---

### ** Why Vertical DEM Errors Cause Horizontal Blur**

- DEM height error → ray intersects at wrong place horizontally.
  - If DEM is too high:  Ray hits surface **sooner** → pixel shifts **backwards**
  - If DEM is too low:  Ray hits surface **later** → pixel shifts **forwards**

Thus:

```
Vertical error → Horizontal displacement → Melted canopy
```

This is why forest orthomosaics often show:
- Swirled branches  
- Double tree crowns  
- Sliding textures  
- Local blur patches  
---
