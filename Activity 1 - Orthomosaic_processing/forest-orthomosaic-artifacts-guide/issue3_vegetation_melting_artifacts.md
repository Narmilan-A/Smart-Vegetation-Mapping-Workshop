## Issue 3 – “Melting” / Swirled Canopy Artifacts

---

### 1. Symptom

- Tree crowns appear **melted**, swirled, or twisted in the orthomosaic.  
- Some canopy areas look like they are “flowing” or smeared.  
- Artifacts often correlate with high‑contrast canopy, steep geometry, or shadowed areas.

This issue appears consistently across different sensors → it is **not sensor‑specific**.

---

### 2. Root Cause – Noisy Surface / DEM

Agisoft support:

> The quality of orthomosaic depends on the quality of the alignment of the source data and the surface on which you use to build the orthomosaic. We can assume that the surface is noisy in these areas.

So:

- If the **DEM (DSM)** is noisy due to irregular canopy, shadows, or mis‑matches, the projection rays will intersect the surface incorrectly.  
- Trees may be projected partially onto wrong heights, causing **horizontal shifts** and 3D smear in the orthomosaic.

---

### 3. Recommended Fixes (from Agisoft + Best Practice)

Agisoft suggests two main strategies:

1. **Smooth the DEM in noisy areas** – DEM editing tools.  
2. **Edit the orthomosaic** – orthomosaic seamline editing (patching).

Best practice is to **start with DEM**, then refine with orthomosaic editing.

---

### 4. DEM Editing
Reference: [Agisoft DEM Editing Tools](https://agisoft.freshdesk.com/support/solutions/articles/31000164388-dem-editing-tools)  

Before editing DEM (**Check Alignment First**):

1. Review camera alignment (look for: misaligned groups, large reprojection errors).  
2. If necessary, optimise camera alignment or remove badly aligned images.  
3. Ensure no gross alignment error is the main cause.

#### **Step 4.1 — Switch to DEM View**
1. In Agisoft Metashape, open your project.  
2. In the Workspace pane → double-click **DEM**.  
3. The DEM view will show elevation as colours.

---

#### **Step 4.2 — Locate Melting Areas**
1. Compare **Orthomosaic** view and **DEM** view.  
2. Wherever the orthomosaic shows:
   - melted trees  
   - warped flowers  
   - blurry crowns  
3. Check that area in the DEM:
   - Often you will see bumps, holes, or noisy surfaces.

---

#### **Step 4.3 — Draw Small Polygons Around Noisy DEM Areas**
✔ Use **Draw Polygon** tool  
✔ Draw **small, local polygons** around each problem area  
❌ Do NOT select large blocks of forest  
❌ Never flatten entire canopy

Small, precise polygons = best results.

---

#### **Step 4.4 — Open “Fill DEM” Tool**
Right-click your polygon →  
**Edit DEM → Fill DEM**

You will see four filling methods.

---

#### **Step 4.5 — Choose the Correct Fill Method**

##### ⭐ **Recommended Default: Natural Neighbour**
Use when:
- Canopy is irregular  
- Area is complex (flowers, mixed leaves, shadows)  
- You want smooth + natural shape  

This is best for forest.

---

##### ✔ IDW (use for very small holes)
Good for tiny:
- Gaps  
- Holes  
- Missing points  

Power 2 is usually fine.

---

##### ❌ Avoid for Canopy:
- Constant  
- Best-fit plane  

These flatten canopy → make things worse.

---

#### **Step 4.6 — Apply the DEM Patch**
Click **OK**  
Polygon border will turn **dotted** (pending update)

---

#### **Step 4.7 — Update DEM**
You MUST commit the changes:

Toolbar → **Update DEM**  
(or Tools → DEM → Update DEM)

Now the DEM is physically corrected.

---

#### **Step 4.8 — Rebuild the Orthomosaic**
To apply the geometric corrections:

Right-click **Orthomosaic** →  
**Build Orthomosaic**

This step is required — DEM fixes do NOT show up automatically.

---

##### 🔍 **Expected Result After DEM Fix**
- Melted areas become stable  
- Branches and flowers align properly  
- No horizontal stretching  
- Texture becomes sharper and consistent  

---

### 🎨 5. Orthomosaic Editing (Texture Fix)
Reference: [Agisoft Orthomosaic Seamline Editing (Patching)](https://agisoft.freshdesk.com/support/solutions/articles/31000148853-orthomosaic-seamline-editing-patching-)  

After DEM correction, some problems may still remain.  
These are caused by:
- Poor seamline choice  
- One image having blur  
- Shadows in one flight line  
- Bad exposure in one image

This is where **orthomosaic patching** is used.

---

#### **Step 5.1 — Open Ortho View**
Double-click **Orthomosaic**.

---

#### **Step 5.2 — Locate Remaining Issues**
Look for:
- small blurred patches  
- seamline cuts across flowers  
- colour jumps  
- ghosted canopy edges  

---

#### **Step 5.3 — Draw Patch Polygon**
Use **Draw Polygon** around the problem region.

---

#### **Step 5.4 — Assign Best Image**
Right-click polygon →  
**Edit Orthomosaic → Assign Images**

Choose an image that:
- Has least shadow  
- Has clear flower texture  
- Has minimal motion blur  
- Has correct sun angle

Click **OK**.

---

#### **Step 5.5 — Use Fill ONLY if no good image exists**
Right-click polygon →  
**Edit Orthomosaic → Fill**

Use this when:
- All images contain unwanted objects  
- All images are blurred  
- There is a hole with no data  

---

#### **Step 5.6 — Apply Changes**
Toolbar → **Update Orthomosaic**

The blue mesh area will become updated.

---

#### 🔍 **Expected Result After Texture Fix**
- Flowers appear correctly placed  
- No twisting or smear  
- Seamlines replaced with better texture  
- Clean, stable canopy appearance

---

