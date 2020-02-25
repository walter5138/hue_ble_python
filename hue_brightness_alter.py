#!/usr/bin/env python3

"""Alters brightness of the Hue Lamp(s)."""

import sys
import termios
import tty
import math
from termcolor import colored
from hue_class import HueLamp
from hue_config import lamp_dict

for a, n in lamp_dict.items():
    globals()[n] = HueLamp(a, n)

def get_key():
    """function to get keyboard key without enter."""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def brightness_alter(hl):

    bri = 1
    already_send = "no"
    bri_sum = 0

    for lamp in hl:
        hl_obj = globals()[lamp]
        print('The current brightness of lamp %s = %s.' % (colored(hl_obj.name, "yellow"), colored(hl_obj.brightness_get(), "green")))
        bri_sum += hl_obj.brightness_get()
    print()
    bri = int(math.floor(bri_sum / len(hl)))

    print('Changing brightness of selected lamps start at their average of %s.\n' % (colored(bri, "cyan")))

    print("Please input [+/-/q]: ")

    while True:
        key = get_key()

        if key == "+":
            bri += 5
            if bri >= 254:
                bri = 254
                print("%s = maximum brightness" % colored(bri, 'red'))
                if already_send == "no":
                    for lamp in hl:
                        hl_obj = globals()[lamp]
                        hl_obj.brightness_set(bri)
                    already_send = "yes"    
            else:
                print(colored(bri, 'green'))
                for lamp in hl:
                    hl_obj = globals()[lamp]
                    hl_obj.brightness_set(bri)
                already_send = "no"
                    
        elif key == "-":
            bri -= 5
            if bri <= 1:
                bri = 1
                print("%s = minimum brightness" % colored(bri, 'red'))
                if already_send == "no":
                    for lamp in hl:
                        hl_obj = globals()[lamp]
                        hl_obj.brightness_set(bri)
                    already_send = "yes"    
            else:
                print(colored(bri, 'green'))
                for lamp in hl:
                    hl_obj = globals()[lamp]
                    hl_obj.brightness_set(bri)
                already_send = "no"

        elif key == "q":
            print("\nbye bye (;-)\n")
            break
        else:
            print("Please just use + or - or (q)uit.")

print("\n######  Alter the lamp's brightness  ######\n")

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
        brightness_alter(k)
        break
    elif kbd_inp == "a":
        brightness_alter([y for y in lamp_dict.values()])
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

    hl_obj.prop_chg_notify.kill()


