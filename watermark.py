import os
import cv2

ENHANCED_FOLDER = 'enhanced'

# Ensure the enhanced folder exists
os.makedirs(ENHANCED_FOLDER, exist_ok=True)




def add_watermark(image_path, watermark_text='Sample Watermark'):
    image = cv2.imread(image_path)
    overlay = image.copy()
    output = image.copy()

    # Set font and scale
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1
    thickness = 2
    color = (0, 255, 0)

    # Get size of the text box
    text_size = cv2.getTextSize(watermark_text, font, scale, thickness)[0]

    # Set text position
    text_x = image.shape[1] - text_size[0] - 10
    text_y = image.shape[0] - 10

    # Add text to image
    cv2.putText(overlay, watermark_text, (text_x, text_y), font, scale, color, thickness)

    # Blend images
    cv2.addWeighted(overlay, 0.5, output, 0.5, 0, output)

    enhanced_path = os.path.join(ENHANCED_FOLDER, 'watermarked_' + os.path.basename(image_path))
    cv2.imwrite(enhanced_path, output)
    return enhanced_path
