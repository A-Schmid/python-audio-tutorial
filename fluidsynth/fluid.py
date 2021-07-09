# example code from https://github.com/nwhitehead/pyfluidsynth

import time
import fluidsynth

fs = fluidsynth.Synth(1)

# different operating systems need different drivers
# on Linux, 'pulseaudio' is often a save bet
# on MacOS, 'portaudio' seems to work
# on Windows, select 'dsound'
fs.start(driver='pulseaudio')

# load a sound font that contains the actual audio files for the midi events
# there are many different free sound fonts available in the web
# in this case we use the default general midi sound font
sfid = fs.sfload('/usr/share/sounds/sf2/default-GM.sf2')

# select MIDI track, sound font, MIDI bank and preset
fs.program_select(0, sfid, 0, 0)

# play a C major chord
# parameters are MIDI track, note ID and velocity
fs.noteon(0, 60, 30)
fs.noteon(0, 67, 30)
fs.noteon(0, 76, 30)

time.sleep(1.0)

# stop playing the chord
# parameters are MIDI track and note ID
fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(1.0)

fs.delete()
