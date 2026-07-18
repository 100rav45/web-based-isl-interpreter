import cv2
import time
import mediapipe as mp
from pathlib import Path
from config import *

from utils.feature_utils import extract_features
from utils.drawing_utils import draw_detected_hands, draw_ui
from utils.mediapipe_utils import create_detector

def choose_category():

    while True:

        print("\nSelect Category")
        print("1. Digits")
        print("2. Alphabet")
        print("3. Words")

        choice = input("\nChoice: ").strip()

        if choice == "1":
            return "digits"

        elif choice == "2":
            return "alphabet"

        elif choice == "3":
            return "words"

        print("Invalid choice.")

def get_label():

    while True:

        label = input("\nEnter Label: ").strip().upper()

        if label:
            return label

        print("Label cannot be empty.")


def create_output_folder(category, label):

    folder = (
        DATA_DIR /
        "datasets" /
        "custom" /
        category /
        label
    )

    folder.mkdir(
        parents=True,
        exist_ok=True
    )

    return folder

def get_next_image_number(output_folder, label):
    """
    Find the next available image number.
    Example:
        A_000001.jpg
        A_000002.jpg
    """

    images = sorted(output_folder.glob(f"{label}_*.jpg"))

    if not images:
        return 1

    last_image = images[-1].stem

    try:
        return int(last_image.split("_")[-1]) + 1
    except:
        return len(images) + 1

def initialize_camera():

    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        raise RuntimeError(
            "Unable to open webcam."
        )

    return cap

def get_next_image_number(folder: Path, label: str):

    existing = sorted(folder.glob(f"{label}_*.jpg"))

    if not existing:
        return 1

    last = existing[-1].stem

    try:
        return int(last.split("_")[-1]) + 1
    except:
        return len(existing) + 1

def main():

    category = choose_category()

    label = get_label()

    output_folder = create_output_folder(
        category,
        label
    )

    image_number = get_next_image_number(
    output_folder,
    label
    )

    detector = create_detector()

    cap = initialize_camera()

    frame_index = 0

    sample_count = 0

    last_capture_time = time.time()

    status = "Waiting..."

    print(f"\nSaving to:\n{output_folder}\n")

    while True:

        success, frame = cap.read()

        if not success:
            break

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        result = detector.detect_for_video(
            mp_image,
            frame_index
        )

        frame_index += 1

        feature_data = extract_features(result)

        draw_detected_hands(
            frame,
            feature_data
        )

        countdown = max(
            0,
            CAPTURE_INTERVAL -
            (time.time() - last_capture_time)
        )

        status = f"Hands Detected: {feature_data['num_hands']}"

        draw_ui(
            frame,
            label,
            sample_count,
            countdown,
            status
        )
    
    # =====================================
    # Auto Capture
    # =====================================

        if (
            feature_data["num_hands"] > 0
            and countdown <= 0
        ):

            filename = f"{label}_{image_number:06d}.jpg"

            save_path = output_folder / filename

            feature_data = extract_features(result)

            if feature_data["num_hands"] == 0:

                status = "No Hand Detected - Image Skipped"

                continue
            
            cv2.imwrite(
                str(save_path),
                frame
            )

            sample_count += 1
            image_number += 1

            last_capture_time = time.time()

            status = "Image Saved!"

        cv2.imshow(
            WINDOW_NAME,
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
        main()