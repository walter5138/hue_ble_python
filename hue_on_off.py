#!/usr/bin/env python3

"""Switches Hue Lamp(s) on or off."""

from termcolor import colored
from hue_class import HueLamp
from hue_config import lamp_dict

for a, n in lamp_dict.items():
    globals()[n] = HueLamp(a, n)

print("\n######  Switches Hue Lamp(s) on or off.  ######\n")

for lamp in lamp_dict.values():
    hl_obj = globals()[lamp]
    if hl_obj.on_off_state() == "on":
        print("%s is %s." % (colored(hl_obj.name, 'yellow'), colored(hl_obj.on_off_state(), 'green')))
    elif hl_obj.on_off_state() == "off":
        print("%s is %s." % (colored(hl_obj.name, 'yellow'), colored(hl_obj.on_off_state(), 'red')))

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

# create a dynamic string:
s = "Where to send ? "
for name in lamp_dict.values():
    y = name[5:]
    s = s + "%s " % y.replace(y[0], "(%s)" % y[0], 1)
if len(lamp_dict) > 1:
    s = s + "or (a)ll : "
else:
    s = s + " : "

while True:
    kbd_inp = input(s)
    print()
    first_letter_list = [y[5] for y in lamp_dict.values()]
    if kbd_inp in first_letter_list:
        k = [y for y in lamp_dict.values() if kbd_inp == y[5]]
        globals()[k[0]].on_off_switch(switch)
        break
    elif kbd_inp == "a":
        for lamp in lamp_dict.values():
            globals()[lamp].on_off_switch(switch)
        break
    else:
        s = "Please just input "
        for name in lamp_dict.values():
            s = s + "(%s) " % name[5]
        if len(lamp_dict) > 1:
            s = s + "or (a) : "
        else:
            s = s + " : "

for lamp in lamp_dict.values():
    hl_obj = globals()[lamp]
    if hl_obj.on_off_state() == "on":
        print("%s is %s." % (colored(hl_obj.name, 'yellow'), colored(hl_obj.on_off_state(), 'green')))
    elif hl_obj.on_off_state() == "off":
        print("%s is %s." % (colored(hl_obj.name, 'yellow'), colored(hl_obj.on_off_state(), 'red')))

    hl_obj.prop_chg_notify.kill()

print()







