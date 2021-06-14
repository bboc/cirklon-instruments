# Circlon Instruments

Several instrument definitions for Sequentix Cirklon. 

Since the CKI files are JSON and contain a large amount of formatting and duplicate information, instruments are defined in a simple YAML file and then the JSON is generated via a python script. 

To facilitate transformation of existing scripts, a converter from JSON to YAML is included in the script.


## Download the Instruments

[Download a ZIP file](https://downgit.github.io/#/home?url=https://github.com/bboc/cirklon-instruments/blob/main/instruments.cki) that contains the following instruments:

* Arturia MicroFreak.cki (alpha)
* Dreadbox Typhon.cki (alpha)
* Elektron Digitakt Kit (inkluding FX Control) (alpha)
* Elektron Digitakt Multi (full parameter set for each sound) (alpha)
* MFB Dominion Club.cki (beta)
* Novation Bass Station Rack.cki (alpha)
* Roland Sh-01a.cki (beta)
* Sherman Filterbank 2.cki (alpha)
* Waldorf Micro Q.cki (alpha)
* Waldorf Streichfett.cki (beta)

The ZIP file always contains the latest version of any instrument.

## CKI Format

(see file-format.yaml, a documented example of the file format)

- NRPN is not possible (yet)
- Intrument names are 9 characters max.
- Parameter names are 6 characters max.


## Pararameter Naming Conventions

The Circlon supports a maximum of six characters for parameter names, but even a simple synth comes with 40 controllable parameters, and people have more than one device, so consistent naming conventions that make effective use of the 6 characters would be a really nice thing to have.

There's no "correct" or perfect way for doing this, and consistency beats personal preference. I'll develop these naming conventions incrementally for the devices I own, since that's my use case. Until then, this documentation will change quite a bit

I assume the circlon will support [ASCII characters 32-127](http://asciiset.com/), so there's quite a few characters besides letters and numbers that can be used, some characters might serve as visual representations of building blocks of (virtual) analog synthesizers.

All parameter names will be in [Camel case](https://en.wikipedia.org/wiki/Camel_case) (or dromedary case, to be more specific) to avoid abiguities and increase Readability.

- Oscillator: 'o', 'o1'
- Suboscillator: 'su'
- Level: 'Lv' or 'Lvl'
- Envelope: '^', '^1'
- LFO: '~', '~1'
- Noise: 'Nz'
- Depth (=Intensity): 'Dp'
- Mode 'Md'
- Type: 'Ty'
- Interval: 'Int' (or Ivl?)


## Interesting Links

### Other CKI resources

- [Circlon Instruments Editor](https://github.com/samdoshi/cirklon-instrument-editor)
- [Python utilities for the Sequentix Cirklon sequencer](https://github.com/pmagwene/cirklon.py)

### Tutorial Videos

- [Circlon very basic workflow](https://www.youtube.com/watch?v=RwFpTG3lyeg&t=259s)
- [Cirklon Informational Video Messages](https://www.youtube.com/playlist?list=PLNEW7foH6qsAozs9VJoUlg7D7XMJvmpGX)
- [Circlon Deep Dive Videos](https://www.youtube.com/playlist?list=PLt3aGCjETwhtagrA6bAcvMxqo3SCnrvB0)

### Other Information

- [How to generate Euclidean rhythm patterns in Cirklon](http://forum.sequentix.com/viewtopic.php?f=5&t=3327&p=21568&hilit=Generative#p21568)
- [evolving random sequences](http://forum.sequentix.com/viewtopic.php?f=5&t=2591&sid=72243ac7761a0d3b1da73b3afbe357a4)


