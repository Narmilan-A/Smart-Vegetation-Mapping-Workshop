# Drone Data Collection with RTK and PPK

This guide will help beginners understand how to collect accurate georeferenced data using drones, with a focus on **RTK** (Real-Time Kinematic) and **PPK** (Post-Processed Kinematic) technologies. RTK and PPK are essential for achieving high accuracy in drone surveys, particularly for photogrammetry and geospatial applications.

## Table of Contents
1. [Introduction](#introduction)
2. [What is RTK and PPK?](#what-is-rtk-and-ppk)
3. [How RTK/PPK Works](#how-rtkppk-works)
4. [Setting Up for RTK/PPK Data Collection](#setting-up-for-rtkppk-data-collection)
    1. [RTK Setup](#rtk-setup)
    2. [PPK Setup](#ppk-setup)
5. [Steps for RTK/PPK Data Collection](#steps-for-rtkppk-data-collection)
6. [Post-Processing with PPK](#post-processing-with-ppk)
7. [Troubleshooting Common Issues](#troubleshooting-common-issues)
8. [Conclusion](#conclusion)

---

## Introduction

In drone-based surveying, the accuracy of the georeferencing process is crucial for producing reliable maps and models. **RTK (Real-Time Kinematic)** and **PPK (Post-Processed Kinematic)** are two advanced GNSS technologies used to improve the **accuracy** of GPS data collected by drones. This guide will walk you through the essential steps and principles involved in setting up and processing RTK and PPK data for high-precision drone surveys.

---

## What is RTK and PPK?

- **RTK (Real-Time Kinematic)**: RTK allows the drone to receive real-time corrections from a base station, resulting in centimeter-level accuracy while the data is being collected. This method is highly effective in real-time applications.
  
- **PPK (Post-Processed Kinematic)**: PPK data collection happens during the drone flight, where the drone’s GPS logs and base station logs are recorded. After the flight, the GPS data is **post-processed** using software to apply corrections, yielding high-precision results once the processing is complete.

---

## How RTK/PPK Works

### RTK Workflow
1. **Base Station Setup**: The base station is placed at a known geodetic point. It transmits correction data to the drone’s GPS in real-time.
2. **Drone Data Collection**: The drone uses RTK to receive corrections from the base station and records high-accuracy GPS data during flight.
3. **Data Use**: The data collected in real-time is georeferenced with centimeter-level accuracy.

### PPK Workflow
1. **Base Station Setup**: Like RTK, the base station is set up at a known point.
2. **Drone Data Collection**: The drone logs its GPS position throughout the flight without real-time corrections.
3. **Post-Processing**: After the flight, GPS data collected by the drone is **processed** against the base station data using software to calculate the precise location of each point.
4. **Data Use**: The post-processed data is used for precise georeferencing of images.

---

## Setting Up for RTK/PPK Data Collection

### RTK Setup
1. **Base Station**: Set up a **base station** at a known geodetic location. This can be a survey marker, or a GPS reference point.
2. **RTK Receiver**: Mount the RTK receiver on your drone and connect it to the base station to receive real-time corrections.
3. **Software Setup**: Ensure the drone’s RTK software is set up to automatically receive and apply corrections during the flight.
4. **Flight Planning**: Use flight planning software to plan the drone flight, ensuring you capture overlapping imagery for photogrammetry.

### PPK Setup
1. **Base Station**: Place the base station at a known point and log its position using a **dGPS** or another high-accuracy GNSS receiver.
2. **Drone GPS Logger**: Set up the drone with a **PPK-capable GNSS receiver**. Ensure it records GPS logs during the flight.
3. **Flight Planning**: Similar to RTK, plan your drone flight for maximum coverage and overlap of imagery.

---

## Steps for RTK/PPK Data Collection

1. **Prepare Your Equipment**: Ensure the drone, base station, and GPS receivers are fully charged and connected.
2. **Set the Base Station**: Place the base station at a known, stable geodetic point.
3. **Start the Drone Flight**:
    - For **RTK**: Ensure the drone is connected to the base station and receiving real-time corrections.
    - For **PPK**: Ensure the drone is logging GPS data for post-processing.
4. **Collect Imagery**: Fly the drone to capture the required images, ensuring enough overlap for photogrammetry.
5. **End the Flight**: Once the survey area is covered, land the drone safely and retrieve the equipment.

---

## Post-Processing with PPK

After completing the flight, the next step is to process the data:

1. **Base Station Logs**: Download the base station log files.
2. **Drone GPS Logs**: Retrieve the drone’s GPS logs.
3. **Post-Processing Software**: Use specialized software (e.g., **RTKLIB**, **POSPac**, or proprietary software from the drone manufacturer) to process the data. This software uses the base station logs to apply corrections to the drone’s GPS logs.
4. **Export Corrected Data**: Export the corrected GPS data for use in photogrammetry software, such as **Agisoft Metashape** or **Pix4D**.

---

## Troubleshooting Common Issues

- **RTK Data Loss**: If the drone loses RTK connection, you may need to rely on PPK or increase the frequency of RTK corrections.
- **Base Station Misalignment**: Ensure that the base station is correctly set up over a known geodetic point, as errors here will affect all georeferenced data.
- **Incorrect GCPs**: If you're using GCPs for further georeferencing, make sure they are measured with **RTK** or **PPK** for optimal accuracy.

---

## Conclusion

Both **RTK** and **PPK** are essential technologies in drone surveying for achieving **high-accuracy** georeferencing. While RTK provides real-time corrections, PPK enables post-processing of GPS data after flight, offering flexibility and accuracy for various applications in photogrammetry, mapping, and geospatial analysis.

For a beginner, understanding these workflows and setups is crucial for producing reliable and precise georeferenced maps and models.

---

## References
- [RTKLIB Official Website](http://rtklib.com/)
- [Agisoft Metashape Documentation](https://www.agisoft.com/)

