import cv2

# ---------------------------------------
# MediaPipe Hand Connections
# ---------------------------------------

HAND_CONNECTIONS = [

    # Thumb
    (0,1),(1,2),(2,3),(3,4),

    # Index
    (0,5),(5,6),(6,7),(7,8),

    # Middle
    (5,9),(9,10),(10,11),(11,12),

    # Ring
    (9,13),(13,14),(14,15),(15,16),

    # Pinky
    (13,17),(17,18),(18,19),(19,20),

    # Palm
    (0,17)
]


# ---------------------------------------
# Draw One Hand
# ---------------------------------------

def draw_hand(frame, landmarks, handedness=None):

    h, w, _ = frame.shape

    points = []

    for lm in landmarks:

        x = int(lm.x * w)
        y = int(lm.y * h)

        points.append((x, y))

        cv2.circle(
            frame,
            (x, y),
            5,
            (0,255,0),
            -1
        )

    for start, end in HAND_CONNECTIONS:

        cv2.line(
            frame,
            points[start],
            points[end],
            (255,0,0),
            2
        )

    # Draw Left / Right label
    if handedness:

        wrist = points[0]

        cv2.putText(
            frame,
            handedness,
            (wrist[0]-15, wrist[1]-20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,255),
            2
        )

# ---------------------------------------
# Draw All Detected Hands
# ---------------------------------------

def draw_detected_hands(frame, feature_data):
    """
    Draw all detected hands with L/R labels.
    """

    if feature_data["left_landmarks"] is not None:
        draw_hand(
            frame,
            feature_data["left_landmarks"],
            "L"
        )

    if feature_data["right_landmarks"] is not None:
        draw_hand(
            frame,
            feature_data["right_landmarks"],
            "R"
        )

# ---------------------------------------
# Draw UI
# ---------------------------------------

def draw_ui(
        frame,
        label,
        sample_count,
        countdown,
        status
):

    cv2.putText(
        frame,
        f"Gesture : {label}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    cv2.putText(
        frame,
        f"Samples : {sample_count}",
        (20,75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        f"Next Capture : {countdown:.1f}s",
        (20,110),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )

    color = (0,255,0)

    if "No" in status:
        color = (0,0,255)

    cv2.putText(
        frame,
        status,
        (20,145),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    cv2.putText(
        frame,
        "Press Q to Quit",
        (20,180),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,255),
        2
    )