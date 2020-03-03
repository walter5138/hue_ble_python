#!/usr/bin/env python3

import sys

def prop_chg_notify(address, name):
    import dbus
    from dbus.mainloop.glib import DBusGMainLoop
    from gi.repository import GLib

    DBusGMainLoop(set_as_default=True)

    loop = GLib.MainLoop()

    systembus = dbus.SystemBus()
    sessionbus = dbus.SessionBus()

    properties_proxy = dbus.Interface(systembus.get_object('org.bluez', '/org/bluez/hci0/dev_'+ address), 'org.freedesktop.DBus.Properties')
    notification_proxy = dbus.Interface(sessionbus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications'), 'org.freedesktop.Notifications')

    def handler(interface, changed_properties, invalidated_properties):
        for p in changed_properties:
            print("%s : %s" % (p, changed_properties[p]))
            notification_proxy.Notify("prop_changed", 0, "", "Props %s changed!" % name, "%s = %s" % (str(p), bool(changed_properties[p])), "", {}, 2000)

    properties_proxy.connect_to_signal("PropertiesChanged", handler)

    loop.run()



prop_chg_notify(sys.argv[1], sys.argv[2])
