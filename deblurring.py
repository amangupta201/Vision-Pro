import cv2
import os
import numpy as np

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)



def deblur_image(image_path):
    image = cv2.imread(image_path, 0)
    psf = np.ones((5, 5)) / 25  # Simple point spread function
    deconvolved = cv2.filter2D(image, -1, psf)

    enhanced_path = os.path.join(ENHANCED_FOLDER, 'deblurred_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, deconvolved)
    return enhanced_path
