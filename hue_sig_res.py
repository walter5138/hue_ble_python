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

    destination = ('org.bluez')
    interface = ('org.freedesktop.DBus.Properties')
    objectpath = ('/org/bluez/hci0/dev_'+ address)
    object = systembus.get_object(destination, objectpath)
    my_receiver = dbus.Interface(object, interface)

    def handler(interface, changed_properties, invalidated_properties):
        dest = ('org.freedesktop.Notifications')
        obj_p = ('/org/freedesktop/Notifications')
        inter_f = ('org.freedesktop.Notifications')
        obj = sessionbus.get_object(dest, obj_p)
        notification = dbus.Interface(obj, inter_f)
        for p in changed_properties:
            #print("%s : %s" % (p, changed_properties[p]))
            notification.Notify("prop_changed", 0, "", "Props %s changed!" % name, "%s = %s" % (str(p), bool(changed_properties[p])), "", {}, 2000)

    my_receiver.connect_to_signal("PropertiesChanged", handler)

    loop.run()



prop_chg_notify(sys.argv[1], sys.argv[2])
