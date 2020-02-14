#!/usr/bin/env python3

"""Sets the the Hue Lamp(s) transitiontime form 0 to 4 miliseconds."""

from hue_class import HueLamp
from termcolor import colored

hl_1 = HueLamp("F6_0A_34_1A_BC_6F", "kitchen   ")
hl_2 = HueLamp("EC_D6_5A_2D_93_CC", "livingroom")
hl_3 = HueLamp("DF_CA_54_1B_39_A8", "homeoffice")

print("Lamp %s has transitiontime %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.transitiontime_get(), 'green')))
print("Lamp %s has transitiontime %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.transitiontime_get(), 'green')))
print("Lamp %s has transitiontime %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.transitiontime_get(), 'green')))

while True:
    x = input("Please input the transitiontime from 0 to 4 miliseconds : ")
    try:
        y = int(x)
        if y in range(0, 5):
            trans = y
            break
        else:
            print("Value out of range.")
    except ValueError:
        print('"%s" is not a number. Try again.' % x)

while True:
    x = input("Where to send: (k)itchen, (l)ivingroom, (h)omeoffice or (a)ll : ")
    if x == 'k':
        hl_1.transitiontime_set(trans)
        break
    elif x == 'kl' or x == 'lk':
        hl_1.transitiontime_set(trans)
        hl_2.transitiontime_set(trans)
        break
    elif x == 'l':
        hl_2.transitiontime_set(trans)
        break
    elif x == 'lh' or x == 'hl':
        hl_2.transitiontime_set(trans)
        hl_3.transitiontime_set(trans)
        break
    elif x == 'h':
        hl_3.transitiontime_set(trans)
        break
    elif x == 'hk' or x == 'kh':
        hl_3.transitiontime_set(trans)
        hl_1.transitiontime_set(trans)
        break
    elif x == 'a':
        hl_1.transitiontime_set(trans)
        hl_2.transitiontime_set(trans)
        hl_3.transitiontime_set(trans)
        break
    else:
        print("Please just input k, l, h or a.")

print("Lamp %s has transitiontime %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.transitiontime_get(), 'green')))
print("Lamp %s has transitiontime %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.transitiontime_get(), 'green')))
print("Lamp %s has transitiontime %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.transitiontime_get(), 'green')))

