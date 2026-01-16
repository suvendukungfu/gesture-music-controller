import cv2
from collections import deque

from src.hand_tracking import HandTracker
from src.gesture_logic import (
    is_fist,
    is_open_palm,
    detect_swipe,
    is_two_fingers
)
from src.music_player import MusicPlayer
from src.ui_overlay import draw_text, draw_volume_bar, draw_song_name


def main():
    cap = cv2.VideoCapture(0)

    tracker = HandTracker()
    player = MusicPlayer()

    cooldown = 0
    x_buffer = deque(maxlen=8)
    current_gesture = ""

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = tracker.process(frame)

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            tracker.draw(frame, hand)

            landmarks = hand.landmark
            index_tip = landmarks[8]

            x_buffer.append(index_tip.x)

            if cooldown == 0:

                if is_fist(landmarks):
                    player.play_pause()
                    current_gesture = "Play / Pause"
                    cooldown = 20
                    x_buffer.clear()

                elif is_open_palm(landmarks):
                    player.stop()
                    current_gesture = "Stop"
                    cooldown = 20
                    x_buffer.clear()

                elif is_two_fingers(landmarks):
                    volume = 1 - index_tip.y
                    player.set_volume(volume)
                    current_gesture = "Volume Control"

                else:
                    swipe = detect_swipe(list(x_buffer))

                    if swipe == "right":
                        player.next_song()
                        current_gesture = "Next Song"
                        cooldown = 25
                        x_buffer.clear()

                    elif swipe == "left":
                        player.previous_song()
                        current_gesture = "Previous Song"
                        cooldown = 25
                        x_buffer.clear()

        if cooldown > 0:
            cooldown -= 1

        # ---------- UI OVERLAY ----------
        draw_text(frame, f"Gesture: {current_gesture}", (30, 30))
        draw_volume_bar(frame, player.get_volume())
        draw_song_name(frame, player.current_song())
        # --------------------------------

        cv2.imshow("Gesture Music Controller", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
