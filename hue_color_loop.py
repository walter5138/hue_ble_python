#!/usr/bin/env python3

"""Color loop."""

from time import sleep
from hue_class import HueLamp
from termcolor import colored

hl_1 = HueLamp("F6_0A_34_1A_BC_6F", "kitchen   ")
hl_2 = HueLamp("EC_D6_5A_2D_93_CC", "livingroom")
hl_3 = HueLamp("DF_CA_54_1B_39_A8", "homeoffice")

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
t = 2
while it < 2:
    print("loop number %s." % it)
    pos = 0
    while pos <= 5:
        color = my_colors[pos]

        hl_1.color_set(color)
        hl_2.color_set(color)
        hl_3.color_set(color)
        
        sleep(1)
        
        print("%s got translated in the bulb in %s!" % (colored(color, 'green'), colored(hl_1.color_get(), 'green')))
        print("%s got translated in the bulb in %s!" % (colored(color, 'green'), colored(hl_1.color_get(), 'green')))
        print("%s got translated in the bulb in %s!" % (colored(color, 'green'), colored(hl_1.color_get(), 'green')))

        pos += 1

        #sleep(1)

    it += 1

print("\nHow to send these values the right way?\nWhat are these values representing?\nAre those values hue and saturation or\nyx values in gamut b?\nWhat data structure is behind it?\n")
