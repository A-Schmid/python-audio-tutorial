import mido
from time import sleep

# the rtmidi backend is needed to create custom ports
mido.set_backend('mido.backends.rtmidi', load=True)

# create new virtual port
with mido.open_output('custom-midi-port', virtual=True) as p:
    # send one note over and over
    while(True):
        p.send(mido.Message('note_on', note=72))
        sleep(0.1)
        p.send(mido.Message('note_off', note=72))
        sleep(1)
