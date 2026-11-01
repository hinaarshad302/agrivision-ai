
"""
AgriVision AI
Disease Prediction Service
"""

import os

from config import (
    MODEL_PATH,
    MODEL_TRAINED,
    PREDICTION_ENABLED
)


def load_model():
    """
    Load the trained AI model when available.
    """

    if not MODEL_TRAINED or not PREDICTION_ENABLED:
        return None

    if not os.path.exists(MODEL_PATH):
        return None

    try:
        import tensorflow as tf

        model = tf.keras.models.load_model(MODEL_PATH)

        return model

    except Exception:
        return None


def predict_disease(image):
    """
    Handle the crop disease prediction process.
    """

    if image is None:
        return {
            "status": "error",
            "message": "Please provide a valid crop image."
        }

    model = load_model()

    if model is None:
        return {
            "status": "unavailable",
            "message": (
                "AI model is not trained or configured yet. "
                "Please try again after model deployment."
            )
        }

    return {
        "status": "pending",
        "message": (
            "Model loaded successfully. "
            "Prediction processing will be implemented "
            "after model training."
        )
    }
