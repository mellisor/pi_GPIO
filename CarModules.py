#!/usr/bin/env python3
import RPi.GPIO as GPIO
from threading import Thread
from threading import Lock
from time import sleep

class PWM(object):
    
    def __init__(self,pin,duty_cycle=.5,frequency=100.0,blocking=False):
        # Lock for timer function
        self.l = Lock()
        # GPIO pin to use
        self.pin = pin
        # Set up GPIO
        GPIO.setup(pin,GPIO.OUT)
        # Sets up duty cycle and frequency
        self.set_duty_cycle(duty_cycle,update=False)
        self.set_frequency(frequency)
        # Off by default
        self.on = False
        # Whether 'runFor' calls should block program execution
        self.blocking = blocking
    
    # Updates duty cycle
    def set_duty_cycle(self,cycle,update=True):
        if cycle < 0 or cycle > 1:
            raise ValueError("Duty cycle must be a number between 0 and 1")
        self.duty_cycle = cycle
        if update:
            self.__set_cycle_time()
        
    # Updates frequency
    def set_frequency(self,freq,update=True):
        if type(freq) != float and type(freq) != int or freq < 0:
            raise ValueError("Frequency must be a positive number")
        self.frequency = freq
        if update:
            self.__set_cycle_time()
        
    # Updates cycle time
    def __set_cycle_time(self):
        if self.duty_cycle == 0:
            self.cycle_time = self.off_time = .01
            self.on_time = 0
        elif self.frequency == 0:
            self.cycle_time = self.on_time = .01
            self.off_time = 0
        else:
            self.cycle_time = 1.0/self.frequency
            self.on_time = self.cycle_time * self.duty_cycle
            self.off_time = self.cycle_time - self.on_time
        
    # PWM Function
    # Multiple instances run concurrently
    def __go(self):
        while self.on:
            while self.on_time > 0 and self.on:
                GPIO.output(self.pin,1)
                sleep(self.on_time)
                GPIO.output(self.pin,0)
                sleep(self.off_time)
            sleep(.01)
            
    # Sets a timer, turn off after 'secs' seconds
    def __timer(self,secs):
        self.l.acquire()
        if self.frequency > 0 and self.duty_cycle > 0:
            self.on = True
        self.thr = Thread(target=self.__go)
        self.thr.start()
        sleep(secs)
        self.on = False
        self.l.release()
    
    # Runs indefinitely
    # Multiple instances run concurrently, not recommended to do so
    def run(self):
        self.on = True
        self.thr = Thread(target=self.__go)
        self.thr.start()
        
    # Runs for a certain amount of time
    # Multiple instances run sequentially
    # If the frequency or duty cycle need to be updated between calls, blocking should be set to True
    def runFor(self,secs):
        if self.blocking:
            self.__timer(secs)
        else:
            self.tim = Thread(target=self.__timer,args=(secs,))
            self.tim.start()
    
    # Stops the pwm pin
    def stop(self):
        self.on = False
        
    # Send one pulse
    def pulse(self):
        GPIO.output(self.pin,1)
        sleep(self.on_time)
        GPIO.output(self.pin,0)
        sleep(self.off_time)

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

    def stop(self):
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

    def set_speed(self,speed):
        self.pwm_pin.set_duty_cycle(speed)

    def run(self,speed):
        self.set_speed(speed)
        self.pwm_pin.run()

class Car(object):

    def __init__(self,lm,rm):
        self.left_motor = lm
        self.right_motor = rm

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

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

    def start_diff_drive(self):
        self.left_motor.run(0)
        self.right_motor.run(0)

    def stop_diff_drive(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def set_lm_speed(self,speed):
        if speed > 0:
            self.left_motor.set_forward()
        else:
            self.left_motor.set_backward()
            speed = -1*speed
        self.left_motor.set_speed(speed)

    def set_rm_speed(self,speed):
        if speed > 0:
            self.right_motor.set_forward()
        else:
            self.right_motor.set_backward()
            speed = -1*speed
        self.right_motor.set_speed(speed)

