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
        if type(cycle) != float and type(cycle) != int or cycle < 0 or cycle > 1:
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
            GPIO.output(self.pin,1)
            sleep(self.on_time)
            GPIO.output(self.pin,0)
            sleep(self.off_time)
            
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
        
        
        
        
        
