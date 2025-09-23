import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26
detector = 6

GPIO.setup(detector, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    GPIO.output(led, not GPIO.input(detector))