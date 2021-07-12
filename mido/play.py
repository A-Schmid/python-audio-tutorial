import mido
from mido import MidiFile

# reads all events from a MIDI file and prints them
# but waits for the corresponding time between events
for msg in MidiFile('four_chords.mid').play():
    print(msg)
