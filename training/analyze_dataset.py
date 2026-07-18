import cv2
from collections import Counter

import mediapipe as mp
from mediapipe.tasks.python import vision

from utils.mediapipe_utils import create_detector
from training.convert_dataset_to_csv import discover_dataset


def main():

    detector = create_detector(
        vision.RunningMode.IMAGE
    )

    images = discover_dataset()

    stats = Counter()

    print(f"\nAnalyzing {len(images)} images...\n")

    for image_info in images:

        try:

            image = cv2.imread(str(image_info["path"]))

            if image is None:
                stats["Corrupted Image"] += 1
                continue

            rgb = cv2.cvtColor(
                image,
                cv2.COLOR_BGR2RGB
            )

            mp_image = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=rgb
            )

            result = detector.detect(mp_image)

            if not result.hand_landmarks:
                stats["No Hand Detected"] += 1
                continue

            stats["Successful"] += 1

        except Exception:

            stats["Exception"] += 1

    print("=" * 45)
    print("Dataset Analysis")
    print("=" * 45)

    for key, value in stats.items():
        print(f"{key:<20}: {value}")

    print("=" * 45)


if __name__ == "__main__":
    main()