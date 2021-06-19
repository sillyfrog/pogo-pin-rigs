#!/usr/bin/env python3

FLASH_PINS = [1, 3, 5, 6, 7, 15]

from solid import *
from solid.utils import *
import pathlib
import math

WIDTH = 16.6
DEPTH = 1.1
PAD_SPACING = 14.14 / 7
WALL = 1

# This is the pin diameter to print in mm.
# Pins are 1.3mm standard, but depending on printer this may need to be smaller or larger.
PIN_D = 1.3
PIN_L = 16.5


def main():
    trim = 0.5
    o = translate([0, 0, trim])(cube([WIDTH + WALL * 2, 10, 8 - trim]))
    o -= translate([WALL, (10 - DEPTH) / 2, -0.1])(cube([WIDTH, DEPTH, 5]))

    o += translate([0, 0, 16])(cube([WIDTH + WALL * 2, 10, 4]))
    midwidth = 2
    o += translate([0, 0, 8])(
        rotate([90, 0, 90])(
            linear_extrude(WIDTH + WALL * 2)(
                polygon(
                    [
                        [0, 0],
                        [(10 - midwidth) / 2, 4],
                        [0, 8],
                        [10, 8],
                        [(10 + midwidth) / 2, 4],
                        [10, 0],
                    ]
                )
            )
        )
    )

    o -= translate([WALL + 0.5, -1, -0.1])(cube([WIDTH - 1, 12, 4]))
    apadsstart = (WIDTH - (7 * PAD_SPACING)) / 2
    apads = [i * PAD_SPACING + apadsstart for i in range(8)]
    bpadsstart = (WIDTH - (6 * PAD_SPACING)) / 2
    bpads = [i * PAD_SPACING + bpadsstart for i in range(7)]

    pin = 15
    for pad in apads:
        if pin in (FLASH_PINS):
            o -= ~translate([WALL + pad, 3.5, -0.1])(
                rotate([10, 0, 0])(cylinder(d=PIN_D, h=PIN_L))
            )
        pin -= 2
    pin = 14
    for pad in bpads:
        if pin in (FLASH_PINS):
            o -= ~translate([WALL + pad, 10 - 3.5, -0.1])(
                rotate([-10, 0, 0])(cylinder(d=PIN_D, h=PIN_L))
            )
        pin -= 2

    # Rotate the final object for printing
    o = rotate([180, 0, 0])(o)

    saveasscad(o)


def saveasscad(obj, extra=""):
    fn = pathlib.Path(__file__)
    outfn = fn.parent / (fn.stem + extra + ".scad")
    scad_render_to_file(obj, outfn, file_header="$fn = 50;\n")


if __name__ == "__main__":
    main()
