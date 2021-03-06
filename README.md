# python-audio-tutorial

Small overview over different methods for playing audio with Python.

## Table of contents

If your goal is to simply play an audio file, have a look at the *playsound* directory.

If you want to build a more sophisticated media player, check out the *QtMultimedia* directory.

If you want to use MIDI to play sounds, you might want to use *fluidsynth*.

If you want to work with MIDI events, *Mido* does everything you want.

# MIDI

The MIDI protocol is used by both digitial instruments and synthesizers to send and receive note and control messages.
MIDI controllers (e.g. a digital piano) only send information about *which* note is played and *how* it is played - interpretation and actual sound generation are handled by a synthesizer.
MIDI events can also be generated by computer programs, for example the [Mido Python module](https://mido.readthedocs.io/en/latest/).

MIDI provides multiple tracks so different instruments can be played simultaneously.
The actual sounds which are played by the synthesizer are stored in a *sound font* which contains sounds for different instruments.

*General MIDI* is a MIDI standard and defines things like the number of different channels, but also the program numbers for different instruments.
For example, MIDI channel 10 is always reserved for percussion and MIDI instrument 1 is always the "Acoustic Grand Piano".

# Further Reading

Tutorial on the MIDI protocol: <https://www.cs.cmu.edu/~music/cmsip/readings/MIDI%20tutorial%20for%20programmers.html>

Lecture slides on the MIDI protocol: <https://www.eecs.umich.edu/courses/eecs373/Lec/StudentF18/MIDI%20Presentation.pdf>

Overview over general MIDI instruments: <https://en.wikipedia.org/wiki/General_MIDI>

Overview over MIDI events: <https://www.mixagesoftware.com/en/midikit/help/HTML/midi_events.html>

Overview over MIDI controller events: <https://www.mixagesoftware.com/en/midikit/help/HTML/controllers.html>

Mapping of MIDI notes, actual notes and frequencies: <http://newt.phys.unsw.edu.au/jw/notes.html>
