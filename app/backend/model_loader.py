import joblib

from app.backend.config import (
    MODEL_FILE,
    LABEL_ENCODER_FILE
)


class ModelLoader:

    def __init__(self):

        self.model = None
        self.label_encoder = None

    def load(self):

        if self.model is None:

            print("Loading Random Forest...")

            self.model = joblib.load(
                MODEL_FILE
            )

            self.label_encoder = joblib.load(
                LABEL_ENCODER_FILE
            )

            print("Model Loaded Successfully.")

        return self.model, self.label_encoder


model_loader = ModelLoader()