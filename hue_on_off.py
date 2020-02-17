#!/usr/bin/env python3

"""Switches Hue Lamp(s) on or off."""

from hue_class import HueLamp
from termcolor import colored

hl_1 = HueLamp("F6_0A_34_1A_BC_6F", "kitchen   ")
hl_2 = HueLamp("EC_D6_5A_2D_93_CC", "livingroom")
hl_3 = HueLamp("DF_CA_54_1B_39_A8", "homeoffice")

print("\n######  Switches Hue Lamp(s) on or off.  ######\n")

if hl_1.on_off_state() == "on":
    print("Lamp %s is %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.on_off_state(), 'green')))
elif hl_1.on_off_state() == "off":
    print("Lamp %s is %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.on_off_state(), 'red')))

if hl_2.on_off_state() == "on":
    print("Lamp %s is %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.on_off_state(), 'green')))
elif hl_2.on_off_state() == "off":
    print("Lamp %s is %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.on_off_state(), 'red')))

if hl_3.on_off_state() == "on":
    print("Lamp %s is %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.on_off_state(), 'green')))
elif hl_3.on_off_state() == "off":
    print("Lamp %s is %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.on_off_state(), 'red')))
print()
    
while True:
    x = input("on/off : ")
    print()
    if x == 'on':
        switch = 1
        break
    elif x == 'off':
        switch = 0
        break
    else:
        print("Please just input on or off.\n")

while True:
    x = input("Where to send: (k)itchen, (l)ivingroom, (h)omeoffice or (a)ll : ")
    print()
    if x == 'k':
        hl_1.on_off_switch(switch)
        break
    elif x == 'kl' or x == 'lk':
        hl_1.on_off_switch(switch)
        hl_2.on_off_switch(switch)
        break
    elif x == 'l':
        hl_2.on_off_switch(switch)
        break
    elif x == 'lh' or x == 'hl':
        hl_2.on_off_switch(switch)
        hl_3.on_off_switch(switch)
        break
    elif x == 'h':
        hl_3.on_off_switch(switch)
        break
    elif x == 'hk' or x == 'kh':
        hl_3.on_off_switch(switch)
        hl_1.on_off_switch(switch)
        break
    elif x == 'a':
        hl_1.on_off_switch(switch)
        hl_2.on_off_switch(switch)
        hl_3.on_off_switch(switch)
        break
    else:
        print("Please just input k, l, h or a.\n")

if hl_1.on_off_state() == "on":
    print("Lamp %s is %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.on_off_state(), 'green')))
elif hl_1.on_off_state() == "off":
    print("Lamp %s is %s." % (colored(hl_1.name, 'yellow'), colored(hl_1.on_off_state(), 'red')))

if hl_2.on_off_state() == "on":
    print("Lamp %s is %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.on_off_state(), 'green')))
elif hl_2.on_off_state() == "off":
    print("Lamp %s is %s." % (colored(hl_2.name, 'yellow'), colored(hl_2.on_off_state(), 'red')))

if hl_3.on_off_state() == "on":
    print("Lamp %s is %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.on_off_state(), 'green')))
elif hl_3.on_off_state() == "off":
    print("Lamp %s is %s." % (colored(hl_3.name, 'yellow'), colored(hl_3.on_off_state(), 'red')))
    
print()
