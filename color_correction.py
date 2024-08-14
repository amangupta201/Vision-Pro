import os

import cv2
import numpy as np
ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)


def color_correction(image_path):
    image = cv2.imread(image_path)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.equalizeHist(l)
    lab = cv2.merge((l, a, b))
    corrected_image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    enhanced_path = os.path.join(ENHANCED_FOLDER, 'color_corrected_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, corrected_image)
    return enhanced_path
