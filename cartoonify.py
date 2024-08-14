import os

import cv2
import numpy as np
from skimage import io
ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)


def cartoonify_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Apply bilateral filter to smoothen the image
    color = cv2.bilateralFilter(img, 9, 300, 300)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Combine edges with the smoothened image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Save the cartoonified image
    enhanced_path = os.path.join(ENHANCED_FOLDER, 'cartoonified_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, cartoon)

    return enhanced_path
