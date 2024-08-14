import os
from PIL import Image

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)

def enhance_super_resolution(image_path, scale_factor=2):
    # Load the image
    image = Image.open(image_path)

    # Calculate the new size
    width, height = image.size
    new_size = (width * scale_factor, height * scale_factor)

    # Apply bicubic interpolation
    resized_image = image.resize(new_size, Image.BICUBIC)

    # Save the enhanced image
    enhanced_path = os.path.join(ENHANCED_FOLDER, 'super_res_' + os.path.basename(image_path))
    resized_image.save(enhanced_path)
    return enhanced_path
