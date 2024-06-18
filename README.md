# Thermal Image Person Detection

## Project Description

This project focuses on detecting persons in thermal images using image processing techniques. The provided thermal image shows multiple figures, and the system processes the image to identify and count the number of persons present. Bounding boxes are drawn around the detected persons for visualization.

Thermal imaging is a technique used to detect heat emitted by objects, making it useful in various applications, including military surveillance, search and rescue operations, and security. This project leverages Python libraries such as PIL, NumPy, scikit-image, and Matplotlib to achieve person detection in thermal images.

## Features

- **Grayscale Conversion**: Converts the thermal image to grayscale for easier processing.
- **Thresholding**: Applies a binary threshold to differentiate between persons and the background.
- **Morphological Operations**: Removes small objects from the binary image to reduce noise.
- **Labeling and Region Properties**: Labels connected regions in the binary image and calculates their properties.
- **Bounding Boxes**: Draws bounding boxes around detected persons for visualization.

---

## Guide

### 1. Setup

#### Prerequisites

Ensure you have Python 3.x installed along with the necessary libraries: PIL, NumPy, scikit-image, and Matplotlib.

#### Installation

Install the required libraries using pip:

```bash
pip install pillow numpy scikit-image matplotlib
```

### 2. Image Processing and Person Detection

The following steps describe the process of detecting persons in the thermal image and visualizing the results:

1. **Load the Image**: Use PIL to load the thermal image.
2. **Convert to Grayscale**: Convert the loaded image to grayscale by averaging the RGB channels.
3. **Apply Thresholding**: Apply a binary threshold to separate the persons (bright areas) from the background.
4. **Remove Small Objects**: Use morphological operations to remove small objects from the binary image, reducing noise.
5. **Label Connected Regions**: Label the connected regions in the binary image and calculate their properties.
6. **Draw Bounding Boxes**: For each detected region that meets the size criteria, draw a bounding box around it.
7. **Display the Image**: Display the original image with bounding boxes using Matplotlib.
8. **Count Persons**: Print the number of detected persons.

---

By following this guide, you can set up, run, and evaluate the person detection system for thermal images. This system is applicable in various scenarios such as surveillance, search and rescue, border security, and combat situations, where thermal imaging can help detect persons in low-visibility conditions.
