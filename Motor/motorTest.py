import PWM
from time import sleep
import RPi.GPIO as GPIO
import math

p = PWM.PWM(24,blocking=True)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(18,1)
GPIO.output(23,0)
GPIO.output(24,0)

freq = 10
p.set_frequency(freq)
p.set_duty_cycle(.5)
p.runFor(20)
p.stop()
