import cv2
import os

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)



def enhance_contrast(image_path):
    image = cv2.imread(image_path, 0)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(image)

    enhanced_path = os.path.join(ENHANCED_FOLDER, 'contrast_enhanced_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, enhanced_image)
    return enhanced_path
