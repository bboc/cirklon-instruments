all:
	python convert.py "Arturia MicroFreak"
	python convert.py "Dreadbox Typhon"
	python convert.py "Elektron Digitakt Kit"
	python convert.py "MFB Dominion Club"
	python convert.py "Novation Bass Station Rack"
	python convert.py "Roland Sh-01a"
	python convert.py "Sherman Filterbank 2"
	python convert.py "Waldorf Micro Q"
	python convert.py "Waldorf Streichfett"

test:
	python convert.py "Elektron Digitakt Multi"
