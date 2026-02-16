import cv2
import numpy as np
from skimage import measure

def otsu_threshold(img):
    """Apply Otsu thresholding."""
    _, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    binary = 255 - binary  # invert to match MATLAB ~imbinarize
    return binary

def fill_holes(binary_img):
    """Fill holes using morphology."""
    return cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, np.ones((3,3), np.uint8))

def label_regions(binary_img):
    """Label connected components and return properties."""
    labels = measure.label(binary_img, connectivity=2)
    props = measure.regionprops(labels, intensity_image=binary_img)
    return labels, props
