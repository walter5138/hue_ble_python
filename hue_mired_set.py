#!/usr/bin/env python3

"""Sets the mired of the Hue Lamp(s)."""

import time
from hue_class import HueLamp
from termcolor import colored

hl_1 = HueLamp("F6_0A_34_1A_BC_6F", "kitchen   ")
hl_2 = HueLamp("EC_D6_5A_2D_93_CC", "livingroom")
hl_3 = HueLamp("DF_CA_54_1B_39_A8", "homeoffice")

print("\n######  Sets the mired of the Hue Lamp(s).  ######\n")

print("Lamp %s has mired %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.mired_get(), 'green')))
print("Lamp %s has mired %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.mired_get(), 'green')))
print("Lamp %s has mired %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.mired_get(), 'green')))
print()

while True:
    x = input("Please input color temerature in mired from 153 (cold light) to 500 (warm light) : ")
    print()
    try:
        bri = int(x)
        if bri in range(153, 501):
            break
        else:
            print("Value out of range.\n")
    except ValueError:
        print('"%s" is not a number. Try again.\n' % x)

while True:
    x = input("Where to send: (k)itchen, (l)ivingroom, (h)omeoffice or (a)ll : ")
    print()
    if x == 'k':
        hl_1.mired_set(bri)
        time.sleep(hl_1.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_1.name, 'yellow'), colored(hl_1.mired_get(), 'green'),  colored(hl_1.transitiontime_get(), 'green')))
        break
    elif x == 'kl' or x == 'lk':
        hl_1.mired_set(bri)
        hl_2.mired_set(bri)
        time.sleep(hl_1.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_1.name, 'yellow'), colored(hl_1.mired_get(), 'green'),  colored(hl_1.transitiontime_get(), 'green')))
        time.sleep(hl_2.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_2.name, 'yellow'), colored(hl_2.mired_get(), 'green'),  colored(hl_2.transitiontime_get(), 'green')))
        break
    elif x == 'l':
        hl_2.mired_set(bri)
        time.sleep(hl_2.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_2.name, 'yellow'), colored(hl_2.mired_get(), 'green'),  colored(hl_2.transitiontime_get(), 'green')))
        break
    elif x == 'lh' or x == 'hl':
        hl_2.mired_set(bri)
        hl_3.mired_set(bri)
        time.sleep(hl_2.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_2.name, 'yellow'), colored(hl_2.mired_get(), 'green'),  colored(hl_2.transitiontime_get(), 'green')))
        time.sleep(hl_3.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_3.name, 'yellow'), colored(hl_3.mired_get(), 'green'),  colored(hl_3.transitiontime_get(), 'green')))
        break
    elif x == 'h':
        hl_3.mired_set(bri)
        time.sleep(hl_3.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_3.name, 'yellow'), colored(hl_3.mired_get(), 'green'),  colored(hl_3.transitiontime_get(), 'green')))
        break
    elif x == 'hk' or x == 'kh':
        hl_1.mired_set(bri)
        hl_3.mired_set(bri)
        time.sleep(hl_1.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_1.name, 'yellow'), colored(hl_1.mired_get(), 'green'),  colored(hl_1.transitiontime_get(), 'green')))
        time.sleep(hl_3.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_3.name, 'yellow'), colored(hl_3.mired_get(), 'green'),  colored(hl_3.transitiontime_get(), 'green')))
        break
    elif x == 'a':
        hl_1.mired_set(bri)
        hl_2.mired_set(bri)
        hl_3.mired_set(bri)
        time.sleep(hl_1.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_1.name, 'yellow'), colored(hl_1.mired_get(), 'green'),  colored(hl_1.transitiontime_get(), 'green')))
        time.sleep(hl_2.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_2.name, 'yellow'), colored(hl_2.mired_get(), 'green'),  colored(hl_2.transitiontime_get(), 'green')))
        time.sleep(hl_3.transitiontime_get())   # if transitiontime is long values needs time to settle.
        print("Lamp %s got mired %s in %s seconds." % (colored(hl_3.name, 'yellow'), colored(hl_3.mired_get(), 'green'),  colored(hl_3.transitiontime_get(), 'green')))
        break
    else:
        print("Please just input k, l, h or a.\n")
print()

