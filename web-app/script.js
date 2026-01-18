const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const audio = document.getElementById("audio");

const songText = document.getElementById("song");
const gestureText = document.getElementById("gesture");
const volumeBar = document.getElementById("volume");
const startBtn = document.getElementById("startBtn");

canvas.width = 480;
canvas.height = 360;

const songs = ["songs/song1.mp3", "songs/song2.mp3", "songs/song3.mp3"];
let songIndex = 0;
audio.src = songs[songIndex];

let volume = 0.5;
audio.volume = volume;

let lastX = null;
let lastSwipeTime = 0;

startBtn.onclick = () => {
  audio.play();
  startBtn.style.display = "none";
  startCamera();
};

function startCamera() {
  const hands = new Hands({
    locateFile: file =>
      `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`,
  });

  hands.setOptions({
    maxNumHands: 1,
    minDetectionConfidence: 0.7,
    minTrackingConfidence: 0.7,
  });

  hands.onResults(onResults);

  const camera = new Camera(video, {
    onFrame: async () => {
      await hands.send({ image: video });
    },
    width: 480,
    height: 360,
  });

  camera.start();
}

function onResults(results) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  if (!results.multiHandLandmarks) {
    gestureText.innerText = "Gesture: --";
    return;
  }

  const landmarks = results.multiHandLandmarks[0];

  // Draw skeleton
  drawConnectors(ctx, landmarks, HAND_CONNECTIONS, { color: "#00FFCC" });
  drawLandmarks(ctx, landmarks, { color: "#FF0000", radius: 4 });

  const fingersUp = countFingers(landmarks);

  // ✋ PLAY
  if (fingersUp === 5 && audio.paused) {
    audio.play();
    gestureText.innerText = "Gesture: Play ✋";
  }

  // ✊ PAUSE
  if (fingersUp === 0 && !audio.paused) {
    audio.pause();
    gestureText.innerText = "Gesture: Pause ✊";
  }

  // ✌️ VOLUME CONTROL
  const indexTip = landmarks[8];
  const middleTip = landmarks[12];
  const dist = Math.abs(indexTip.y - middleTip.y);

  if (dist < 0.04) {
    volume = Math.min(1, volume + 0.02);
    gestureText.innerText = "Gesture: Volume Up ✌️";
  } else {
    volume = Math.max(0, volume - 0.02);
    gestureText.innerText = "Gesture: Volume Down ✌️";
  }

  audio.volume = volume;
  volumeBar.style.width = `${volume * 100}%`;

  // 👉 👈 SWIPE
  const wristX = landmarks[0].x;
  const now = Date.now();

  if (lastX && now - lastSwipeTime > 1000) {
    if (wristX - lastX > 0.15) nextSong();
    if (lastX - wristX > 0.15) prevSong();
  }

  lastX = wristX;
}

function nextSong() {
  songIndex = (songIndex + 1) % songs.length;
  audio.src = songs[songIndex];
  audio.play();
  songText.innerText = `Song: ${songs[songIndex]}`;
  lastSwipeTime = Date.now();
}

function prevSong() {
  songIndex = (songIndex - 1 + songs.length) % songs.length;
  audio.src = songs[songIndex];
  audio.play();
  songText.innerText = `Song: ${songs[songIndex]}`;
  lastSwipeTime = Date.now();
}

function countFingers(lm) {
  let count = 0;
  if (lm[8].y < lm[6].y) count++;   // index
  if (lm[12].y < lm[10].y) count++; // middle
  if (lm[16].y < lm[14].y) count++; // ring
  if (lm[20].y < lm[18].y) count++; // pinky
  if (lm[4].x < lm[3].x) count++;   // thumb
  return count;
}
