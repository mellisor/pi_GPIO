import json

BaseNotes = { 'C' : 16.35, 'C#' : 17.32, 'Db' : 17.32, 'D' : 18.35, 'D#' : 19.45, 'Eb' : 19.45, 'E' : 20.6, 'F' : 21.83, 'F#' : 23.12, 'Gb' : 23.12, 'G' : 24.5, 'G#' : 25.96, 'Ab' : 25.96, 'A': 27.5, 'A#' : 29.14, 'Bb' : 29.14, 'B' : 30.87 }  

Notes = dict()
Notes[0] = 0
for note in BaseNotes.keys():
    base = BaseNotes[note]
    for a in range(8):
        Notes[note + str(a)] = base
        base = base * 2
print(Notes)
with open('notes.json','w+') as f:
    json.dump(Notes,f)
