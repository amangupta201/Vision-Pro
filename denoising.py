import os
from skimage import io
from skimage.filters import gaussian

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)

def enhance_denoising(image_path):
    # Load the image
    image = io.imread(image_path, as_gray=True)

    # Apply Gaussian filter
    sigma = 1  # Adjust sigma value as needed
    denoised_img = gaussian(image, sigma=sigma)

    # Save the enhanced image
    enhanced_path = os.path.join(ENHANCED_FOLDER, 'denoised_' + os.path.basename(image_path))
    io.imsave(enhanced_path, (denoised_img * 255).astype('uint8'))
    return enhanced_path
