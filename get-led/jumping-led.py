import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
gpio.setup(leds, gpio.OUT)

gpio.output(leds, 0)

delay = 0.1

for i in range(10):
    for led in leds[0:len(leds)]:
        gpio.output(led, 1)
        time.sleep(delay)
        gpio.output(led, 0)
    for led in reversed(leds[1:len(leds)-1]):
        gpio.output(led, 1)
        time.sleep(delay)
        gpio.output(led, 0)