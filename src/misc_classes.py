# class for sentences
# class for sentence breakage

import time
import pygame

pygame.init()

class Text:
    def __init__(self, sentence):
        self.sentence = sentence
        for character in sentence:
                        print(character, end='', flush=True)
                        time.sleep(0.03)
        input().lower()



class Music:
    def __init__(self, track, channel, track_channel, loops, maxtime, fade_ms):
        self.track = track
        self.channel = channel
        self.track_channel = track_channel
        self.loops = loops
        self.maxtime = maxtime
        self.fade_ms = fade_ms

        self.track = pygame.mixer.Sound(f'../media/music/{self.track}.mp3')
        self.track_channel = pygame.mixer.Channel(self.channel)
        self.track_channel.play(self.track, loops=self.loops, maxtime=self.maxtime, fade_ms=self.fade_ms)

    def fade_out(self, mseconds):
        self.mseconds = mseconds
        self.track_channel.fadeout(self.mseconds)

    def set__volume(self, volume):
        self.volume = volume
        self.track_channel.set_volume(self.volume)

class Sound_effect:
    def __init__(self, wav, channel, wav_channel, loops, maxtime, fade_ms):
        self.wav = wav
        self.channel = channel
        self.wav_channel = wav_channel
        self.loops = loops
        self.maxtime = maxtime
        self.fade_ms = fade_ms

        self.wav = pygame.mixer.Sound(f'../media/sounds/{self.wav}.wav')
        self.wav_channel = pygame.mixer.Channel(self.channel)
        self.wav_channel.play(self.wav, loops=self.loops, maxtime=self.maxtime, fade_ms=self.fade_ms)
    
    def fade_out(self, mseconds):
        self.mseconds = mseconds
        self.wav_channel.fadeout(self.mseconds)

    def set__volume(self, volume):
        self.volume = volume
        self.wav_channel.set_volume(self.volume)