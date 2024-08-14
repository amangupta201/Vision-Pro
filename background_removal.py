import numpy as np
import cv2
import os

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)


def remove_background(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
    foreground = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(thresh))

    enhanced_path = os.path.join(ENHANCED_FOLDER, 'background_removed_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, foreground)
    return enhanced_path
