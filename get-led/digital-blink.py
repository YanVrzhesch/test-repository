import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

state, period = 0, 1

while True:
    GPIO.output(led, state)
    print(state)
    state = not state
    time.sleep(period/2)