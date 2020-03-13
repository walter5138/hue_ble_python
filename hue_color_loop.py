#!/usr/bin/env python3

"""Color loop."""

from time import sleep
from termcolor import colored
from hue_class import HueLamp
from hue_config import lamp_dict

for a, n in lamp_dict.items():
    globals()[n] = HueLamp(a, n)

print("\n######  Color loop.  ######\n")

red = (0x01, 0xfe, 0x00, 0x01)
yellow = (0x01, 0x7f, 0x00, 0x7f)
green = (0x01, 0x00, 0x01, 0xfe)
cyan = (0x01, 0x00, 0x7f, 0x7f)
blue = (0x01, 0x00, 0xfe, 0x01)
magenta = (0x01, 0x7f, 0x7f, 0x00)

my_colors = (red, yellow, green, cyan, blue, magenta)

it = 0
pos = 0

while it < 10:
    print("loop # %s" % it)
    pos = 0
    while pos <= 5:
        color = my_colors[pos]

        for lamp in lamp_dict.values():
            hl_obj = globals()[lamp]
            hl_obj.color_set(color)
        
            print("%s got translated in the bulb to %s!" % (colored(color, 'green'), colored(hl_obj.color_get(), 'green')))

        pos += 1

        sleep(0.4)

    it += 1

for lamp in lamp_dict.values():
    hl_obj = globals()[lamp]
    hl_obj.prop_chg_notify.kill()

print("""
How to send these values the right way?
What are these values representing?
Are those values hue and saturation or
yx values in gamut b?
What data structure is behind it?
""")
