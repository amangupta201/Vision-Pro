import os
import cv2

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)



def grayscale_conversion(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    enhanced_path = os.path.join(ENHANCED_FOLDER, 'grayscale_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, image)
    return enhanced_path
