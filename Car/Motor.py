from PWM import PWM
from time import sleep
import RPi.GPIO as GPIO

class Motor(object):

    def __init__(self,fwd,bwd,pwm):
        self.fwd_pin = fwd
        self.bwd_pin = bwd
        self.pwm_pin = PWM(pwm,blocking=False)
        GPIO.setup(self.fwd_pin,GPIO.OUT)
        GPIO.setup(self.bwd_pin,GPIO.OUT)

    def set_forward(self):
        GPIO.output(self.fwd_pin,1)
        GPIO.output(self.bwd_pin,0)

    def set_backward(self):
        GPIO.output(self.fwd_pin,0)
        GPIO.output(self.bwd_pin,1)

    def stop():
        self.pwm_pin.stop()

    def forward(self,speed):
        self.set_forward()
        self.pwm_pin.set_duty_cycle(speed)
        self.pwm_pin.run()

    def forward_for(self,speed,time):
        self.set_forward()
        self.pwm_pin.set_duty_cycle(speed)
        self.pwm_pin.runFor(time)

    def backward(self,speed):
        self.set_backward()
        self.pwm_pin.set_duty_cycle(speed)
        self.pwm_pin.run()

    def backward_for(self,speed,time):
        self.set_backward()
        self.pwm_pin.set_duty_cycle(speed)
        self.pwm_pin.runFor(time)

    
