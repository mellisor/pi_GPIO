import Buzzer
from time import sleep
import json

with open('notes.json') as f:
    notes = json.load(f)
b = Buzzer.Buzzer(18)
b.set_duty_cycle(.1)
base = Buzzer.Notes['C']

for k,v in notes.items():
    print("Playing: " + str(k))
    b.playFor(v,.1)
