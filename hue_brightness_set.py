#!/usr/bin/env python3

"""Sets the brightness of the Hue Lamp(s)."""

import dbus
from hue_config import lamp_addresses
from hue_functions import connect, brightness_set, brightness_get

connect(lamp_addresses)

for lamp_address in lamp_addresses:
    brightness_get(lamp_address)

while True:
    x = input("Please input brightness from 1 to 254 : ")
    try:
        y = int(x)
        if y in range(1,255):
            bri = y
            break
        else:
            print("Value out of range.")
    except ValueError:
        print('"%s" is not a number. Try again.' % x)

for lamp_address in lamp_addresses:
    brightness_set(lamp_address, bri)

for lamp_address in lamp_addresses:
    brightness_get(lamp_address)

