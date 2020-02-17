#!/usr/bin/env python3

"""Alters the color temperature of the Hue Lamp(s)."""

import sys
import termios
import tty
import math
from hue_class import HueLamp
from termcolor import colored

hl_1 = HueLamp("F6_0A_34_1A_BC_6F", "kitchen   ")
hl_2 = HueLamp("EC_D6_5A_2D_93_CC", "livingroom")
hl_3 = HueLamp("DF_CA_54_1B_39_A8", "homeoffice")

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

def mired_alter(*hl):

    mir = 153
    already_send = "no"
    mir_sum = 0

    for lamp in hl:
        print('The current mired of lamp %s = %s.' % (colored(lamp.name, "yellow"), colored(lamp.mired_get(), "green")))
        mir_sum += lamp.mired_get()
    print()
    mir = int(math.floor(mir_sum / len(hl)))

    print('Changing mired of selected lamps start at their average of %s.\n' % (colored(mir, "cyan")))

    print("Please input [+/-/q]: ")

    while True:
        key = get_key()

        if key == "+":
            mir += 10 
            if mir >= 500:
                mir= 500
                print("%s = maximum mired" % colored(mir, 'red'))
                if already_send == "no":
                    for x in hl:
                        x.mired_set(mir)
                    already_send = "yes"    
            else:
                print(colored(mir, 'green'))
                for x in hl:
                    x.mired_set(mir)
                already_send = "no"
                    
        elif key == "-":
            mir -= 10
            if mir <= 153:
                mir = 153
                print("%s = minimum mired" % colored(mir, 'red'))
                if already_send == "no":
                    for x in hl:
                        x.mired_set(mir)
                    already_send = "yes"    
            else:
                print(colored(mir, 'green'))
                for x in hl:
                    x.mired_set(mir)
                already_send = "no"

        elif key == "q":
            print("\nbye bye (;-)\n")
            break
        else:
            print("Please just use + or - or (q)uit.")

print("\n######  Alter the lamp's mired  ######\n")

while True:
    x = input("Where to send: (k)itchen, (l)ivingroom, (h)omeoffice or (a)ll : ")
    print()
    if x == 'k':
        mired_alter(hl_1)
        break
    elif x == 'kl' or x == 'lk':
        mired_alter(hl_1, hl_2)
        break
    elif x == 'l':
        mired_alter(hl_2)
        break
    elif x == 'lh' or x == 'hl':
        mired_alter(hl_2, hl_3)
        break
    elif x == 'h':
        mired_alter(hl_3)
        break
    elif x == 'hk' or x == 'kh':
        mired_alter(hl_3, hl_1)
        break
    elif x == 'a':
        mired_alter(hl_1, hl_2, hl_3)
        break
    else:
        print("Please just input k, l, h or a.\n")

