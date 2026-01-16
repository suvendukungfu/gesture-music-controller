import cv2

from src.hand_tracking import HandTracker
from src.gesture_logic import is_fist, is_open_palm
from src.music_player import MusicPlayer
from src.ui_overlay import draw_text


def main():
    cap = cv2.VideoCapture(0)

    tracker = HandTracker()
    player = MusicPlayer()

    cooldown = 0  # frames to wait before next gesture

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = tracker.process(frame)

        if result.multi_hand_landmarks and cooldown == 0:
            hand = result.multi_hand_landmarks[0]
            tracker.draw(frame, hand)

            landmarks = hand.landmark

            if is_fist(landmarks):
                player.play_pause()
                draw_text(frame, "Play / Pause")
                cooldown = 20

            elif is_open_palm(landmarks):
                player.stop()
                draw_text(frame, "Stop")
                cooldown = 20

        if cooldown > 0:
            cooldown -= 1

        cv2.imshow("Gesture Music Controller", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
