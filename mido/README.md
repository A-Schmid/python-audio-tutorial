# MIDI Objects for Python (Mido)

Mido (short for MIDI Objects) is a Python module for reading MIDI events from input devices of files, and generating MIDI events.
The [official documentation](https://mido.readthedocs.io/en/latest/) is pretty good and provides short and useful code samples.

## Installation

Mido can be installed with pip:

```
pip3 install mido
```

However, for some advanced features (such as custom MIDI ports), the additional installation of python-rtmidi is required:

```
pip3 install python-rtmidi
```

## Usage

### Messages

The `Message` object wraps one MIDI message with the attributes `type`, `note`, `channel`, `velocity` and `time`.
Messages can be used to play and stop notes, but also for control or program changes.
A full list of supported message types can be found in the [Mido documentation](https://mido.readthedocs.io/en/latest/message_types.html).

### Input

MIDI events can be retrieved either from a connected MIDI device such as a keyboard (see *midi_device.py*) or from a MIDI file.
In both cases, Mido provides a list of MIDI events which can be iterated over.
Keep in mind that when playing back MIDI in real time (with the `play()` function) or using a MIDI device, Mido waits for new events and thus blocks the thread.
Therefore, running the playback loop in a separate thread is recommended for real time applications.

### Output

Mido can be used to write MIDI events to MIDI files.
There is a pretty good example for this in the [official documentation](https://mido.readthedocs.io/en/latest/midi_files.html).

If you want to use events generated with Mido in other programs, such as a synthesizer or a digital audio workstation (DAW), you have to send messages to a custom MIDI port.
A code example can be found in *custom_port.py*.
