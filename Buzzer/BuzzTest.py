import Buzzer
from time import sleep
import json

with open('notes.json') as f:
    notes = json.load(f)
b = Buzzer.Buzzer(18)
b.set_duty_cycle(.1)

seq = ((notes['E4'],.5),(notes['D4'],.5),(notes['C4'],1))
b.playSequence(seq)

b.loadNotes('notes.json')
seq = (('E4',.5),('D4',.5),('C4',1),('B3',1))
b.playNotes(seq)


