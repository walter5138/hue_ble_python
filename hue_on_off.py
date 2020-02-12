#!/usr/bin/env python3

"""Switches Hue Lamp(s) on or off."""

from hue_config import lamp_addresses
from hue_functions import connect, on_off_switch, on_off_state

connect(lamp_addresses)

for lamp_address in lamp_addresses:
    on_off_state(lamp_address)

while True:
    x = input("on/off : ")
    if x == 'on':
        switch = 1
        break
    elif x == 'off':
        switch = 0
        break
    else:
        print("Please just input on or off.")

for lamp_address in lamp_addresses:
    on_off_switch(lamp_address, switch)

for lamp_address in lamp_addresses:
    on_off_state(lamp_address)
