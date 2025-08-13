# Annotation Guidelines

## Learning Objectives
- Understand the standardised annotation protocol.
- Apply consistent polygon labelling for vegetation types.
- Avoid common mistakes in annotation.

---

## Annotation Attributes Summary (Example Only)

| Class ID | Class Name         | Confidence Level (%) | Remarks                          |
|----------|--------------------|---------------------|---------------------------------|
| 1        | Healthy Moss       | 25, 50, 75, 100     | Use to indicate health status   |
| 2        | Stressed Moss      | 25, 50, 75, 100     | Shows signs of stress            |
| 3        | Moribund Moss      | 25, 50, 75, 100     | Near death or dying moss         |
| 4        | Lichen A           | 25, 50, 75, 100     | One species of lichen            |
| 5        | Lichen B           | 25, 50, 75, 100     | Another lichen species           |
| 6        | Non vegetated area | 100                 | Confirmed bare ground or rocks   |

### Annotation Attribute: Confidence Level

Each annotated polygon should include an attribute called **Confidence_Level** indicating the annotator's confidence in the classification:

| Confidence Level | Description          |
|------------------|----------------------|
| 25%              | Low confidence       |
| 50%              | Moderate confidence  |
| 75%              | High confidence      |
| 100%             | Full confidence      |

---
### General Rules:
- We prefer most polygons to be labelled with **100% confidence**.  
- If your confidence is very low, please **do not label** the polygon.  
- Avoid labelling polygons that include **mixed pixels at the border**.  
- Ignore 1–2 pixels from the polygon edges and label only the middle area to avoid mixed pixel effects.
- Annotate **only clearly visible areas**.
- Avoid overlaps polygons.
---

## Step-by-Step
1. Open the drone orthomosaic.
2. Create a new vector layer for annotations.
3. Select the correct class before drawing each polygon.
4. Save your layer frequently.

---

📌 **Remember:** Follow the class definitions exactly for data consistency.

---
<div style="text-align: right;">
  <a href="Activity_06_Ground_Truth_Data_and_Region_of_Interest.md" style="background-color:#4CAF50; color:white; padding:6px 12px; text-decoration:none; border-radius:4px;">
    Next ➡
  </a>
</div>
