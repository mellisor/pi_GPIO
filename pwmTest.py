import PWM
from time import sleep
import RPi.GPIO as GPIO

p = PWM.PWM(18,blocking=True)

freq = 300

p.set_duty_cycle(.1)
p.set_frequency(freq)

for a in range(40):
    p.runFor(.02)
    p.set_frequency(freq)
    freq+=10

sleep(.1)
GPIO.cleanup()