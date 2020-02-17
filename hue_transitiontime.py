#!/usr/bin/env python3

"""Sets the the Hue Lamp(s) transitiontime form 0 to 4 miliseconds."""

from hue_class import HueLamp
from termcolor import colored

hl_1 = HueLamp("F6_0A_34_1A_BC_6F", "kitchen   ")
hl_2 = HueLamp("EC_D6_5A_2D_93_CC", "livingroom")
hl_3 = HueLamp("DF_CA_54_1B_39_A8", "homeoffice")

print("\n######  Sets the the Hue Lamp(s) transitiontime form 0 to 4 miliseconds.  ######\n")

print("Lamp %s has transitiontime %s seconds." % (colored(hl_1.name, 'yellow'), colored(hl_1.transitiontime_get(), 'green')))
print("Lamp %s has transitiontime %s seconds." % (colored(hl_2.name, 'yellow'), colored(hl_2.transitiontime_get(), 'green')))
print("Lamp %s has transitiontime %s seconds." % (colored(hl_3.name, 'yellow'), colored(hl_3.transitiontime_get(), 'green')))
print()

while True:
    tra = input("Please input the transitiontime from 0 to 4 miliseconds : ")
    print()
    try:
        tra = int(tra)
        if tra in range(0, 5):
            break
        else:
            print("Value out of range.\n")
    except ValueError:
        print('"%s" is not a number. Try again.\n' % x)

while True:
    sel = input("Where to send: (k)itchen, (l)ivingroom, (h)omeoffice or (a)ll : ")
    print()
    if sel == 'k':
        hl_1.transitiontime_set(tra)
        break
    elif sel == 'kl' or sel == 'lk':
        hl_1.transitiontime_set(tra)
        hl_2.transitiontime_set(tra)
        break
    elif sel == 'l':
        hl_2.transitiontime_set(tra)
        break
    elif sel == 'lh' or sel == 'hl':
        hl_2.transitiontime_set(tra)
        hl_3.transitiontime_set(tra)
        break
    elif sel == 'h':
        hl_3.transitiontime_set(tra)
        break
    elif sel == 'hk' or sel == 'kh':
        hl_3.transitiontime_set(tra)
        hl_1.transitiontime_set(tra)
        break
    elif sel == 'a':
        hl_1.transitiontime_set(tra)
        hl_2.transitiontime_set(tra)
        hl_3.transitiontime_set(tra)
        break
    else:
        print("Please just input k, l, h or a.\n")

print("Lamp %s has transitiontime %s seconds." % (colored(hl_1.name, 'yellow'), colored(hl_1.transitiontime_get(), 'green')))
print("Lamp %s has transitiontime %s seconds." % (colored(hl_2.name, 'yellow'), colored(hl_2.transitiontime_get(), 'green')))
print("Lamp %s has transitiontime %s seconds." % (colored(hl_3.name, 'yellow'), colored(hl_3.transitiontime_get(), 'green')))

print()
