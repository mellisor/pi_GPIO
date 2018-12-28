import rospy
from geometry_msgs.msg import Twist
from CarModules import *
import RPi.GPIO as GPIO
from time import sleep
import math

# Set up GPIO
GPIO.setmode(GPIO.BCM)
rm = Motor(18,23,25)
lm = Motor(16,20,21)
c = Car(lm,rm)
c.stop()
c.forward_for(.5,1)
sleep(1.5)
GPIO.cleanup()
