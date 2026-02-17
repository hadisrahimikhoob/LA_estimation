# Leaf Segmentation and Area Measurement

This project segments leaf images and calculates calibrated area (cm²) using Python and OpenCV.

## Features

- Extract the red channel of a leaf image.
- Apply median filtering to reduce noise.
- Segment the leaf using Otsu thresholding.
- Fill holes in the binary mask.
- Label connected components in the segmented image.
- Calculate calibrated area using reference object.
- Visualize the segmented leaf.

## Installation

```bash
git clone <your-repo-url>
cd <your-repo-folder>
pip install -r requirements.txt


