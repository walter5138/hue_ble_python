#!/usr/bin/env python3

"""Makes the Hue Lamp(s) ping or blink."""

import dbus
from hue_config import lamp_addresses
from hue_functions import connect, alert

connect(lamp_addresses)

while True:
    x = input("You can make the lamps (p)ing once or (b)link 15 times and (s)top blinking while blinking : ")
    if x == 'p':
        state = 1
        break
    elif x == 'b':
        state = 2
        break
    elif x == 's':
        state = 0
        break
    else:
        print("Please just input (p)ing, (b)link or (s)top.")
    
for lamp_address in lamp_addresses:
    alert(lamp_address, state)
   
