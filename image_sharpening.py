import os
import cv2
import numpy as np


ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)

def sharpen_image(image_path):
    image = cv2.imread(image_path)
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel)

    enhanced_path = os.path.join(ENHANCED_FOLDER, 'sharpened_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, sharpened)
    return enhanced_path
