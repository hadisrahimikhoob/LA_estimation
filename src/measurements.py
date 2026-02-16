import numpy as np

def polygon_area(x, y):
    """Calculate polygon area using Shoelace formula."""
    return 0.5 * abs(np.dot(x, np.roll(y,1)) - np.dot(y, np.roll(x,1)))

def calibrated_area(leaf_coords, ref_coords):
    """Compute calibrated area in cm² based on reference object."""
    leaf_area = polygon_area(*leaf_coords)
    ref_area = polygon_area(*ref_coords)
    return leaf_area / ref_area
