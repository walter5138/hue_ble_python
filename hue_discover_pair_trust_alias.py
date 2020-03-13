#!/usr/bin/env python3

import dbus
import subprocess
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from time import sleep

DBusGMainLoop(set_as_default=True)

loop = GLib.MainLoop()

systembus = dbus.SystemBus()
sessionbus = dbus.SessionBus()

scantime = 60 

print()

def interfaces_added(object, interfaces):
    print("\n\n********************************************************************************************************\n\n")
    print("device (object path) added : %s\n" % object)
    print("\twith interfaces : ")
    for interface, properties in interfaces.items():
        print("\t\t%s" % interface)
        for prop, value in properties.items():
            if "ManufacturerData" in prop:
                if prop == "ManufacturerData":
                    for md_key, md_val_arr in value.items():
                        print("\t\t\t%s = %s : %s" % (prop, md_key, [int(md_val) for md_val in md_val_arr]))
            elif "ServiceData" in prop:
                if prop == "ServiceData":
                    for sd_key, sd_val_arr in value.items():
                        print("\t\t\t%s = %s : %s" % (prop, sd_key, [int(sd_val) for sd_val in sd_val_arr]))
            elif "UUIDs" in prop:
                if prop == "UUIDs":
                    print("\t\t\t%s = " % prop)
                    for UUID in value:
                        print("\t\t\t\t%s" % UUID)
            elif "Value" in prop:
                if prop == "Value":
                    print("\t\t\t%s = %s" % (prop, [int(Value) for Value in value]))
            elif "Flags" in prop:
                if prop == "Flags":
                    print("\t\t\t%s = %s" % (prop, [str(Flag) for Flag in value]))
            elif "Includes" in prop:
                if prop == "Includes":
                    print("\t\t\t%s = %s" % (prop, [str(Includes) for Includes in value]))
            else:
                print("\t\t\t%s = %s" % (prop, value))
    print()
    
def interfaces_removed(object, interfaces):
    print("\n\n********************************************************************************************************\n\n")
    print("device (object path) removed : %s\n" % object)
    print("\tremoved interfaces : ")
    for interface in interfaces:
        print("\t\t%s" % interface)
    print()

def notify_adapter1(switch):
    global prop_chg_notify
    if switch == "start":
        prop_chg_notify = subprocess.Popen(["./hue_props_ad1_chg_notify.py"])
        print("adapter1 notification started : %s pid %s" % (prop_chg_notify.args, prop_chg_notify.pid))
    if switch == "stop":
        print("adapter1 notification stopped : pid %s" % prop_chg_notify.pid)
        prop_chg_notify.kill()
    print()
    sleep(1)

def notify_lamps(switch, address):
    pass

def discovery(switch):
    adapter1_proxy = dbus.Interface(systembus.get_object('org.bluez', '/org/bluez/hci0'), 'org.bluez.Adapter1')
    if switch == "start":
        adapter1_proxy.StartDiscovery()
        print("Discovery started!")
    if switch == "stop":
        adapter1_proxy.StopDiscovery()
        print("Discovery stoped!")
    print()
    sleep(1)

def set_scantime(sec):
    GLib.timeout_add_seconds(sec, quit)

def quit():
    loop.quit()

def new_huelamps_get():
    o_manager = dbus.Interface(systembus.get_object('org.bluez', '/'), 'org.freedesktop.DBus.ObjectManager') 
    m_objects = o_manager.GetManagedObjects()
    new_huelamp_addresses = []
    for obj_paths, obj_dict in m_objects.items():
        if "org.bluez.Device1" in obj_dict.keys():
            for interface, properties in obj_dict.items():
                if "Hue Lamp" in properties.values():
                    if properties["Paired"] == 0:
                        print("New %s with address %s found, paired = %s!" % (properties["Name"], properties["Address"], bool(properties["Paired"])))
                        new_huelamp_addr = properties["Address"]
                        new_huelamp_addr = new_huelamp_addr.replace(":", "_")
                        new_huelamp_addresses.append(new_huelamp_addr)
    if new_huelamp_addresses == []:
        print("No new Hue Lamps found!")
    print()
    return new_huelamp_addresses

def new_huelamp_pair_trust(new_huelamp_addresses):
    properties_adapter1 = dbus.Interface(systembus.get_object('org.bluez', '/org/bluez/hci0'), 'org.freedesktop.DBus.Properties')
    properties_adapter1.Set("org.bluez.Adapter1", "Pairable", True)

    for new_huelamp_address in new_huelamp_addresses:
        new_device_proxy = dbus.Interface(systembus.get_object('org.bluez', '/org/bluez/hci0/dev_' + new_huelamp_address), 'org.bluez.Device1')
        new_device_proxy.Pair()
        properties_lamp = dbus.Interface(systembus.get_object('org.bluez', '/org/bluez/hci0/dev_' + new_huelamp_address), 'org.freedesktop.DBus.Properties')
        properties_lamp.Set("org.bluez.Device1", "Trusted", True)
        is_paired = properties_lamp.Get("org.bluez.Device1", "Paired")
        print("New Hue Lamp %s is paired : %s." % (new_huelamp_address, bool(is_paired)))
        is_trusted = properties_lamp.Get("org.bluez.Device1", "Trusted")
        print("New Hue Lamp %s is trusted : %s." % (new_huelamp_address, bool(is_trusted)))
    print()

def new_huelamp_alias(new_huelamp_addresses):
    for new_huelamp_address in new_huelamp_addresses:
        blink_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + new_huelamp_address + "/service0023/char0032"), 'org.bluez.GattCharacteristic1')
        blink_handle.WriteValue([2], [])
        properties_lamp = dbus.Interface(systembus.get_object('org.bluez', '/org/bluez/hci0/dev_' + new_huelamp_address), 'org.freedesktop.DBus.Properties')
        name = input("Please input an alias for the blinking lamp : ")
        print()
        properties_lamp.Set("org.bluez.Device1", "Alias", "lamp_" + name)
    print()

systembus.add_signal_receiver(interfaces_added,
                                dbus_interface = "org.freedesktop.DBus.ObjectManager",
                                signal_name = "InterfacesAdded")

systembus.add_signal_receiver(interfaces_removed,
                                dbus_interface = "org.freedesktop.DBus.ObjectManager",
                                signal_name = "InterfacesRemoved")

notify_adapter1("start")
discovery("start")

set_scantime(scantime)

loop.run()

#print("\nloop finished program continuing!\n")

discovery("stop")

new_huelamp_addresses = new_huelamps_get()

if new_huelamp_addresses != []:
    new_huelamp_pair_trust(new_huelamp_addresses)
    new_huelamp_alias(new_huelamp_addresses)

notify_adapter1("stop")


