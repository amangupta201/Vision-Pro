from flask import Flask, request, render_template, send_file
import os

from artistic_filters import apply_artistic_filter
from background_removal import remove_background
from cartoonify import cartoonify_image
from color_correction import color_correction
from contrast_enhancement import enhance_contrast
from deblurring import deblur_image
from grayscale import grayscale_conversion
from hdr_compression import hdr_compression
from image_sharpening import sharpen_image
from image_stitching import image_stitching
from super_resolution import enhance_super_resolution
from denoising import enhance_denoising
from watermark import add_watermark

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ENHANCED_FOLDER = 'enhanced'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENHANCED_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('image')  # Get list of uploaded files
        filepaths = []

        # Save all files and store their paths
        for file in files:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            filepaths.append(filepath)

        enhancement_type = request.form['enhancement_type']
        if enhancement_type == "super_resolution":
            enhanced_image_path = enhance_super_resolution(filepaths[0])
        elif enhancement_type == "denoising":
            enhanced_image_path = enhance_denoising(filepaths[0])
        elif enhancement_type == "color_correction":
            enhanced_image_path = color_correction(filepaths[0])
        elif enhancement_type == "sharpen_image":
            enhanced_image_path = sharpen_image(filepaths[0])
        elif enhancement_type == "contrast_enhancement":
            enhanced_image_path = enhance_contrast(filepaths[0])
        elif enhancement_type == "deblur_image":
            enhanced_image_path = deblur_image(filepaths[0])
        elif enhancement_type == "hdr_compression":
            enhanced_image_path = hdr_compression(filepaths[0])
        elif enhancement_type == "artistic_filter":
            enhanced_image_path = apply_artistic_filter(filepaths[0])
        elif enhancement_type == "grayscale_conversion":
            enhanced_image_path = grayscale_conversion(filepaths[0])
        elif enhancement_type == "image_stitching":
            # Pass all uploaded file paths for stitching
            enhanced_image_path = image_stitching(filepaths)
        elif enhancement_type == "watermarking":
            enhanced_image_path = add_watermark(filepaths[0])
        elif enhancement_type == "background_removal":
            enhanced_image_path = remove_background(filepaths[0])
        elif enhancement_type == "cartoonify":
            enhanced_image_path = cartoonify_image(filepath)
        else:
            return "Invalid enhancement type selected."

        return send_file(enhanced_image_path, mimetype='image/png')

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
