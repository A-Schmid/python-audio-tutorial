import mido

# list of all available MIDI input devices
inputs = mido.get_input_names()

# let user select a device
counter = 0
for device in inputs:
    print(f'[{counter}] {device}')
    counter += 1

selection = input('select device: ')

try:
    # listen to input from selected device and print MIDI messages
    with mido.open_input(inputs[int(selection)]) as p:
        for msg in p:
            print(msg)
except (ValueError, IndexError) as e:
    print(f'invalid device number: {selection} - must be between 0 and {len(inputs)-1}')
except KeyboardInterrupt:
    pass
