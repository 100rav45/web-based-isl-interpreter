"""
csv_utils.py

Handles all CSV operations for the project.
"""

import csv
from pathlib import Path


def create_csv(csv_path: Path):
    """
    Create CSV with the correct header if it doesn't exist.
    """

    if csv_path.exists():
        return

    with open(csv_path, "w", newline="") as f:

        writer = csv.writer(f)

        header = ["label"]

        # Left Hand
        for i in range(21):
            header.extend([
                f"left_x{i}",
                f"left_y{i}",
                f"left_z{i}"
            ])

        # Right Hand
        for i in range(21):
            header.extend([
                f"right_x{i}",
                f"right_y{i}",
                f"right_z{i}"
            ])

        writer.writerow(header)


def append_sample(csv_path: Path, label: str, features: list):
    """
    Append one training sample.
    """

    with open(csv_path, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([label] + features)


def count_samples(csv_path: Path, label: str):
    """
    Count how many samples already exist
    for a particular label.
    """

    if not csv_path.exists():
        return 0

    count = 0

    with open(csv_path, newline="") as f:

        reader = csv.reader(f)

        next(reader, None)

        for row in reader:

            if row and row[0] == label:
                count += 1

    return count