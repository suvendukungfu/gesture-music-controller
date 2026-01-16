import cv2
from collections import deque

from src.hand_tracking import HandTracker
from src.gesture_logic import is_fist, is_open_palm, detect_swipe
from src.music_player import MusicPlayer
from src.ui_overlay import draw_text


def main():
    cap = cv2.VideoCapture(0)

    tracker = HandTracker()
    player = MusicPlayer()

    cooldown = 0
    x_buffer = deque(maxlen=8)  # store recent x positions

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = tracker.process(frame)

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            tracker.draw(frame, hand)

            index_tip_x = hand.landmark[8].x
            x_buffer.append(index_tip_x)

            if cooldown == 0:
                landmarks = hand.landmark

                # Play / Pause
                if is_fist(landmarks):
                    player.play_pause()
                    draw_text(frame, "Play / Pause")
                    cooldown = 20
                    x_buffer.clear()

                # Stop
                elif is_open_palm(landmarks):
                    player.stop()
                    draw_text(frame, "Stop")
                    cooldown = 20
                    x_buffer.clear()

                # Swipe
                else:
                    swipe = detect_swipe(list(x_buffer))
                    if swipe == "right":
                        player.next_song()
                        draw_text(frame, "Next Song ▶")
                        cooldown = 25
                        x_buffer.clear()

                    elif swipe == "left":
                        player.previous_song()
                        draw_text(frame, "Previous Song ◀")
                        cooldown = 25
                        x_buffer.clear()

        if cooldown > 0:
            cooldown -= 1

        cv2.imshow("Gesture Music Controller", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
