import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

led = 26
#led = 13
gpio.setup(led, gpio.OUT)

#pwm = gpio.PWM(led, 20)
pwm = gpio.PWM(led, 200)
duty, d, t = 0, 1, 0.01
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(t)
    #T = 2*t*(200/d)
    duty += d
    if duty>100:
        d *= -1
        duty = 100
    if duty<0:
        d *= -1
        duty = 0