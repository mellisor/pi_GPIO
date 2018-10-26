import PWM
from time import sleep
import RPi.GPIO as GPIO
import math

p = PWM.PWM(18,blocking=True)

freq = 300

p.set_duty_cycle(.1)
p.set_frequency(freq)

p.run()
for a in range(100):
    freq = math.sin(a)*50 + 500
    p.set_frequency(freq)
    print(freq)
    sleep(.1)
p.stop()
