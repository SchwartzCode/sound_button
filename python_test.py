import RPi.GPIO as GPIO
import time

button_pin = 3

GPIO.setmode(GPIO.BOARD)

GPIO.setup(button_pin, GPIO.IN)

while True:
    input = GPIO.input(button_pin)
    print(input)
    time.sleep(1)


