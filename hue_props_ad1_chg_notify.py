#!/usr/bin/env python3

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

DBusGMainLoop(set_as_default=True)

loop = GLib.MainLoop()

systembus = dbus.SystemBus()
sessionbus = dbus.SessionBus()

def prop_handler(interface, changed_properties, invalidated_properties):
    notification_proxy = dbus.Interface(sessionbus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications'), 'org.freedesktop.Notifications')
    for p in changed_properties:
        notification_proxy.Notify("prop_changed", 0, "", "Props %s changed!" % interface, "%s = %s" % (str(p), bool(changed_properties[p])), "", {}, 4000)
        print("%s : %s" % (p, changed_properties[p]))
    print()

properties_proxy = dbus.Interface(systembus.get_object('org.bluez', '/org/bluez/hci0'), 'org.freedesktop.DBus.Properties')
properties_proxy.connect_to_signal("PropertiesChanged", prop_handler)

loop.run()

