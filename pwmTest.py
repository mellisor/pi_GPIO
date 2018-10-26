import PWM
from time import sleep
import RPi.GPIO as GPIO
import math

p = PWM.PWM(18,blocking=True)

freq = 100

p.set_duty_cycle(.1)
p.set_frequency(freq)

p.run()
for a in range(800):
    cyc = math.sin(a/16.0)*.25 + .5
    p.set_duty_cycle(cyc)
    sleep(.0125)
p.stop()
