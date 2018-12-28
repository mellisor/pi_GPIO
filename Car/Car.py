from PWM import PWM
from Motor import Motor

class Car(object):

    def __init__(self,lm,rm):
        self.left_motor = lm
        self.right_motor = rm

    def forward(self,speed):
        self.left_motor.forward(speed)
        self.right_motor.forward(speed)

    def forward_for(self,speed,time):
        self.left_motor.forward_for(speed,time)
        self.right_motor.forward_for(speed,time)

    def backward(self,speed):
        self.left_motor.backward(speed)
        self.right_motor.backward(speed)

    def backward_for(self,speed,time):
        self.left_motor.backward_for(speed,time)
        self.right_motor.backward_for(speed,time)

    def left(self,speed):
        self.left_motor.backward(speed)
        self.right_motor.forward(speed)

    def left_for(self,speed,time):
        self.left_motor.backward_for(speed,time)
        self.right_motor.forward_for(speed,time)

    def right(self,speed):
        self.left_motor.forward(speed)
        self.right_motor.backward(speed)

    def right_for(self,speed,time):
        self.left_motor.forward_for(speed,time)
        self.right_motor.backward_for(speed,time)
