def is_fist(landmarks):
    return (
        landmarks[8].y > landmarks[6].y and
        landmarks[12].y > landmarks[10].y and
        landmarks[16].y > landmarks[14].y and
        landmarks[20].y > landmarks[18].y
    )


def is_open_palm(landmarks):
    return (
        landmarks[8].y < landmarks[6].y and
        landmarks[12].y < landmarks[10].y and
        landmarks[16].y < landmarks[14].y and
        landmarks[20].y < landmarks[18].y
    )


def is_two_fingers(landmarks):
    return (
        landmarks[8].y < landmarks[6].y and
        landmarks[12].y < landmarks[10].y and
        landmarks[16].y > landmarks[14].y and
        landmarks[20].y > landmarks[18].y
    )


def detect_swipe(x_positions, threshold=0.08):
    if len(x_positions) < 5:
        return None

    delta = x_positions[-1] - x_positions[0]

    if delta > threshold:
        return "right"
    elif delta < -threshold:
        return "left"

    return None
