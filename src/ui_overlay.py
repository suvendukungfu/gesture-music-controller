import cv2
import os


def draw_text(frame, text, pos=(30, 40), scale=1, color=(0, 255, 0)):
    cv2.putText(
        frame,
        text,
        pos,
        cv2.FONT_HERSHEY_SIMPLEX,
        scale,
        color,
        2
    )


def draw_volume_bar(frame, volume, x=30, y=80, w=200, h=20):
    """
    volume: 0.0 - 1.0
    """
    # Outline
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)

    # Filled bar
    fill_width = int(w * volume)
    cv2.rectangle(frame, (x, y), (x + fill_width, y + h), (0, 255, 0), -1)

    percent = int(volume * 100)
    draw_text(frame, f"Volume: {percent}%", (x, y - 10), scale=0.6)


def draw_song_name(frame, song_path, x=30, y=140):
    if not song_path:
        return

    song_name = os.path.basename(song_path)
    draw_text(frame, f"Song: {song_name}", (x, y), scale=0.6)
