import mido
from mido import MidiFile

# reads all events from a MIDI file and prints them
for msg in MidiFile('four_chords.mid'):
    print(msg)
