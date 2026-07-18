import cv2
import joblib
import mediapipe as mp
from collections import Counter, deque
from config import MODEL_DIR

from utils.feature_utils import extract_features
from utils.drawing_utils import draw_detected_hands
from utils.mediapipe_utils import create_detector

from mediapipe.tasks.python import vision

MODEL_FILE = MODEL_DIR / "random_forest_model.pkl"

LABEL_ENCODER_FILE = MODEL_DIR / "label_encoder.pkl"

# ==============================
# Prediction Configuration
# ==============================

SMOOTHING_WINDOW = 5

prediction_history = deque(
    maxlen=SMOOTHING_WINDOW
)

def load_model():

    print("Loading model...")

    model = joblib.load(MODEL_FILE)

    label_encoder = joblib.load(
        LABEL_ENCODER_FILE
    )

    print("Model Loaded Successfully.\n")

    return model, label_encoder

def initialize_detector():

    return create_detector(
        vision.RunningMode.VIDEO
    )

def initialize_camera():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        raise RuntimeError(
            "Unable to open webcam."
        )

    return cap

def smooth_prediction(prediction):

    prediction_history.append(prediction)

    return Counter(
        prediction_history
    ).most_common(1)[0][0]

def predict_gesture(
    model,
    label_encoder,
    features
):

    prediction = model.predict(
        [features]
    )[0]

    confidence = model.predict_proba(
        [features]
    )[0].max()

    label = label_encoder.inverse_transform(
        [prediction]
    )[0]

    return label, confidence

def main():

    model, label_encoder = load_model()

    detector = initialize_detector()

    cap = initialize_camera()

    frame_index = 0

    print("Press Q to Quit.\n")

    while True:

        ret, frame = cap.read()

        if not ret:
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

        if result.hand_landmarks:

            feature_data = extract_features(result)

            draw_detected_hands(
                frame,
                feature_data
            )

            label, confidence = predict_gesture(
                model,
                label_encoder,
                feature_data["features"]
            )

            label = smooth_prediction(label)

            cv2.putText(
                frame,
                f"Prediction : {label}",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )

            cv2.putText(
                frame,
                f"Confidence : {confidence*100:.2f}%",
                (20,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255,255,255),
                2
            )

        else:

            cv2.putText(
                frame,
                "No Hand Detected",
                (20,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                2
            )

        cv2.imshow(
            "ISL Predictor V2",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()