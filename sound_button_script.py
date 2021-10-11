import RPi.GPIO as GPIO
import time
import atexit
import subprocess
import os
import random

class SoundPlayer(object):

    def __init__(self):
        print("init")
        self.loadSounds()

    def loadSounds(self):
        self.sounds = []
        self.sound_dex = 0

        for file in os.listdir("./audio/"):
            if file.endswith(".mp3"):
                self.sounds.append(file)
        random.shuffle(self.sounds)

    def playSound(self):
        sound = self.sounds[self.sound_dex]
        subprocess.call(["omxplayer", "-o", "alsa", "audio/" + sound])
        self.sound_dex += 1
        if self.sound_dex == len(self.sounds):
            self.sound_dex = 0
            random.shuffle(self.sounds)

GPIO.setmode(GPIO.BOARD)

button_pin = 3
GPIO.setup(button_pin, GPIO.IN)

noisey_guy = SoundPlayer()


while True:
    input = GPIO.wait_for_edge(button_pin, GPIO.RISING)

    if input:
        print("pressed!")
        noisey_guy.playSound()

    time.sleep(0.1)


atexit.register(GPIO.cleanup())
