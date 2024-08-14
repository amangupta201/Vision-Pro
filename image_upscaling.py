import os
import cv2

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)


def upscale_image(image_path, scale=2):
    image = cv2.imread(image_path)
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    upscaled_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)

    enhanced_path = os.path.join(ENHANCED_FOLDER, 'upscaled_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, upscaled_image)
    return enhanced_path
