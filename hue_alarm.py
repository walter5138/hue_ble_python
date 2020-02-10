#!/usr/bin/env python3

"""Makes the Hue Lamp(s) ping or blink."""

import dbus
from hue_config import lamp_addresses
from hue_functions import connect

connect(lamp_addresses)

while True:
    x = str(input("You can make the lamps (p)ing once or (b)link 15 times and (s)top blinking while blinking : "))
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

systembus = dbus.SystemBus()

destination = ('org.bluez')
interface = ('org.bluez.GattCharacteristic1')
object_paths = lamp_addresses

for object_path in object_paths:
    objectpath = ("/org/bluez/hci0/dev_" + object_path + "/service0023/char0032")
    object = systembus.get_object(destination, objectpath)
    alarm_handle = dbus.Interface(object, interface)

    alarm_handle.WriteValue((dbus.Array([dbus.Byte(state)], dbus.Signature('y'))), (dbus.Dictionary([], dbus.Signature('sv'))))
   
