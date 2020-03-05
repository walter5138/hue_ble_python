#!/usr/bin/env python3

import dbus

systembus = dbus.SystemBus()

o_manager = dbus.Interface(systembus.get_object('org.bluez', '/'), 'org.freedesktop.DBus.ObjectManager') 
m_objects = o_manager.GetManagedObjects()

lamp_dict = {}

for obj_paths, obj_dict in m_objects.items():
    if "org.bluez.Device1" in obj_dict.keys():
        for interface, properties in obj_dict.items():
            if "Hue Lamp" in properties.values():
                for property, value in properties.items():
                    if property == "Address":
                        v = str(value)
                        x = v.replace(":", "_")
                    if property == "Alias":
                        y = str(value)
                lamp_dict[x] = y 

#print(lamp_dict)
lamp_dict
