# gesture_logic.py

def is_fist(landmarks):
    tips = [8, 12, 16, 20]
    for tip in tips:
        if landmarks[tip].y < landmarks[tip - 2].y:
            return False
    return True


def is_open_palm(landmarks):
    tips = [8, 12, 16, 20]
    for tip in tips:
        if landmarks[tip].y > landmarks[tip - 2].y:
            return False
    return True


def detect_swipe(x_positions, threshold=0.15):
    """
    x_positions: list of x values (0–1 normalized)
    returns: "right", "left", or None
    """
    if len(x_positions) < 5:
        return None

    delta = x_positions[-1] - x_positions[0]

    if delta > threshold:
        return "right"
    elif delta < -threshold:
        return "left"

    return None
