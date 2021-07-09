# FluidSynth and pyFluidSynth

## Installation

Installing FluidSynth (CLI):

```
sudo apt install fluidsynth
```

Installing a sound font:

```
sudo apt install fluid-soundfont-gm
```

Installing pyFluidSynth

```
pip3 install pyfluidsynth
```

## Usage

### FluidSynth CLI

FluidSynth can be run from the command line as a standalone MIDI synthesizer.
The manpage and [official user manual](https://github.com/FluidSynth/fluidsynth/wiki/UserManual) are pretty self-explanatory so we will not go into detail here.

An example for using FluidSynth to play a MIDI file:

```
fluidsynth --audio-driver=pulseaudio --gain=1 /usr/share/sounds/sf2/FluidR3_GM.sf2 path/to/file.mid
```

### pyFluidSynth

Repository and documentation: <https://github.com/nwhitehead/pyfluidsynth>

*pyFluidSynth* is a Python module with bindings to the FluidSynth MIDI synthesizer.
Its interface provides functions based on the MIDI protocol.

Before usage, an audio driver and a sound font have to be provided to the synthesizer.
A complete list of compatible drivers can be found [here](https://www.fluidsynth.org/api/CreatingAudioDriver.html).

```
fs.start(driver='pulseaudio')
sfid = fs.sfload('/usr/share/sounds/sf2/default-GM.sf2')
```

The most important functions are `noteon(track, note, velocity)` and `noteoff(track, note)`, which invoke corresponding MIDI events at the synthesizer.
This way, sounds can be played or stopped.
By playing multiple sounds consecutively, chords can be played.

Using multiple MIDI tracks allows for playing different MIDI instruments simultaneously.
