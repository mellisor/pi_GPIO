import PWM
from time import sleep
import json

class Buzzer(PWM.PWM):
    
    def __init__(self,pin):
        PWM.PWM.__init__(self,pin,blocking= True)
        
    # Plays a note indefinitely
    def play(self,freq):
        self.set_frequency(freq)
        self.run()

    # Plays a note for a certain amount of time
    def playFor(self,freq,secs):
        if freq == 0:
            sleep(secs)
        else:
            self.set_frequency(freq)
            self.runFor(secs)
          
    # Plays a sequency of frequencies
    # seq format: ((frequency,length),...)
    def playSequence(self,seq):
        for tup in seq:
            self.playFor(tup[0],tup[1])
            
    # Loads a json file of notes, generated by noteGenerator.py
    def loadNotes(self,noteFile):
        with open(noteFile) as f:
            self.notes = json.load(f)
            
    # Plays a sequence of notes
    # seq format: (('note',length),...)
    def playNotes(self,seq):
        if not self.notes:
            print("Notes not loaded")
            return
        for tup in seq:
            self.playFor(self.notes[tup[0]],tup[1])
            
    # Plays one tick followed by a rest
    def tick(self,sec):
        self.set_frequency(100)
        self.pulse()
        sleep(sec - self.cycle_time)