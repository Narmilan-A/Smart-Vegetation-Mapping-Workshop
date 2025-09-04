# 🛰️ Coordinate Systems & Altitudes in Drone-Based Mapping

This beginner-friendly guide introduces the key types of coordinate systems and altitude references used in drone-based data collection. Understanding these concepts is crucial for accurate photogrammetry, remote sensing, and 3D modeling.

---

## 📌 What is a Coordinate System?

A **coordinate system** allows us to define the location of objects in 2D or 3D space. Drones use coordinate systems to geotag images, generate maps, and align spatial data with real-world positions.

There are two main types:

### 1. **Geographic Coordinate System (GCS)**
- Based on a 3D ellipsoid model of Earth
- Uses **latitude**, **longitude**, and **ellipsoid height**
- Example: `WGS84` (used by GPS)
- Units: degrees

### 2. **Projected Coordinate System (PCS)**
- Flattens the 3D globe into a 2D map using projections
- Uses **X, Y (and sometimes Z)** coordinates
- Example: `UTM` (Universal Transverse Mercator)
- Units: meters

---

## 🌍 Common Coordinate Systems in Drone Mapping

| System | Type | Used For |
|--------|------|----------|
| WGS84 | Geographic | Default for drone GPS data and EXIF tags |
| UTM | Projected | Mapping, measuring distances and areas |
| Local Grid | Projected or relative | Custom maps, construction sites, small areas |

Drones usually store image coordinates in **WGS84**. These can be reprojected into UTM for easier distance calculations and orthomosaic generation.

---

## 📏 Types of Altitudes in Drone Mapping

In drone-based workflows, understanding different altitude types is essential to align your image metadata, GCPs, and models correctly.

### 1. **Ellipsoid Height**
- Measured from the mathematical ellipsoid (like WGS84)
- Output from most GPS systems and stored in drone EXIF
- Not corrected for terrain or sea level

### 2. **Orthometric Height (Absolute Height)**
- Measured from the **geoid** (approximated mean sea level)
- This is the "elevation above sea level"
- Used in most maps, GCPs, and DEMs

### 3. **Relative Height (AGL)**
- Measured from the takeoff point or ground
- Common in drone flight planning (e.g., fly 60 m above ground)

---

## 🔍 Difference Between Ellipsoid Height and Geoid Height

- **Ellipsoid Height** is the vertical distance from a point on the Earth's surface to the reference ellipsoid, which is a smooth, mathematical representation of the Earth's shape. It is what most GPS systems output and is usually stored in drone EXIF data.
- **Geoid Height** (or **Geoid Separation**) is the difference between the ellipsoid and the geoid. The **geoid** represents the mean sea level (MSL) across the Earth's surface, making it a more accurate reference for real-world sea-level measurements.

In simple terms:
- Ellipsoid height: Measured from a mathematical model of Earth.
- Geoid height: Measured from the Earth's actual sea level, which is affected by local variations in gravity.

To convert from **ellipsoid height** to **absolute (orthometric) height**, you subtract the **geoid height**:

```math
Orthometric Height (H) = Ellipsoid Height (h) - Geoid Height (N)
```



![ellipsoid_to_egm2008](https://github.com/user-attachments/assets/b4047c0d-0193-43e1-a1c6-200edc748714)

---

## 🧭 Summary Table of Height Types

| Height Type         | Measured From              | Also Called             | Common Use Case                                  |
|---------------------|----------------------------|--------------------------|--------------------------------------------------|
| **Absolute Height** | 🌊 Geoid (mean sea level)   | Orthometric Height       | Maps, GCPs, terrain elevation                    |
| **Ellipsoid Height**| 🏐 Ellipsoid (e.g., WGS84)  | GPS Height, Geodetic Height | Drone EXIF metadata, RTK GPS outputs         |
| **Relative Height** | ⛰️ Ground/local surface     | Above Ground Level (AGL) | Flight planning, camera altitudes, local models |

---

## 📐 How to Convert Between Heights

To convert GPS height (ellipsoid height) to orthometric height:

```math
Orthometric Height (H) = Ellipsoid Height (h) - Geoid Height (N)
```

- `h` = height from ellipsoid (GPS or RTK)
- `N` = geoid separation (difference between ellipsoid and sea level)
- `H` = orthometric (absolute) height

> You can find local geoid heights using tools like NOAA’s VERTCON (US) or AusGeoid (Australia).

---

## 📷 Drone Example Use Case

If your drone image EXIF says:
- **Ellipsoid height** = 120.0 m
- **Geoid height at the site** = 38.0 m

Then:
```math
Absolute height (H) = 120.0 - 38.0 = 82.0 m above sea level
```

This conversion ensures accurate comparison with GCPs or elevation models that use sea level.

---

## 🗺️ Summary for Drone Users

- GPS and RTK systems typically record **ellipsoid heights**.
- Ground Control Points (GCPs) usually use **absolute (orthometric)** heights.
- For accurate photogrammetry, convert your drone camera altitudes to **orthometric height** using the local **geoid separation**.
- Always check whether your software expects ellipsoid or orthometric height.

---
