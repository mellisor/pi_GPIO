import PWM
from time import sleep
import RPi.GPIO as GPIO
import math

GPIO.setmode(GPIO.BCM)
p = PWM.PWM(25,blocking=False)
q = PWM.PWM(21,blocking=False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.output(18,1)
GPIO.output(23,0)
GPIO.output(16,1)
GPIO.output(20,0)
p.set_duty_cycle(1)
q.set_duty_cycle(1)
p.set_frequency(100)
q.set_frequency(100)
p.run()
q.run()
sleep(1)
p.stop()
q.stop()
sleep(2)
GPIO.cleanup()
