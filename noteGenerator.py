import Buzzer
import json

Notes = dict()

for note in Buzzer.Notes.keys():
    base = Buzzer.Notes[note]
    for a in range(8):
        Notes[note + str(a)] = base
        base = base * 2
print(Notes)
with open('notes.json','w+') as f:
    json.dump(Notes,f)
