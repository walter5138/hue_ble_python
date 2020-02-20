#!/usr/bin/env python3

class HueLamp:
    """HueLamp class representing and interact with Philips Bluetooth Hue Lamps."""

    def __init__(self, address, name="Hue_Lamp"):
        #import time
        #import threading
        self.address = address
        #thread_address = threading.Thread(target=self.prop_chg_notify(), args=())
        #thread_address.daemon = True
        #thread_address.start()
        #self.prop_chg_notify()
        self.connect()
        #time.sleep(4)
        self.name_set(name)
        self.name = self.name_get()
        print('%s = %s, connection state: %s' % (address, name, self.connection_state()))

    def prop_chg_notify(self):
        """Properties notification"""

        """
        It should be initiated with the class, showing changed properties with every instance
        from HueLamp, just for testing and learning.
        But it never returns although with treading or multiprocessing.
        It can be called while initiating only one instance, then it does what it schould do,
        but never returns. Thus no further executing and no further class instanciating.
        Has anyone an idea implementing this?
        """

        import dbus
        from dbus.mainloop.glib import DBusGMainLoop
        from gi.repository import GLib

        DBusGMainLoop(set_as_default=True)

        loop = GLib.MainLoop()

        systembus = dbus.SystemBus()
        sessionbus = dbus.SessionBus()

        destination = ('org.bluez')
        interface = ('org.freedesktop.DBus.Properties')
        objectpath = ('/org/bluez/hci0/dev_' + self.address)
        object = systembus.get_object(destination, objectpath)
        my_receiver = dbus.Interface(object, interface)

        def handler(interface, changed_properties, invalidated_properties):
            dest = ('org.freedesktop.Notifications')
            obj_p = ('/org/freedesktop/Notifications')
            inter_f = ('org.freedesktop.Notifications')
            obj = sessionbus.get_object(dest, obj_p)
            notification = dbus.Interface(obj, inter_f)
            for p in changed_properties:
                print("%s : %s" % (p, changed_properties[p]))
                notification.Notify("prop_changed", 0, "", "Properties changed!", "%s = %s" % (str(p), bool(changed_properties[p])), "", {}, 2000)

        my_receiver.connect_to_signal("PropertiesChanged", handler)

        loop.run()

    def connection_state(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ('/org/bluez/hci0/dev_' + self.address)
        interface = ('org.freedesktop.DBus.Properties')
        object = systembus.get_object(destination, objectpath)
        connection_test_handle = dbus.Interface(object, interface)
        x = connection_test_handle.Get((dbus.String('org.bluez.Device1')), (dbus.String('Connected')))
        return (bool(x))

    def connect(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ('/org/bluez/hci0/dev_' + self.address)
        interface = ('org.bluez.Device1')
        object = systembus.get_object(destination, objectpath)
        connect_handle = dbus.Interface(object, interface)
        connect_handle.Connect()

    def name_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0011/char0014")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        get_name_handle = dbus.Interface(object, interface)
        x = get_name_handle.ReadValue([])
        return ''.join([str(v) for v in x])

    def name_set(self, name):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0011/char0014")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        set_name_handle = dbus.Interface(object, interface)
        
        ascii_list = [ord(c) for c in name]                 # comment

        set_name_handle.WriteValue(ascii_list, [])

    def on_off_switch(self, switch):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0026")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        on_off_handle = dbus.Interface(object, interface)
        on_off_handle.WriteValue([switch], [])

    def on_off_state(self):
        import dbus
        from termcolor import colored
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0026")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        on_off_handle = dbus.Interface(object, interface)
        ay = on_off_handle.ReadValue([])

        if ay[0] == 0:        # ReadValue returns an array of bytes now stored in the variable ay.
            return "off"      # There is only one item in the array, accessed with ay[0].  
        elif ay[0] == 1:
            return "on"

    def mired_set(self, mired):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char002c")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        mired_set_handle = dbus.Interface(object, interface)

        y = mired.to_bytes(2, 'little')                     # comment

        mired_set_handle.WriteValue([y[:1], y[1:]], [])     # comment

    def mired_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char002c")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        mired_get_handle = dbus.Interface(object, interface)
        ay = mired_get_handle.ReadValue([])

        x = bytes(reversed(ay)).hex()                       # comment

        return int(x, 16)                                   # comment
                        
    def alert_set(self, state):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0032")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        alert_handle = dbus.Interface(object, interface)
        alert_handle.WriteValue([state], [])
                       
    def brightness_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0029")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        brightness_state_handle = dbus.Interface(object, interface)
        ay = brightness_state_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))

        return int(ay[0])     # ReadValue returns an array of bytes now stored in the variable ay.
                              # There is only one item in the array, accessed with ay[0].
                              # Convert the byte into int: int().

    def brightness_set(self, bri):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0029")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        brightness_handle = dbus.Interface(object, interface)
        brightness_handle.WriteValue([bri], [])

    def transitiontime_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0037")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        transitiontime_state_handle = dbus.Interface(object, interface)
        ay = transitiontime_state_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))

        return float(ay[0] / 10)                # ReadValue returns an array of bytes now stored in the variable ay.
                                                # There is only one item in the array, accessed with ay[0].
                                                # Return value is in miliseconds. "/10" converts it in seconds,
                                                # so the return value is, for example, usable in "time.sleep(0.4)".
                                                # Convert the byte into float: float().

    def transitiontime_set(self, trans):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0037")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        transitiontime_handle = dbus.Interface(object, interface)
        transitiontime_handle.WriteValue([trans, 0], [])

    def color_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char002f")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        transitiontime_handle = dbus.Interface(object, interface)
        col = transitiontime_handle.ReadValue([])

        return [int(z) for z in col]

    def color_set(self, col):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char002f")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        transitiontime_handle = dbus.Interface(object, interface)
        transitiontime_handle.WriteValue(col, [])                   # comment



