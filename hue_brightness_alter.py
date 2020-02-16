#!/usr/bin/env python3

"""Alters brightness of the Hue Lamp(s)."""

import sys, termios, tty
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

def brightness_alter(*hl):

    bri = 1
    already_send = "no"
    bri_sum = 0

    for lamp in hl:
        print('The current brightness of lamp %s = %s.' % (colored(lamp.name, "yellow"), colored(lamp.brightness_get(), "green")))
        bri_sum += lamp.brightness_get()
    bri = int(math.floor(bri_sum / len(hl)))
    print('\nThe average brightness of selected lamps = %s.' % (colored(bri, "cyan")))

    print("\nPlease input [+/-/q]: \n")

    while True:
        key = get_key()

        if key == "+":
            bri += 5
            if bri >= 254:
                bri = 254
                print("%s = maximum brightness" % colored(bri, 'red'))
                if already_send == "no":
                    for x in hl:
                        x.brightness_set(bri)
                    already_send = "yes"    
            else:
                print(colored(bri, 'green'))
                for x in hl:
                    x.brightness_set(bri)
                already_send = "no"
                    
        elif key == "-":
            bri -= 5
            if bri <= 1:
                bri = 1
                print("%s = minimum brightness" % colored(bri, 'red'))
                if already_send == "no":
                    for x in hl:
                        x.brightness_set(bri)
                    already_send = "yes"    
            else:
                print(colored(bri, 'green'))
                for x in hl:
                    x.brightness_set(bri)
                x.brightness_set(bri)
                already_send = "no"

        elif key == "q":
            print("\nbye bye (;-)\n")
            break
        else:
            print("Please just use + or - or (q)uit.\n")

print("\n######  Alter the lamp's brightness  ######")

while True:
    x = input("\nWhere to send: (k)itchen, (l)ivingroom, (h)omeoffice or (a)ll : ")
    print("\n")

    if x == 'k':
        brightness_alter(hl_1)
        break
    elif x == 'kl' or x == 'lk':
        brightness_alter(hl_1, hl_2)
        break
    elif x == 'l':
        brightness_alter(hl_2)
        break
    elif x == 'lh' or x == 'hl':
        brightness_alter(hl_2, hl_3)
        break
    elif x == 'h':
        brightness_alter(hl_3)
        break
    elif x == 'hk' or x == 'kh':
        brightness_alter(hl_3, hl_1)
        break
    elif x == 'a':
        brightness_alter(hl_1, hl_2, hl_3)
        break
    else:
        print("Please just input k, l, h or a.")

