from pathlib import Path

# =====================================
# Project Directories
# =====================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
MODEL_DIR = BASE_DIR / "models"
UTILS_DIR = BASE_DIR / "utils"

# =====================================
# Models
# =====================================

HAND_LANDMARK_MODEL = MODEL_DIR / "hand_landmarker.task"

RANDOM_FOREST_MODEL = MODEL_DIR / "random_forest_model.pkl"

LABEL_ENCODER_MODEL = MODEL_DIR / "label_encoder.pkl"

MODEL_INFO_FILE = MODEL_DIR / "random_forest_model_info.json"

# =====================================
# Dataset
# =====================================

CSV_FILE = DATA_DIR / "isl_landmarks.csv"

NEW_DATA_FILE = DATA_DIR / "new_samples.csv"

# =====================================
# MediaPipe
# =====================================

NUM_HANDS = 2

CAPTURE_INTERVAL = 2.0

# =====================================
# Feature Vector
# =====================================

LANDMARKS_PER_HAND = 21

FEATURES_PER_LANDMARK = 3

FEATURES_PER_HAND = LANDMARKS_PER_HAND * FEATURES_PER_LANDMARK

TOTAL_FEATURES = FEATURES_PER_HAND * NUM_HANDS

# =====================================
# Webcam
# =====================================

CAMERA_INDEX = 0
WINDOW_NAME = "ISL Dataset Collector V2"