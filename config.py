"""
AgriVision AI
Central Project Configuration
"""

APP_NAME = "AgriVision AI"
APP_TAGLINE = "AI-Powered Smart Agriculture Intelligence Platform"
APP_VERSION = "1.0.0"

SUPPORTED_CROPS = ["Tomato", "Potato", "Corn", "Apple"]

IMAGE_TYPES = ["jpg", "jpeg", "png"]
MAX_IMAGE_SIZE_MB = 10
IMAGE_SIZE = (224, 224)

MODEL_PATH = "models/agrivision_mobilenet_finetuned_best.keras"
CLASS_LABELS_PATH = "models/class_labels.json"
CALIBRATION_PATH = "models/calibration.json"
MODEL_NAME = "MobileNetV2"
NUM_CLASSES = 21
MODEL_TEMPERATURE = 1.1289

# Conservative display gate; this is not an out-of-distribution detector.
MIN_PREDICTION_CONFIDENCE = 0.60

MODEL_TRAINED = True
PREDICTION_ENABLED = True

DATABASE_PROVIDER = "Supabase"
DATABASE_ENABLED = False
