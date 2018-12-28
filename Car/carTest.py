from Car import Car
from Motor import Motor
import RPi.GPIO as GPIO
from time import sleep

# Set up GPIO
GPIO.setmode(GPIO.BCM)
rm = Motor(18,23,25)
#rm.forward_for(.5,3)
lm = Motor(16,20,21)
#lm.forward_for(.5,3)
c = Car(lm,rm)
c.right_for(.5,2)
sleep(4)
GPIO.cleanup()
