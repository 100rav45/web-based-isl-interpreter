import cv2
import mediapipe as mp

from mediapipe.tasks.python import vision

from utils.feature_utils import extract_features
from utils.mediapipe_utils import create_detector

from app.backend.services.prediction_service import (
    prediction_service
)


class ImagePredictionService:

    def __init__(self):

        self.detector = create_detector(
            vision.RunningMode.VIDEO
        )
        self.frame_index = 0

    def predict(self, image):

        rgb = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2RGB
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = self.detector.detect_for_video(
            mp_image,
            self.frame_index
        )
        self.frame_index += 1

        feature_data = extract_features(
            result
        )

        if feature_data["num_hands"] == 0:

            return {

                "prediction": None,

                "confidence": None

            }

        return prediction_service.predict(
            feature_data["features"]
        )


image_prediction_service = ImagePredictionService()