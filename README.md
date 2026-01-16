It includes:

* Clear project overview
* Gesture table
* Demo GIF section
* Setup & run instructions
* Tech stack
* Future improvements
* Professional tone (intern/interview ready)

---

# 🎵 Gesture-Controlled Music Player

Control your **local music playback using hand gestures** in real time — powered by **OpenCV**, **MediaPipe**, and **pygame**.

This project uses **computer vision–based hand tracking** to recognize gestures through a webcam and map them to music controls like play, pause, stop, next/previous song, and volume adjustment.

---

## 🚀 Features

* 🎥 Real-time webcam hand tracking
* ✋ Gesture-based music control
* 🎵 Local music playback
* 🎨 On-screen UI overlay

  * Current gesture label
  * Volume bar & percentage
  * Current song name
* 🧠 Gesture cooldown to prevent accidental triggers
* 🧩 Modular, clean Python architecture

---

## ✋ Supported Gestures

| Gesture                      | Action         |
| ---------------------------- | -------------- |
| ✊ **Fist**                   | Play / Pause   |
| ✋ **Open Palm**              | Stop           |
| 👉 **Swipe Right**           | Next Song      |
| 👈 **Swipe Left**            | Previous Song  |
| ✌️ **Two Fingers (Up/Down)** | Volume Control |

---

## 🎬 Demo

> 📌 **Add a GIF or video here after recording**

```md
![Gesture Music Player Demo](assets/demo.gif)
```

**How to record demo GIF (recommended):**

* macOS: QuickTime / ScreenFlow
* Convert to GIF using ezgif.com or ffmpeg
* Place file in `assets/demo.gif`

---

## 🧠 How It Works (High Level)

1. **OpenCV** captures webcam frames
2. **MediaPipe Hands** detects 21 hand landmarks
3. Gesture logic analyzes landmark positions
4. Gestures are mapped to music controls
5. **pygame** handles audio playback
6. UI overlays are drawn on each frame

---

## 🗂 Project Structure

```
gesture-music-controller/
│
├── src/
│   ├── __init__.py
│   ├── main.py              # Main controller
│   ├── hand_tracking.py     # MediaPipe hand detection
│   ├── gesture_logic.py     # Gesture recognition
│   ├── music_player.py     # Music control (pygame)
│   └── ui_overlay.py        # UI elements
│
├── local_music/             # Add your songs here
├── assets/
│   └── demo.gif
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/gesture-music-controller.git
cd gesture-music-controller
```

### 2️⃣ Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🎶 Add Music

1. Create / open the `local_music/` folder
2. Add audio files:

   * `.mp3`
   * `.wav`
   * `.ogg`

Example:

```
local_music/
 ├── song1.mp3
 └── song2.wav
```

---

## ▶️ Run the Application

```bash
python -m src.main
```

🛑 Press **ESC** to exit.

---

## 🔐 macOS Camera Permission (Important)

Go to:

```
System Settings → Privacy & Security → Camera
```

Enable access for:

* ✅ Terminal
* ✅ Visual Studio Code (if used)

Restart Terminal after enabling.

---

## 🧪 Tips for Best Performance

* Keep your hand **clearly visible**
* Use gestures **deliberately**, not too fast
* Maintain **steady lighting**
* Keep palm facing the camera

---

## 🛠 Tech Stack

* **Python 3.11**
* **OpenCV**
* **MediaPipe**
* **pygame**
* **NumPy**

---

## 🌱 Future Improvements

* 🎚 System volume control (OS-level)
* 🧠 ML-based gesture classification
* 🎧 Spotify API integration
* 🖥 Desktop app (Tkinter / PyQt)
* 📱 Mobile camera support

---

## 👨‍💻 Author

**Suvendu Kumar Sahoo**

Built as a hands-on **Computer Vision + Python project** to explore real-time gesture recognition and human-computer interaction.

---

## 📜 License

This project is open-source and free to use for learning and experimentation.

---

### ✅ Final Step (Commit README)

```bash
git add README.md
git commit -m "Add final README with gesture table and demo section"
```
