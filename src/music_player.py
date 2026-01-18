import pygame
import os


class MusicPlayer:
    def __init__(self, music_dir="local_music"):
        pygame.mixer.init()
        self.music_dir = music_dir
        self.songs = self.load_songs()
        self.index = 0
        self.volume = 0.5
        self.playing = False

        pygame.mixer.music.set_volume(self.volume)

    def load_songs(self):
        if not os.path.exists(self.music_dir):
            return []

        return [
            os.path.join(self.music_dir, f)
            for f in os.listdir(self.music_dir)
            if f.endswith((".mp3", ".wav", ".ogg"))
        ]

    def play_pause(self):
        if not self.songs:
            return

        if not self.playing:
            pygame.mixer.music.load(self.songs[self.index])
            pygame.mixer.music.play()
            self.playing = True
        else:
            pygame.mixer.music.pause()
            self.playing = False

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next_song(self):
        if not self.songs:
            return

        self.index = (self.index + 1) % len(self.songs)
        pygame.mixer.music.load(self.songs[self.index])
        pygame.mixer.music.play()
        self.playing = True

    def previous_song(self):
        if not self.songs:
            return

        self.index = (self.index - 1) % len(self.songs)
        pygame.mixer.music.load(self.songs[self.index])
        pygame.mixer.music.play()
        self.playing = True

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.volume)

    def get_volume(self):
        return self.volume

    def current_song(self):
        if not self.songs:
            return None
        return self.songs[self.index]
