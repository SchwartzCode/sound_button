import RPi.GPIO as GPIO
import time
import atexit
import subprocess
import os
import random
import signal

class SoundPlayer(object):

    def __init__(self):
        print("init")
        self.loadSounds()
        self.audio = None

        self.audio = subprocess.Popen(["omxplayer", "-o", "alsa", "audio/buzzer.mp3"], preexec_fn=os.setsid)

    def loadSounds(self):
        self.sounds = []
        self.sound_dex = 0

        for file in os.listdir("./audio/"):
            if file.endswith(".mp3"):
                self.sounds.append(file)
        random.shuffle(self.sounds)

    def playSound(self):
        if self.audio is not None:
            os.killpg(os.getpgid(self.audio.pid), signal.SIGTERM)
            self.audio = None
            print("killing...")

        self.audio = subprocess.Popen(["omxplayer", "-o", "alsa", "audio/" + self.sounds[self.sound_dex]], preexec_fn=os.setsid)
        self.sound_dex += 1

        if self.sound_dex == len(self.sounds):
            self.sound_dex = 0
            random.shuffle(self.sounds)

if __name__ == "__main__":
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
    atexit.register(os.killpg(os.getgpid(noisey_guy.audio.pid), signal.SIGTERM))


atexit.register(GPIO.cleanup())
