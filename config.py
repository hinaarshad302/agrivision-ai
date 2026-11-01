
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

MODEL_PATH = "models/agrivision_mobilenet.keras"

CLASS_LABELS_PATH = "models/class_labels.json"

MODEL_NAME = "MobileNetV2"


# --------------------------------------------------
# 5. PROJECT STATUS
# --------------------------------------------------

MODEL_TRAINED = False

PREDICTION_ENABLED = False


# --------------------------------------------------
# 6. DATABASE SETTINGS
# --------------------------------------------------

DATABASE_PROVIDER = "Supabase"

DATABASE_ENABLED = False
