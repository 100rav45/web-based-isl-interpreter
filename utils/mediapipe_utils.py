"""
mediapipe_utils.py

Shared MediaPipe initialization.
Supports both VIDEO and IMAGE modes.
"""

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from config import HAND_LANDMARK_MODEL, NUM_HANDS


def create_detector(running_mode=vision.RunningMode.VIDEO):
    """
    Create a MediaPipe Hand Landmarker.

    Parameters
    ----------
    running_mode : vision.RunningMode
        VIDEO (default) -> For webcam applications.
        IMAGE           -> For processing still images.

    Returns
    -------
    vision.HandLandmarker
    """

    base_options = python.BaseOptions(
        model_asset_path=str(HAND_LANDMARK_MODEL)
    )

    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        num_hands=NUM_HANDS,
        running_mode=running_mode,

        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5
    )

    return vision.HandLandmarker.create_from_options(options)