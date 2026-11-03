"""
AgriVision AI
Central Project Configuration
"""

# --------------------------------------------------
# 1. APPLICATION INFORMATION
# --------------------------------------------------

APP_NAME = "AgriVision AI"

APP_TAGLINE = "AI-Powered Smart Agriculture Intelligence Platform"

APP_VERSION = "1.0.0"


# --------------------------------------------------
# 2. SUPPORTED CROPS
# --------------------------------------------------

SUPPORTED_CROPS = [
    "Tomato",
    "Potato",
    "Corn",
    "Apple"
]


# --------------------------------------------------
# 3. IMAGE SETTINGS
# --------------------------------------------------

IMAGE_TYPES = [
    "jpg",
    "jpeg",
    "png"
]

MAX_IMAGE_SIZE_MB = 10

IMAGE_SIZE = (224, 224)


# --------------------------------------------------
# 4. MACHINE LEARNING MODEL SETTINGS
# --------------------------------------------------

MODEL_PATH = "models/agrivision_mobilenet_finetuned_best.keras"

CLASS_LABELS_PATH = "models/class_labels.json"

CALIBRATION_PATH = "models/calibration.json"

MODEL_NAME = "MobileNetV2"

NUM_CLASSES = 21

MODEL_TEMPERATURE = 1.1289


# --------------------------------------------------
# 5. PROJECT STATUS
# --------------------------------------------------

MODEL_TRAINED = True

# Predictions will be enabled after prediction_service.py
# has been updated and successfully tested.

PREDICTION_ENABLED = True

# --------------------------------------------------
# 6. DATABASE SETTINGS
# --------------------------------------------------

DATABASE_PROVIDER = "Supabase"

DATABASE_ENABLED = False
