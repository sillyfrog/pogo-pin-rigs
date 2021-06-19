#!/usr/bin/env python3
from solid import *
from solid.utils import *
import pathlib
import math

SPACING = 2.54
WALL = 1.5
HEIGHT = 35
FLOOR = 2

PIN_D = 1.2
PIN_L = 16.5

COUNT = 5


def main():
    width = (COUNT - 1) * SPACING + WALL * 2
    o = cube([width, WALL * 2 + PIN_D, HEIGHT])
    o -= translate([-0.1, -0.1, FLOOR + 0.5])(
        cube([width + 0.2, WALL + PIN_D + 0.1, PIN_L - 5.0 - FLOOR])
    )
    for i in range(COUNT):
        o -= translate([WALL + SPACING * i, WALL + PIN_D / 2 - 0.2, -4])(
            cylinder(d=PIN_D, h=PIN_L)
        )

    # Print on it's back
    o = rotate([-90, 0, 90])(o)
    saveasscad(o)


def saveasscad(obj, extra=""):
    fn = pathlib.Path(__file__)
    outfn = fn.parent / (fn.stem + extra + ".scad")
    scad_render_to_file(obj, outfn, file_header="$fn = 50;\n")


if __name__ == "__main__":
    main()
