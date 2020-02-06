#!/usr/bin/env python3

"""Switches Hue Lamp(s) on or off."""

import dbus
from settings import lamp_addresses

while True:
    x = input("on/off : ")
    if x == 'on':
        state = 1
        break
    elif x == 'off':
        state = 0
        break
    else:
        print("Please just input on or off.")

systembus = dbus.SystemBus()

destination = ('org.bluez')
interface = ('org.bluez.GattCharacteristic1')
object_paths = lamp_addresses

for object_path in object_paths:
    objectpath = ("/org/bluez/hci0/dev_" + object_path + "/service0023/char0026")
    object = systembus.get_object(destination, objectpath)
    on_off_handle = dbus.Interface(object, interface)

    on_off_handle.WriteValue((dbus.Array([dbus.Byte(state)], dbus.Signature('y'))), (dbus.Dictionary([], dbus.Signature('sv'))))
    x = on_off_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))
    print("int: %s" % [int(y) for y in x])
   # print("str: %s" % [str(y) for y in x])
   # print("hex: %s" % [hex(y) for y in x])
   # print("hex: %#0.2x" % 14)
