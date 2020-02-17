#!/usr/bin/env python3

"""Sets the color of the Hue Lamp(s)."""

import time
from hue_class import HueLamp
from termcolor import colored

hl_1 = HueLamp("F6_0A_34_1A_BC_6F", "kitchen   ")
hl_2 = HueLamp("EC_D6_5A_2D_93_CC", "livingroom")
hl_3 = HueLamp("DF_CA_54_1B_39_A8", "homeoffice")

print("\n######  Sets the color of the Hue Lamp(s). ######\n")

print("Lamp %s has color %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.color_get(), 'green')))
print("Lamp %s has color %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.color_get(), 'green')))
print("Lamp %s has color %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.color_get(), 'green')))
print()

while True:
    x = input("Please input one color: (w)hite, (r)ed, (y)ellow, (g)reen, (c)yan, (b)lue, (m)agenta: ")
    print()
    if x == "white" or x == "w":
        col = (0x01, 0x55, 0x55, 0x55)
        break
    elif x == "red" or x == "r":
        col = (0x01, 0xfe, 0x00, 0x01)
        break
    elif x == "green" or x == "g":
        col = (0x01, 0x00, 0x01, 0xfe)
        break
    elif x == "blue" or x == "b":
        col = (0x01, 0x00, 0xfe, 0x01)
        break
    elif x == "yellow" or x == "y":
        col = (0x01, 0x7f, 0x00, 0x7f)
        break
    elif x == "cyan" or x == "c":
        col = (0x01, 0x00, 0x7f, 0x7f)
        break
    elif x == "magenta" or x == "m":
        col = (0x01, 0x7f, 0x7f, 0x00)
        break
    else:
        print("Wrong input!\n")

while True:
    sel = input("Where to send: (k)itchen, (l)ivingroom, (h)omeoffice or (a)ll : ")
    print()
    if sel == 'k':
        hl_1.color_set(col)
        break
    elif sel == 'kl' or sel == 'lk':
        hl_1.color_set(col)
        hl_2.color_set(col)
        break
    elif sel == 'l':
        hl_2.color_set(col)
        break
    elif sel == 'lh' or sel == 'hl':
        hl_2.color_set(col)
        hl_3.color_set(col)
        break
    elif sel == 'h':
        hl_3.color_set(col)
        break
    elif sel == 'hk' or sel == 'kh':
        hl_3.color_set(col)
        hl_1.color_set(col)
        break
    elif sel == 'a':
        hl_1.color_set(col)
        hl_2.color_set(col)
        hl_3.color_set(col)
        break
    else:
        print("Please just input k, l, h or a.\n")

time.sleep(0.4)   # if transitiontime is long values needs time to settle.

print("Lamp %s has color %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.color_get(), 'green')))
print("Lamp %s has color %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.color_get(), 'green')))
print("Lamp %s has color %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.color_get(), 'green')))

print()
