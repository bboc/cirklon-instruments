all:
	python convert.py "Arturia MicroFreak"
	python convert.py "Dreadbox Typhon"
	python convert.py "Elektron Digitakt Kit"
	python convert.py "Elektron Digitakt Multi"
	python convert.py "MFB Dominion Club"
	python convert.py "Novation Bass Station Rack"
	python convert.py "Roland Sh-01a"
	python convert.py "Roland Boutique A-01"
	python convert.py "Sherman Filterbank 2"
	python convert.py "Waldorf Micro Q"
	python convert.py "Waldorf Streichfett"

mine:
	mv instruments.cki instruments.bak
	mv my-instruments instruments.cki

	python convert.py "Arturia MicroFreak" 1 15
	python convert.py "Dreadbox Typhon" 1 11
	python convert.py "Elektron Digitakt Kit" 4 10
	python convert.py "Elektron Digitakt Multi" 4 1
	python convert.py "MFB Dominion Club" 1 14
	python convert.py "Novation Bass Station Rack" 1 11
	python convert.py "Roland Sh-01a" 1 12
	python convert.py "Roland Boutique A-01" 1 8
	python convert.py "Sherman Filterbank 2" 2 16
	python convert.py "Waldorf Micro Q" 1 1
	python convert.py "Waldorf Streichfett" 1 16

	mv instruments.cki my-instruments
	mv instruments.bak instruments.cki

setup:
	mkdir instruments.cki
	mkdir my-instruments

test:
	python convert.py "Roland Boutique A-01"
