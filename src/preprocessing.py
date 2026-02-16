import cv2
import numpy as np

def read_image(path):
    """Read an image from path."""
    img = cv2.imread(path)
    return img

def extract_red_channel(img):
    """Extract red channel from BGR image."""
    return img[:, :, 2]

def crop_image(img, x, y, w, h):
    """Crop image with rectangle (x, y, w, h)."""
    return img[y:y+h, x:x+w]

def median_filter(img, ksize=3):
    """Apply median filter."""
    return cv2.medianBlur(img, ksize)
