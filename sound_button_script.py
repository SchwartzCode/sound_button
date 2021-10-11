import RPi.GPIO as GPIO
import time
import atexit
import subprocess
import os

class SoundPlayer(object):

    def __init__(self):
        print("init")
        self.loadSounds()

    def loadSounds(self):
        self.sounds = []
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                self.sounds.append(file)

    def playSound(self):
        print("should be playing a sound")
        subprocess.call(["omxplayer", "-o", "alsa", "test_sound.mp3"])

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


# while True:
#     input = GPIO.input(button_pin)
#     print(input)
#     time.sleep(1)

atexit.register(GPIO.cleanup())
