import os
import cv2

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)

def image_stitching(image_paths):
    images = []
    for img_path in image_paths:
        img = cv2.imread(img_path)
        if img is None:
            print(f"Error loading image: {img_path}")
            return f"Error loading image: {img_path}"
        images.append(img)

    stitcher = cv2.createStitcher() if int(cv2.__version__.split('.')[0]) < 4 else cv2.Stitcher_create()
    status, stitched_image = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        enhanced_path = os.path.join(ENHANCED_FOLDER, 'stitched_image.png')
        cv2.imwrite(enhanced_path, stitched_image)
        return enhanced_path
    else:
        return f"Error in image stitching: Status code {status}"

# Example usage
image_paths = ["path_to_image1.jpg", "path_to_image2.jpg", "path_to_image3.jpg"]
result = image_stitching(image_paths)
print(result)
