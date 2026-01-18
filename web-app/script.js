const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

const audio = document.getElementById("audio");
const songText = document.getElementById("song");
const gestureText = document.getElementById("gesture");
const volumeFill = document.getElementById("volume-fill");

const songs = [
  "songs/song1.mp3",
  "songs/song2.mp3",
  "songs/song3.mp3"
];

let songIndex = 0;
let volume = 0.5;
let prevX = null;
let cooldown = false;

audio.src = songs[songIndex];
audio.volume = volume;
songText.innerText = "Song: " + songs[songIndex].split("/").pop();

function setCooldown() {
  cooldown = true;
  setTimeout(() => cooldown = false, 800);
}

const hands = new Hands({
  locateFile: file =>
    `https://cdn.jsdelivr.net/npm/@mediapipe/hands/${file}`
});

hands.setOptions({
  maxNumHands: 1,
  minDetectionConfidence: 0.7,
  minTrackingConfidence: 0.7
});

hands.onResults(results => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(results.image, 0, 0, canvas.width, canvas.height);

  if (!results.multiHandLandmarks) {
    prevX = null;
    return;
  }

  const lm = results.multiHandLandmarks[0];
  drawConnectors(ctx, lm, HAND_CONNECTIONS);
  drawLandmarks(ctx, lm);

  const index = lm[8];
  const middle = lm[12];
  const ring = lm[16];
  const wrist = lm[0];

  // ✌️ VOLUME
  if (!cooldown && index.y < ring.y && middle.y < ring.y) {
    if (index.y < 0.4) {
      volume = Math.min(1, volume + 0.05);
      gestureText.innerText = "Gesture: Volume Up";
      setCooldown();
    } else if (index.y > 0.6) {
      volume = Math.max(0, volume - 0.05);
      gestureText.innerText = "Gesture: Volume Down";
      setCooldown();
    }
    audio.volume = volume;
    volumeFill.style.width = (volume * 100) + "%";
  }

  // ✊ PLAY / PAUSE
  if (!cooldown &&
      lm[8].y > lm[6].y &&
      lm[12].y > lm[10].y &&
      lm[16].y > lm[14].y) {
    if (audio.paused) audio.play();
    else audio.pause();
    gestureText.innerText = "Gesture: Play / Pause";
    setCooldown();
  }

  // 👉 👈 SWIPE
  if (!cooldown && prevX !== null) {
    const diff = wrist.x - prevX;
    if (diff > 0.15) {
      songIndex = (songIndex + 1) % songs.length;
      audio.src = songs[songIndex];
      audio.play();
      songText.innerText = "Song: " + songs[songIndex].split("/").pop();
      gestureText.innerText = "Gesture: Next";
      setCooldown();
    } else if (diff < -0.15) {
      songIndex = (songIndex - 1 + songs.length) % songs.length;
      audio.src = songs[songIndex];
      audio.play();
      songText.innerText = "Song: " + songs[songIndex].split("/").pop();
      gestureText.innerText = "Gesture: Previous";
      setCooldown();
    }
  }

  prevX = wrist.x;
});

const camera = new Camera(video, {
  onFrame: async () => {
    await hands.send({ image: video });
  },
  width: 640,
  height: 480
});

camera.start();
