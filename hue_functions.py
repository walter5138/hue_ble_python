#!/usr/bin/env python3

import dbus

def connect(lamp_addresses):

    systembus = dbus.SystemBus()

    destination = ('org.bluez')
    interface = ('org.bluez.Device1')
    object_paths = lamp_addresses

    for object_path in object_paths:
        objectpath = ("/org/bluez/hci0/dev_" + object_path)
       # print(objectpath)
        object = systembus.get_object(destination, objectpath)
       # print(object)
        connection_handle = dbus.Interface(object, interface)
       # print(connection_handle)

        x = connection_handle.Connect()
        print(x)
       # x = connection_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))
       # print("%s" % [int(v) for v in x])


