# main.py
import numpy as np
import cv2
from src.preprocessing import read_image, extract_red_channel, crop_image, median_filter
from src.segmentation import otsu_threshold, fill_holes, label_regions
from src.measurements import calibrated_area
from src.utils import show_image

# ======== Dummy Data (simulate a leaf image) =========
# Create a black image
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Draw a red ellipse to simulate a leaf
cv2.ellipse(img, (250, 250), (100, 150), 0, 0, 360, (0, 0, 255), -1)

# ================= Preprocessing =================
red_channel = extract_red_channel(img)         # Extract red channel
filtered_img = median_filter(red_channel)      # Apply median filter
crop_img = filtered_img                         # For dummy data, take full image

# ================= Segmentation =================
binary_img = otsu_threshold(crop_img)          # Apply Otsu threshold
binary_img = fill_holes(binary_img)            # Fill holes
labels, props = label_regions(binary_img)      # Label connected components

# ================= Calibrated Area =================
# Example coordinates for leaf and reference object
leaf_coords = np.array([[150, 100], [350, 100], [350, 400], [150, 400]])
ref_coords = np.array([[10, 10], [60, 10], [60, 60], [10, 60]])

# Transpose coordinates to match polygon_area function (x, y)
area_cm2 = calibrated_area(leaf_coords.T, ref_coords.T)
print(f"Leaf area (cm²): {area_cm2:.2f}")

# ================= Visualization =================
show_image(binary_img, title='Segmented Leaf')
