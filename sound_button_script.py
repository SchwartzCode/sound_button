import RPi.GPIO as GPIO
import time
import atexit

class SoundPlayer(object):

    def __init__(self, sounds):
        print("init")
        self.sounds = sounds

    def playSound(self):
        print("should be playing a sound")

GPIO.setmode(GPIO.BOARD)

button_pin = 3
GPIO.setup(button_pin, GPIO.IN)

sounds = []

noisey_guy = SoundPlayer(sounds)


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
