"""
Backend Configuration
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_DIR = PROJECT_ROOT / "models"

MODEL_FILE = MODEL_DIR / "random_forest_model.pkl"

LABEL_ENCODER_FILE = MODEL_DIR / "label_encoder.pkl"

MODEL_INFO_FILE = MODEL_DIR / "model_info.json"