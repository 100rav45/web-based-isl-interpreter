import cv2
import csv
import os 
from tqdm import tqdm

import mediapipe as mp
from mediapipe.tasks.python import vision
from config import DATA_DIR, CSV_FILE
from utils.feature_utils import extract_features
from utils.mediapipe_utils import create_detector

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}

TEMP_CSV_FILE = CSV_FILE.with_name("isl_landmarks_temp.csv")

def discover_dataset():

    dataset_root = DATA_DIR / "datasets"

    images = []

    for source in ["public", "custom"]:

        source_path = dataset_root / source

        if not source_path.exists():
            continue

        for category in source_path.iterdir():

            if not category.is_dir():
                continue

            for label in category.iterdir():

                if not label.is_dir():
                    continue

                for image in label.iterdir():

                    if image.suffix.lower() in IMAGE_EXTENSIONS:

                        images.append({

                            "source": source,

                            "category": category.name,

                            "label": label.name,

                            "path": image

                        })

    return images

def create_csv():

    with open(TEMP_CSV_FILE, "w", newline="") as f:

        writer = csv.writer(f)

        header = ["label"]

        # Left Hand (63 features)
        for i in range(21):
            header.extend([
                f"L_x{i}",
                f"L_y{i}",
                f"L_z{i}"
            ])

        # Right Hand (63 features)
        for i in range(21):
            header.extend([
                f"R_x{i}",
                f"R_y{i}",
                f"R_z{i}"
            ])

        writer.writerow(header)

def main():

    images = discover_dataset()

    print("\nDataset Summary")
    print("=" * 40)

    print(f"Total Images : {len(images)}")

    labels = sorted(set(img["label"] for img in images))

    print(f"Classes Found : {len(labels)}")

    create_csv()

    detector = create_detector(
        vision.RunningMode.IMAGE
    )

    successful = 0
    skipped = 0

    with open(TEMP_CSV_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        for image_info in tqdm(
            images,
            desc="Converting Images",
            unit="image"
        ):

            try:

                image = cv2.imread(
                    str(image_info["path"])
                )

                if image is None:
                    skipped += 1
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

                feature_data = extract_features(result)

                if feature_data["num_hands"] == 0:
                    skipped += 1
                    continue

                row = [image_info["label"]]
                row.extend(feature_data["features"])

                writer.writerow(row)

                successful += 1

                # ALL your existing code for this image
                # (rgb conversion, MediaPipe, feature extraction, writer.writerow, etc.)

            except Exception as e:

                skipped += 1
                print(f"Skipped: {image_info['path'].name} -> {e}")



    print("\nConversion Complete")
    print("=" * 40)
    print(f"Successful : {successful}")
    print(f"Skipped    : {skipped}")

    # Replace old CSV with new one
    if successful > 0:

       os.replace(
        TEMP_CSV_FILE,
        CSV_FILE
       )
    print("\nCSV updated successfully.")
    print(f"CSV Saved  : {CSV_FILE}")

if __name__ == "__main__":
    main()