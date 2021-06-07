# Circlon Instruments

Several instrument definitions for Sequentix Cirklon. 

Since the CKI files are JSON and contain a large amount of formatting and duplicate information, instruments are defined in a simple YAML file and then the JSON is generated via a python script. 

To facilitate transformation of existing scripts, a converter from JSON to YAML is included in the script.

## CKI Format

(see dummy.yaml for more documentation)

- NRPN is not possible
- Intrument Names are 9 characters max.


## Pararameter Naming Conventions

The Circlon supports a maximum of six characters for parameter names, but even a simple synth comes with 40 controllable parameters, and people have more than one device, so consistent naming conventions that make effective use of the 6 characters would be a really nice thing to have.

There's no "correct" or perfect way for doing this, and consistency beats personal preference. I'll develop these naming conventions incrementally for the devices I own, since that's my use case. Until then, this documentation will change quite a bit

I assume the circlon will support [ASCII characters 32-127](http://asciiset.com/), so there's quite a few characters besides letters and numbers that can be used, some characters might serve as visual representations of building blocks of (virtual) analog synthesizers.

All parameter names will be in [Camel case](https://en.wikipedia.org/wiki/Camel_case) (or dromedary case, to be more specific) to avoid abiguities and increase Readability.

- Oscillator: 'o', 'o1'
- Suboscillator: 'su'
- Level
- Modulation Intensity
- Envelope: '^', '^1'
- LFO: '~', '~1'
- Noise: 'Nz'
- Depth (=Intensity): 'Dp'
- Mode 'Md'
- Type: 'Ty'



## Interesting Links

- [Circlon Instruments Editor](https://github.com/samdoshi/cirklon-instrument-editor)
- [Python utilities for the Sequentix Cirklon sequencer](https://github.com/pmagwene/cirklon.py)
- [Circlon very basic workflow](https://www.youtube.com/watch?v=RwFpTG3lyeg&t=259s)
- [Circlon Deep Dive Videos](https://www.youtube.com/playlist?list=PLt3aGCjETwhtagrA6bAcvMxqo3SCnrvB0)
