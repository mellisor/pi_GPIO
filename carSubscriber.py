import rospy
from geometry_msgs.msg import Twist
from CarModules import *
import RPi.GPIO as GPIO
from time import sleep
import math
import numpy as np

class carSub(object):

    def __init__(self,car):
        self.car = car
        self.car.start_diff_drive()
        rospy.init_node('carSub',anonymous=True)
        self.sub = rospy.Subscriber('/picar/cmd_vel',Twist,self.vel_callback)
        rospy.spin()


    def vel_callback(self,msg):
        if msg.linear.x != 0.0:
            A = np.array([[1,1],[1,-1]])
            b = np.array([[2*msg.linear.x],[.14*msg.angular.z]])
            x = np.matmul(np.linalg.inv(A),b)
            vr = x[0][0]
            vl = x[1][0]
        elif msg.angular.z != 0.0:
            if msg.angular.z > 0:
                vr = .5
                vl = -.5
            else:
                vr = -.5
                vl = .5
        else:
            vl = msg.linear.x
            vr = msg.linear.x
        self.car.set_lm_speed(vl)
        self.car.set_rm_speed(vr)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
rm = Motor(18,23,25)
lm = Motor(16,20,21)
c = Car(lm,rm)
cs = carSub(c)
c.stop()
sleep(.5)
GPIO.cleanup()
