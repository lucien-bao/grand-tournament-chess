# simple script that uses the Inkscape CLI to render the vector
# pieces into PNG (displayable image) form
# usage: cd into the directory with the SVGs, then run this
# $ python3 path/to/this/script/conv.py
# then the PNGs will be exported to the parent directory (..)

import os

colors = ["w", "b"]
pieces = ["B", "K", "N", "R", "Q", "P"]

for c in colors:
	for p in pieces:
		os.system(f"inkscape {c}{p}.svg -w 128 -h 128 -o ../{c}{p}.png")
		
os.system(f"inkscape icon.svg -w 128 -h 128 -o ../icon.png")
