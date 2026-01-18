import cv2
import time

from src.hand_tracking import HandTracker
from src.music_player import MusicPlayer
from src.ui_overlay import (
    draw_panel,
    draw_title,
    draw_song,
    draw_gesture,
    draw_volume,
    draw_help
)

# -----------------------------
# Configuration
# -----------------------------
CAMERA_INDEX = 0
GESTURE_COOLDOWN = 1.0  # seconds


def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        print("❌ Cannot open camera")
        return

    tracker = HandTracker()
    player = MusicPlayer()
    player.load_songs("songs")

    last_action_time = 0
    gesture_label = "None"

    print("🎵 Gesture Music Controller started")
    print("Press ESC to exit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        # -----------------------------
        # Hand Tracking
        # -----------------------------
        result = tracker.process(frame)

        current_time = time.time()
        can_act = (current_time - last_action_time) > GESTURE_COOLDOWN

        if result.multi_hand_landmarks and can_act:
            gesture = tracker.detect_gesture(result)

            if gesture == "PLAY_PAUSE":
                player.play_pause()
                gesture_label = "✊ Play / Pause"
                last_action_time = current_time

            elif gesture == "NEXT":
                player.next_song()
                gesture_label = "👉 Swipe Right (Next)"
                last_action_time = current_time

            elif gesture == "PREVIOUS":
                player.prev_song()
                gesture_label = "👈 Swipe Left (Previous)"
                last_action_time = current_time

            elif gesture == "VOLUME_UP":
                player.change_volume(0.05)
                gesture_label = "👍 Volume Up"

            elif gesture == "VOLUME_DOWN":
                player.change_volume(-0.05)
                gesture_label = "👎 Volume Down"

        # -----------------------------
        # UI Overlay
        # -----------------------------
        draw_panel(frame)
        draw_title(frame)
        draw_song(frame, player.current_song(), player.playing)
        draw_gesture(frame, gesture_label)
        draw_volume(frame, player.get_volume())
        draw_help(frame)

        cv2.imshow("Gesture Music Controller", frame)

        # ESC to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    player.stop()
    print("👋 Exited cleanly")


if __name__ == "__main__":
    main()
