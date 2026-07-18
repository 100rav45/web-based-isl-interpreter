from config import FEATURES_PER_HAND, NUM_HANDS

def empty_hand():
    
    return [0.0] * FEATURES_PER_HAND


def hand_to_features(hand_landmarks):
    """
    Converts one detected hand into
    63 numerical features.
    """

    features = []

    for lm in hand_landmarks:
        features.extend([
            lm.x,
            lm.y,
            lm.z
        ])

    return features


def extract_features(result):
    """
    Returns a fixed-length feature vector.
    Output:
    Left Hand (63)
    +
    Right Hand (63)
    = 126 Features
    """

    left_features = empty_hand()
    right_features = empty_hand()

    left_landmarks = None
    right_landmarks = None
    num_hands = 0

    if not result.hand_landmarks:
        return {
            "features": left_features + right_features,
            "left_landmarks": None,
            "right_landmarks": None,
            "num_hands": 0
        }
        
    num_hands = min(
    len(result.hand_landmarks),
    NUM_HANDS
    )

    for i, hand in enumerate(result.hand_landmarks):

        handedness = result.handedness[i][0].category_name

        if handedness == "Left":
            left_landmarks = hand
            left_features = hand_to_features(hand)

        elif handedness == "Right":
            right_landmarks = hand
            right_features = hand_to_features(hand)

    return {
        "features": left_features + right_features,
        "left_landmarks": left_landmarks,
        "right_landmarks": right_landmarks,
        "num_hands": num_hands
    }