#!/usr/bin/env python3

"""Alters the color temperature of the Hue Lamp(s)."""

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
    """Function to get keyboard key without enter."""

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def mired_alter(hl):

    mir = 153
    already_send = "no"
    mir_sum = 0

    for lamp in hl:
        hl_obj = globals()[lamp]
        print('The current mired of lamp %s = %s.' % (colored(hl_obj.name, "yellow"), colored(hl_obj.mired_get(), "green")))
        mir_sum += hl_obj.mired_get()
    print()
    mir = int(math.floor(mir_sum / len(hl)))

    print('Changing mired of selected lamps start at their average of %s.\n' % (colored(mir, "cyan")))

    print("Please input [+/-/q]: ")

    while True:
        key = get_key()

        if key == "+":
            mir += 10 
            if mir >= 500:
                mir = 500
                print("%s = maximum mired" % colored(mir, 'red'))
                if already_send == "no":
                    for lamp in hl:
                        hl_obj = globals()[lamp]
                        hl_obj.mired_set(mir)
                    already_send = "yes"    
            else:
                print(colored(mir, 'green'))
                for lamp in hl:
                    hl_obj = globals()[lamp]
                    hl_obj.mired_set(mir)
                already_send = "no"
                    
        elif key == "-":
            mir -= 10
            if mir <= 153:
                mir = 153
                print("%s = minimum mired" % colored(mir, 'red'))
                if already_send == "no":
                    for lamp in hl:
                        hl_obj = globals()[lamp]
                        hl_obj.mired_set(mir)
                    already_send = "yes"    
            else:
                print(colored(mir, 'green'))
                for lamp in hl:
                    hl_obj = globals()[lamp]
                    hl_obj.mired_set(mir)
                already_send = "no"

        elif key == "q":
            print("\nbye bye (;-)\n")
            break
        else:
            print("Please just use + or - or (q)uit.")

print("\n######  Alter the lamp's mired  ######\n")

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
        mired_alter(k)
        break
    elif kbd_inp == "a":
        mired_alter([y for y in lamp_dict.values()])
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



