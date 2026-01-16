import pygame
import os


class MusicPlayer:
    def __init__(self, music_dir="local_music"):
        pygame.mixer.init()

        self.songs = [
            os.path.join(music_dir, f)
            for f in os.listdir(music_dir)
            if f.endswith((".mp3", ".wav", ".ogg"))
        ]

        self.index = 0
        self.paused = False
        self.volume = 0.5

        pygame.mixer.music.set_volume(self.volume)

        if not self.songs:
            print("❌ No music files found in local_music/")
        else:
            print(f"✅ Loaded {len(self.songs)} songs")

    def play_pause(self):
        if not self.songs:
            return

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.songs[self.index])
            pygame.mixer.music.play()
            self.paused = False
        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.pause()
            self.paused = True

    def stop(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.paused = False

    def next_song(self):
        if not self.songs:
            return

        self.index = (self.index + 1) % len(self.songs)
        pygame.mixer.music.load(self.songs[self.index])
        pygame.mixer.music.play()
        self.paused = False

    def previous_song(self):
        if not self.songs:
            return

        self.index = (self.index - 1) % len(self.songs)
        pygame.mixer.music.load(self.songs[self.index])
        pygame.mixer.music.play()
        self.paused = False

    def set_volume(self, volume):
        volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(volume)
        self.volume = volume

    def get_volume(self):
        return self.volume
