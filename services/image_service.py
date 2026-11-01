
"""
AgriVision AI
Image Validation and Processing Service
"""

from PIL import Image
from config import IMAGE_TYPES, MAX_IMAGE_SIZE_MB, IMAGE_SIZE


def validate_image(uploaded_file):
    """
    Check whether the uploaded image is valid.
    """

    if uploaded_file is None:
        raise ValueError("Please upload an image.")

    file_size_mb = uploaded_file.size / (1024 * 1024)

    if file_size_mb > MAX_IMAGE_SIZE_MB:
        raise ValueError(
            f"Image size must not exceed {MAX_IMAGE_SIZE_MB} MB."
        )

    file_extension = uploaded_file.name.rsplit(".", 1)[-1].lower()

    if file_extension not in IMAGE_TYPES:
        raise ValueError("Only JPG, JPEG and PNG images are supported.")

    try:
        image = Image.open(uploaded_file).convert("RGB")
        return image

    except Exception as error:
        raise ValueError("Invalid or corrupted image file.") from error


def preprocess_image(image):
    """
    Resize the image for the AI model.
    """

    if image is None:
        raise ValueError("Image is required.")

    processed_image = image.resize(IMAGE_SIZE)

    return processed_image
