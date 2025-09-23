import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
print(leds)
gpio.setup(leds, gpio.OUT)

up, down = 9, 10
gpio.setup([up, down], gpio.IN)

num = 0

def dec2bin(n):
    return [int(element) for element in bin(n)[2:].zfill(8)]

def display(num):
    a = dec2bin(num)
    for i in range(8):
        gpio.output(leds[i], a[i])

while True:

    if gpio.input(up):
        num += 1
        if num>=2**9:
            num = 0
        display(num)
        while gpio.input(up):
            if gpio.input(down):
                num = 2**9-1
                display(num)
            time.sleep(0.01)

    if gpio.input(down):
        num = 0
        display(num)
        while gpio.input(down):
            if gpio.input(up):
                num = 2**9-1
                display(num)
            time.sleep(0.01)