import cv2
import os


def draw_panel(frame, x=20, y=20, w=360, h=230):
    overlay = frame.copy()
    cv2.rectangle(overlay, (x, y), (x + w, y + h), (20, 20, 20), -1)
    cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


def draw_title(frame, text="🎵 Gesture Music Controller", x=30, y=45):
    cv2.putText(frame, text, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.line(frame, (x, y + 5), (x + 300, y + 5), (0, 255, 0), 1)


def draw_song(frame, song_path, playing, x=30, y=85):
    if not song_path:
        text = "No music found"
        color = (0, 0, 255)
    else:
        name = os.path.basename(song_path)
        icon = "▶" if playing else "⏸"
        text = f"{icon} {name}"
        color = (255, 255, 255)

    cv2.putText(frame, f"Song: {text}", (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)


def draw_gesture(frame, gesture, x=30, y=120):
    cv2.putText(frame, f"Gesture: {gesture}", (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 0), 2)


def draw_volume(frame, volume, x=30, y=150, w=280, h=18):
    cv2.putText(frame, "Volume", (x, y - 8),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)

    fill = int(w * volume)
    cv2.rectangle(frame, (x, y), (x + fill, y + h), (0, 255, 0), -1)

    percent = int(volume * 100)
    cv2.putText(frame, f"{percent}%", (x + w + 10, y + h),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)


def draw_help(frame, x=30, y=200):
    cv2.putText(frame, "← Swipe: Prev   → Swipe: Next",
                (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (200, 200, 200), 1)
