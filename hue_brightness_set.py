#!/usr/bin/env python3

"""Sets the brightness of the Hue Lamp(s)."""
import time
from hue_class import HueLamp
from termcolor import colored

hl_1 = HueLamp("F6_0A_34_1A_BC_6F", "kitchen   ")
hl_2 = HueLamp("EC_D6_5A_2D_93_CC", "livingroom")
hl_3 = HueLamp("DF_CA_54_1B_39_A8", "homeoffice")

print("Lamp %s has brightness %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.brightness_get(), 'green')))
print("Lamp %s has brightness %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.brightness_get(), 'green')))
print("Lamp %s has brightness %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.brightness_get(), 'green')))

while True:
    x = input("Please input the brightness from 1 to 254 : ")
    try:
        y = int(x)
        if y in range(1, 255):
            bri = y
            break
        else:
            print("Value out of range.")
    except ValueError:
        print('"%s" is not a number. Try again.' % x)

while True:
    x = input("Where to send: (k)itchen, (l)ivingroom, (h)omeoffice or (a)ll : ")
    if x == 'k':
        hl_1.brightness_set(bri)
        break
    elif x == 'kl' or x == 'lk':
        hl_1.brightness_set(bri)
        hl_2.brightness_set(bri)
        break
    elif x == 'l':
        hl_2.brightness_set(bri)
        break
    elif x == 'lh' or x == 'hl':
        hl_2.brightness_set(bri)
        hl_3.brightness_set(bri)
        break
    elif x == 'h':
        hl_3.brightness_set(bri)
        break
    elif x == 'hk' or x == 'kh':
        hl_3.brightness_set(bri)
        hl_1.brightness_set(bri)
        break
    elif x == 'a':
        hl_1.brightness_set(bri)
        hl_2.brightness_set(bri)
        hl_3.brightness_set(bri)
        break
    else:
        print("Please just input k, l, h or a.")

time.sleep(0.5)   # if transitiontime is short values needs time to settle.

print("Lamp %s has brightness %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.brightness_get(), 'green')))
print("Lamp %s has brightness %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.brightness_get(), 'green')))
print("Lamp %s has brightness %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.brightness_get(), 'green')))

