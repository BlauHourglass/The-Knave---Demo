# class for sentences
# class for sentence breakage

import time
import pygame
import datetime

current_time = datetime.datetime.now()

pygame.init()

try:
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
        def __init__(self, audio, channel, audio_channel, loops, maxtime, fade_ms):
            self.audio = audio
            self.channel = channel
            self.audio_channel = audio_channel
            self.loops = loops
            self.maxtime = maxtime
            self.fade_ms = fade_ms

            self.audio = pygame.mixer.Sound(f'../media/sounds/{self.audio}.mp3')
            self.audio_channel = pygame.mixer.Channel(self.channel)
            self.audio_channel.play(self.audio, loops=self.loops, maxtime=self.maxtime, fade_ms=self.fade_ms)
        
        def fade_out(self, mseconds):
            self.mseconds = mseconds
            self.audio_channel.fadeout(self.mseconds)

        def set__volume(self, volume):
            self.volume = volume
            self.audio_channel.set_volume(self.volume)

except Exception as e:
	try:
		error_log = open("error_log.txt", "a")
		error_log.close()
	except:
		error_log = open("error_log.txt", "x")
		error_log.close()
	with open("error_log.txt", "a") as error_log:
		error_log.write(f"{current_time}: Misc Classes: {e}\n")
	error_message = input("\nSomething has gone wrong with the classes script. Please press \"enter\" to quit.")

except KeyboardInterrupt:
	try:
		error_log = open("error_log.txt", "a")
		error_log.close()
	except:
		error_log = open("error_log.txt", "x")
		error_log.close()
	with open("error_log.txt", "a") as error_log:
		error_log.write(f"{current_time}: Misc Classes: User has interrupted program with a keyboard shortcut.\n")
	error_message = input("\nSomething has gone wrong with the classes script. Please press \"enter\" to quit.")