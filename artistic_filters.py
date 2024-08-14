import cv2
import os

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)




def apply_artistic_filter(image_path, filter_type='pencil'):
    image = cv2.imread(image_path)
    if filter_type == 'pencil':
        _, filtered = cv2.pencilSketch(image, sigma_s=60, sigma_r=0.07, shade_factor=0.1)
    elif filter_type == 'watercolor':
        filtered = cv2.stylization(image, sigma_s=60, sigma_r=0.6)
    else:
        filtered = image  # No filter applied

    enhanced_path = os.path.join(ENHANCED_FOLDER, filter_type + '_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, filtered)
    return enhanced_path
