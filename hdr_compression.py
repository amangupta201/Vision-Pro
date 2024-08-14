import cv2
import os

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)



def hdr_compression(image_path):
    image = cv2.imread(image_path)
    hdr_image = cv2.detailEnhance(image, sigma_s=12, sigma_r=0.15)

    enhanced_path = os.path.join(ENHANCED_FOLDER, 'hdr_compressed_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, hdr_image)
    return enhanced_path
