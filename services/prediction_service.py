"""
AgriVision AI
Disease Prediction Service
"""

import os
import json
from functools import lru_cache

import numpy as np
from PIL import Image

from config import (
    MODEL_PATH,
    CLASS_LABELS_PATH,
    CALIBRATION_PATH,
    IMAGE_SIZE,
    MODEL_TRAINED,
    PREDICTION_ENABLED,
    MODEL_TEMPERATURE,
    SUPPORTED_CROPS
)


# --------------------------------------------------
# 1. CROP NAME NORMALIZATION
# --------------------------------------------------

CROP_ALIASES = {
    "tomato": "Tomato",
    "tamatar": "Tomato",
    "potato": "Potato",
    "aloo": "Potato",
    "alu": "Potato",
    "corn": "Corn",
    "maize": "Corn",
    "makai": "Corn",
    "makkai": "Corn",
    "apple": "Apple",
    "seb": "Apple",
    "saib": "Apple",
}


def normalize_crop_name(crop_name):
    """Return the canonical supported crop name, or None."""

    if not crop_name:
        return None

    normalized = " ".join(str(crop_name).strip().lower().replace("_", " ").split())

    canonical_name = CROP_ALIASES.get(normalized)

    if canonical_name and canonical_name in SUPPORTED_CROPS:
        return canonical_name

    for supported_crop in SUPPORTED_CROPS:
        if normalized == supported_crop.lower():
            return supported_crop

    return None


# --------------------------------------------------
# 2. LOAD TRAINED MODEL
# --------------------------------------------------

@lru_cache(maxsize=1)
def load_model():
    """Load the trained MobileNetV2 model."""

    if not MODEL_TRAINED or not PREDICTION_ENABLED:
        return None

    if not os.path.exists(MODEL_PATH):
        return None

    try:
        import tensorflow as tf

        return tf.keras.models.load_model(
            MODEL_PATH,
            compile=False
        )

    except Exception as error:
        print(f"Model loading error: {error}")
        return None


# --------------------------------------------------
# 3. LOAD CLASS LABELS
# --------------------------------------------------

@lru_cache(maxsize=1)
def load_class_labels():
    """Load the 21 crop disease class labels."""

    if not os.path.exists(CLASS_LABELS_PATH):
        raise FileNotFoundError("Class labels file was not found.")

    with open(CLASS_LABELS_PATH, "r", encoding="utf-8") as file:
        labels_data = json.load(file)

    return [
        labels_data[str(index)]
        for index in range(len(labels_data))
    ]


# --------------------------------------------------
# 4. LOAD CALIBRATION SETTINGS
# --------------------------------------------------

def load_temperature():
    """Read temperature scaling configuration."""

    if os.path.exists(CALIBRATION_PATH):

        with open(CALIBRATION_PATH, "r", encoding="utf-8") as file:
            calibration_data = json.load(file)

        temperature = float(
            calibration_data.get("temperature", MODEL_TEMPERATURE)
        )

    else:
        temperature = float(MODEL_TEMPERATURE)

    if temperature <= 0:
        raise ValueError("Invalid calibration temperature.")

    return temperature


# --------------------------------------------------
# 5. PREPROCESS IMAGE
# --------------------------------------------------

def preprocess_image(image):
    """Prepare an uploaded image for MobileNetV2."""

    if not isinstance(image, Image.Image):
        image = Image.fromarray(np.asarray(image))

    image = image.convert("RGB")
    image = image.resize(IMAGE_SIZE, Image.Resampling.BILINEAR)

    image_array = np.asarray(image, dtype=np.float32)
    image_array = np.expand_dims(image_array, axis=0)

    import tensorflow as tf

    return tf.keras.applications.mobilenet_v2.preprocess_input(
        image_array
    )


# --------------------------------------------------
# 6. TEMPERATURE CALIBRATION
# --------------------------------------------------

def calibrate_probabilities(probabilities, temperature):
    """Apply temperature scaling to model probabilities."""

    probabilities = np.clip(probabilities, 1e-12, 1.0)
    logits = np.log(probabilities)
    scaled_logits = logits / temperature

    exp_values = np.exp(scaled_logits - np.max(scaled_logits))
    return exp_values / np.sum(exp_values)


# --------------------------------------------------
# 7. PREDICT CROP DISEASE
# --------------------------------------------------

def predict_disease(image, expected_crop=None):
    """
    Predict disease only when the user-entered crop is supported.

    The current model does not automatically identify arbitrary crops.
    """

    if image is None:
        return {
            "status": "error",
            "message": "Please upload a crop leaf image."
        }

    if expected_crop is None:
        return {
            "status": "error",
            "message": "Please enter the crop name before prediction."
        }

    normalized_crop = normalize_crop_name(expected_crop)

    if normalized_crop is None:
        return {
            "status": "unsupported",
            "message": (
                f"Disease prediction for '{expected_crop}' is not available yet. "
                "You can upload the image, but this AI model currently supports "
                "only Tomato, Potato, Corn and Apple. No disease diagnosis has "
                "been generated for this crop."
            )
        }

    model = load_model()

    if model is None:
        return {
            "status": "unavailable",
            "message": (
                "AI model is currently unavailable. "
                "Please check model configuration."
            )
        }

    try:

        labels = load_class_labels()
        temperature = load_temperature()
        processed_image = preprocess_image(image)

        predictions = model.predict(processed_image, verbose=0)
        probabilities = np.asarray(predictions[0], dtype=np.float64)

        if probabilities.ndim != 1 or len(probabilities) != len(labels):
            raise ValueError("Model output does not match the class labels.")

        if not np.all(np.isfinite(probabilities)):
            raise ValueError("Model returned invalid prediction values.")

        calibrated_probabilities = calibrate_probabilities(
            probabilities,
            temperature
        )

        predicted_index = int(np.argmax(calibrated_probabilities))
        predicted_label = labels[predicted_index]

        if "___" not in predicted_label:
            raise ValueError("Invalid class label format.")

        predicted_crop, disease = predicted_label.split("___", maxsplit=1)

        # Never show a disease result if the model crop differs from
        # the crop name supplied by the user.
        if predicted_crop.lower() != normalized_crop.lower():
            return {
                "status": "mismatch",
                "message": (
                    f"You entered '{normalized_crop}', but the model's top "
                    f"class belongs to '{predicted_crop}'. The result has "
                    "been blocked to avoid showing a potentially incorrect "
                    "disease diagnosis. Please check the crop name and image."
                )
            }

        confidence = float(calibrated_probabilities[predicted_index])

        top_indices = np.argsort(calibrated_probabilities)[-3:][::-1]
        top_predictions = []

        for index in top_indices:

            label = labels[int(index)]

            if "___" not in label:
                continue

            top_crop, top_disease = label.split("___", maxsplit=1)

            top_predictions.append({
                "crop": top_crop,
                "disease": top_disease,
                "confidence": float(calibrated_probabilities[index])
            })

        return {
            "status": "success",
            "crop": predicted_crop,
            "disease": disease,
            "confidence": confidence,
            "top_predictions": top_predictions,
            "temperature": temperature,
            "message": "Prediction completed successfully."
        }

    except Exception as error:

        print(f"Prediction error: {error}")

        return {
            "status": "error",
            "message": (
                "Prediction could not be completed. "
                "Please check the application logs."
            )
        }
