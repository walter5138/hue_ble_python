#!/usr/bin/env python3

"""Sets the brightness of the Hue Lamp(s)."""

import dbus
from hue_config import lamp_addresses
from hue_functions import connect

connect(lamp_addresses)

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

systembus = dbus.SystemBus()

destination = ('org.bluez')
interface = ('org.bluez.GattCharacteristic1')
object_paths = lamp_addresses

for object_path in object_paths:
    objectpath = ("/org/bluez/hci0/dev_" + object_path + "/service0023/char0029")
    object = systembus.get_object(destination, objectpath)
    brighness_handle = dbus.Interface(object, interface)

    brighness_handle.WriteValue((dbus.Array([dbus.Byte(bri)], dbus.Signature('y'))), (dbus.Dictionary([], dbus.Signature('sv'))))

