
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
    MODEL_TEMPERATURE
)


# --------------------------------------------------
# 1. LOAD TRAINED MODEL
# --------------------------------------------------

@lru_cache(maxsize=1)
def load_model():
    """
    Load the trained MobileNetV2 model.
    """

    if not MODEL_TRAINED or not PREDICTION_ENABLED:
        return None

    if not os.path.exists(MODEL_PATH):
        return None

    try:
        import tensorflow as tf

        model = tf.keras.models.load_model(
            MODEL_PATH,
            compile=False
        )

        return model

    except Exception as error:
        print(f"Model loading error: {error}")
        return None


# --------------------------------------------------
# 2. LOAD CLASS LABELS
# --------------------------------------------------

@lru_cache(maxsize=1)
def load_class_labels():
    """
    Load the 21 crop disease class labels.
    """

    if not os.path.exists(CLASS_LABELS_PATH):
        raise FileNotFoundError(
            "Class labels file was not found."
        )

    with open(CLASS_LABELS_PATH, "r") as file:
        labels_data = json.load(file)

    return [
        labels_data[str(index)]
        for index in range(len(labels_data))
    ]


# --------------------------------------------------
# 3. LOAD CALIBRATION SETTINGS
# --------------------------------------------------

def load_temperature():
    """
    Read temperature scaling configuration.
    """

    if os.path.exists(CALIBRATION_PATH):

        with open(CALIBRATION_PATH, "r") as file:
            calibration_data = json.load(file)

        temperature = float(
            calibration_data.get(
                "temperature",
                MODEL_TEMPERATURE
            )
        )

    else:
        temperature = float(MODEL_TEMPERATURE)

    if temperature <= 0:
        raise ValueError("Invalid calibration temperature.")

    return temperature


# --------------------------------------------------
# 4. PREPROCESS IMAGE
# --------------------------------------------------

def preprocess_image(image):
    """
    Prepare an uploaded image for MobileNetV2.
    """

    if not isinstance(image, Image.Image):
        image = Image.fromarray(np.asarray(image))

    image = image.convert("RGB")

    image = image.resize(
        IMAGE_SIZE,
        Image.Resampling.BILINEAR
    )

    image_array = np.asarray(
        image,
        dtype=np.float32
    )

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    # MobileNetV2 preprocessing: pixel values -1 to 1
    import tensorflow as tf

    image_array = tf.keras.applications.mobilenet_v2.preprocess_input(
        image_array
    )

    return image_array


# --------------------------------------------------
# 5. TEMPERATURE CALIBRATION
# --------------------------------------------------

def calibrate_probabilities(probabilities, temperature):
    """
    Apply temperature scaling to model probabilities.
    """

    probabilities = np.clip(
        probabilities,
        1e-12,
        1.0
    )

    logits = np.log(probabilities)

    scaled_logits = logits / temperature

    exp_values = np.exp(
        scaled_logits - np.max(scaled_logits)
    )

    calibrated = exp_values / np.sum(exp_values)

    return calibrated


# --------------------------------------------------
# 6. PREDICT CROP DISEASE
# --------------------------------------------------

def predict_disease(image):
    """
    Predict crop disease from an uploaded leaf image.
    """

    if image is None:
        return {
            "status": "error",
            "message": "Please upload a crop leaf image."
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

        predictions = model.predict(
            processed_image,
            verbose=0
        )

        probabilities = np.asarray(
            predictions[0],
            dtype=np.float64
        )

        if len(probabilities) != len(labels):
            raise ValueError(
                "Model output does not match the class labels."
            )

        calibrated_probabilities = calibrate_probabilities(
            probabilities,
            temperature
        )

        predicted_index = int(
            np.argmax(calibrated_probabilities)
        )

        predicted_label = labels[predicted_index]

        crop, disease = predicted_label.split(
            "___",
            maxsplit=1
        )

        confidence = float(
            calibrated_probabilities[predicted_index]
        )

        top_indices = np.argsort(
            calibrated_probabilities
        )[-3:][::-1]

        top_predictions = []

        for index in top_indices:

            label = labels[int(index)]

            top_crop, top_disease = label.split(
                "___",
                maxsplit=1
            )

            top_predictions.append({
                "crop": top_crop,
                "disease": top_disease,
                "confidence": float(
                    calibrated_probabilities[index]
                )
            })

        return {
            "status": "success",
            "crop": crop,
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
