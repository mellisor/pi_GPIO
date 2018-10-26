import PWM
from time import sleep

Notes = { 'C' : 16.35, 'C#' : 17.32, 'Db' : 17.32, 'D' : 18.35, 'D#' : 19.45, 'Eb' : 19.45, 'E' : 20.6, 'F' : 21.83, 'F#' : 23.12, 'Gb' : 23.12, 'G' : 24.5, 'G#' : 25.96, 'Ab' : 25.96, 'A': 27.5, 'A#' : 29.14, 'Bb' : 29.14, 'B' : 30.87 }  

class Buzzer(object):
    
    def __init__(self,pin):
        
        self.p = PWM.PWM(pin,blocking = True)
        self.pin = pin
        
    def play(self,freq):
        self.p.set_frequency(freq)
        self.p.run()
        
    def stop(self):
        self.p.stop()
        
    def playFor(self,freq,secs):
        self.p.set_frequency(freq)
        self.p.runFor(secs)
        
    def set_duty_cycle(self,cycle):
        self.p.set_duty_cycle(cycle)