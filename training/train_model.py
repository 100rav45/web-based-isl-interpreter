import pandas as pd
import joblib
import json
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
from config import CSV_FILE, DATA_DIR

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    precision_score,
    recall_score,
    f1_score
)

MODEL_NAME = "RandomForest"
MODEL_ALGORITHM = "Random Forest"

MODEL_DIR = DATA_DIR.parent / "models"

MODEL_DIR.mkdir(
    exist_ok=True
)

RESULTS_DIR = DATA_DIR.parent / "results"

RESULTS_DIR.mkdir(exist_ok=True)

MODEL_FILE = MODEL_DIR / "random_forest_model.pkl"

LABEL_ENCODER_FILE = MODEL_DIR / "label_encoder.pkl"

MODEL_INFO_FILE = MODEL_DIR / "random_forest_model_info.json"


def load_dataset():

    print("Loading dataset...")

    df = pd.read_csv(CSV_FILE, dtype={"label":str})

    print(f"Samples  : {len(df)}")
    print(f"Columns  : {len(df.columns)}")

    if df.empty:
        raise ValueError("Dataset is empty.")

    if "label" not in df.columns:
        raise ValueError("Missing 'label' column.")

    print("\nDataset loaded successfully.\n")

    return df

def prepare_dataset(df):
    """
    Prepare features and labels for training.
    """

    # Features
    X = df.drop(columns=["label"])

    # Labels
    y = df["label"]

    # Encode labels
    label_encoder = LabelEncoder()

    y_encoded = label_encoder.fit_transform(y)

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_encoded,
        test_size=0.25,
        random_state=42,
        stratify=y_encoded
    )

    print("Dataset Prepared")
    print("=" * 40)

    print(f"Total Samples : {len(df)}")
    print(f"Training      : {len(X_train)}")
    print(f"Testing       : {len(X_test)}")
    print(f"Classes       : {len(label_encoder.classes_)}")
    print(f"Features      : {X_train.shape[1]}")

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        label_encoder
    )

def train_model(X_train, y_train):

    print("\nTraining Random Forest...")
    print("=" * 40)

    model = RandomForestClassifier(

        n_estimators=300,

        random_state=42,

        n_jobs=-1
    )

    model.fit(
        X_train,
        y_train
    )


    print("Training Completed.\n")

    return model

def evaluate_model(model, X_test, y_test, label_encoder):

    print("\nEvaluating Model...")
    print("=" * 40)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    print(f"Accuracy : {accuracy:.4f}")

    print("\nClassification Report\n")

    print(
        classification_report(
            y_test,
            predictions,
            target_names=label_encoder.classes_
        )
    )

    cm = confusion_matrix(
        y_test,
        predictions
    )
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=label_encoder.classes_
    )

    fig, ax = plt.subplots(figsize=(14,14))

    disp.plot(
        ax=ax,
        cmap="Blues",
        xticks_rotation=90
    )

    plt.tight_layout()

    plt.savefig(
        RESULTS_DIR / "confusion_matrix.png",
        dpi=300
    )

    plt.close()

    print("Confusion Matrix Shape:", cm.shape)

    metrics = {

        "accuracy": float(accuracy),

        "precision": float(precision),

        "recall": float(recall),

        "f1_score": float(f1)

    }

    with open(
        RESULTS_DIR / "metrics.json",
        "w"
    ) as f:

        json.dump(
            metrics,
            f,
            indent=4
        )

    return accuracy, cm, metrics

def save_model(
    model,
    label_encoder,
    accuracy,
    X_train,
    X_test
):

    print("\nSaving Model...")
    print("=" * 40)

    # Save trained model
    joblib.dump(
        model,
        MODEL_FILE
    )

    # Save label encoder
    joblib.dump(
        label_encoder,
        LABEL_ENCODER_FILE
    )

    # Model metadata
    model_info = {

        "model_name": MODEL_NAME,

        "algorithm": MODEL_ALGORITHM,

        "model_file": MODEL_FILE.name,

        "label_encoder": LABEL_ENCODER_FILE.name,

        "accuracy": round(float(accuracy), 6),

        "training_samples": len(X_train),

        "testing_samples": len(X_test),

        "features": X_train.shape[1],

        "classes": len(label_encoder.classes_),

        "class_labels": label_encoder.classes_.tolist(),

        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    }

    with open(
        MODEL_INFO_FILE,
        "w"
    ) as f:

        json.dump(
            model_info,
            f,
            indent=4
        )

    print("Model Saved Successfully.\n")

    print(f"Model          : {MODEL_FILE}")
    print(f"Label Encoder  : {LABEL_ENCODER_FILE}")
    print(f"Model Info     : {MODEL_INFO_FILE}")

def main():

    df = load_dataset()

    X_train, X_test, y_train, y_test, label_encoder = prepare_dataset(df)

    model = train_model(
    X_train,
    y_train
    )

    accuracy, cm, metrics = evaluate_model(
        model,
        X_test,
        y_test,
        label_encoder
    )
    
    save_model(
        model,
        label_encoder,
        accuracy,
        X_train,
        X_test
    )

    print("\nClass Labels:\n")
    print(label_encoder.classes_)

if __name__ == "__main__":
    main()