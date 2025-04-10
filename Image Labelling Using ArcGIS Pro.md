# Image Labelling Using ArcGIS Pro

## 2.5.2 Image Labelling

In the methodology of the image labelling process, we employed a rigorous approach to accurately label the target species within a high-resolution RGB orthomosaic. Two different approaches were utilised for labelling. For our specific task, we focused on identifying two distinct classes:

- **Target species**: Identified as *Broad-Leaved Pepper (BLP)* or *Pandanus*.
- **Background**: Other vegetation and non-vegetation features.

To ensure labelling accuracy, we combined ground truth information with expert support throughout the process.

---

## 2.5.2.1 Method 1: Use of ArcGIS Pro Image Analyst Extension

We used the advanced capabilities of **ArcGIS Pro 3.1** with the **Image Analyst** extension (available through a separate license). This extension enabled efficient and detailed image labelling through tools such as the **Training Samples Manager**.

- This method **required less time** for labelling.
- A **separate license** for the Image Analyst extension is needed.

> 📌 See *Appendix-D* for detailed processing steps.

### Figure 1: Licensing details and Training Samples Manager  
![image](https://github.com/user-attachments/assets/33c281f9-1928-49a7-8382-b649d730ccfc)


---

## 2.5.2.2 Method 2: Use of ArcGIS Pro Feature Class Tool

The second method used the **“Create Feature Class”** tool in ArcGIS Pro to label the target species manually.

- This approach **does not require an additional license**.
- However, it **requires more time** due to manual labelling and attribute population steps.

Figures below show the processing workflow for creating and exporting the labelled vector file, which is used in the model development pipeline.

### Figure 2: Processing steps for labelling using feature class tool (Part-1)  
![image](https://github.com/user-attachments/assets/7d7a9732-cbc5-4fe6-a723-ebfa8361640a)

### Figure 3: Processing steps for labelling using feature class tool (Part-2)  
![image](https://github.com/user-attachments/assets/0cf017e2-6533-4c3c-a360-867f8d241bda)

---

### Summary

| Method | Tool Used | License Required | Labelling Time | Notes |
|--------|-----------|------------------|----------------|-------|
| **1** | Image Analyst Extension | Yes | Less | Efficient, good for batch tasks |
| **2** | Create Feature Class | No | More | Manual but cost-effective |

Both methods contributed to the accurate creation of training datasets for the image classification and machine learning modelling tasks.
