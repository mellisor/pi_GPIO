import Buzzer
from time import sleep
import json

with open('notes.json') as f:
    notes = json.load(f)
b = Buzzer.Buzzer(18)
b.set_duty_cycle(.3)

#seq = ((notes['E4'],.5),(notes['D4'],.5),(notes['C4'],1))
#b.playSequence(seq)

b.loadNotes('notes.json')
seq = (('B3',.5),('C#4',.25),('D4',1),('C#4',.5),('D4',.5),('A3',.5),('D4',.75),('E4',.25),('F#4',.5),('E4',.5),('D4',.5),('B3',.5),('C#4',2))
b.playNotes(seq)


