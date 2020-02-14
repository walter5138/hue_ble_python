#!/usr/bin/env python3

class HueLamp:

    def __init__(self, address, name="Hue_Lamp"):
        self.address = address
        self.set_name(name)
        self.name = self.get_name()
        print('%s = %s' % (address, name))

    def connection_state(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.freedesktop.DBus.Properties')
        objectpath = ('/org/bluez/hci0/dev_' + self.address)
        object = systembus.get_object(destination, objectpath)
        connection_test_handle = dbus.Interface(object, interface)
        x = connection_test_handle.Get((dbus.String('org.bluez.Device1')), (dbus.String('Connected')))
        return (bool(x))

    def connect(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.Device1')
        objectpath = ('/org/bluez/hci0/dev_' + self.address)
        object = systembus.get_object(destination, objectpath)
        connection_handle = dbus.Interface(object, interface)
        connection_handle.Connect()

    def get_name(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0011/char0014")
        object = systembus.get_object(destination, objectpath)
        get_name_handle = dbus.Interface(object, interface)
        x = get_name_handle.ReadValue([])
        return ''.join([str(v) for v in x])

    def set_name(self, name):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0011/char0014")
        object = systembus.get_object(destination, objectpath)
        set_name_handle = dbus.Interface(object, interface)
        ascii_list = [ord(c) for c in name]
        set_name_handle.WriteValue((ascii_list), [])

    def on_off_switch(self, switch):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0026")
        object = systembus.get_object(destination, objectpath)
        on_off_handle = dbus.Interface(object, interface)
        on_off_handle.WriteValue([switch], [])

    def on_off_state(self):
        import dbus
        from termcolor import colored
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0026")
        object = systembus.get_object(destination, objectpath)
        on_off_handle = dbus.Interface(object, interface)
        ay = on_off_handle.ReadValue([])

        return bool(ay[0])     # ReadValue returns an array of bytes now stored in the variable ay.
                               # There is only one item in the array, accessed with ay[0].
                               # Convert the byte into bool: bool(). Result is True or False.

    def mired_set(self, mired):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char002c")
        object = systembus.get_object(destination, objectpath)
        mired_set_handle = dbus.Interface(object, interface)

        y = mired.to_bytes(2, 'little')                     # Please comment!!!!!!!!!!!!!!!!!!!

        mired_set_handle.WriteValue([y[:1], y[1:]], [])     # Please comment!!!!!!!!!!!!!!!!!!!

    def mired_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char002c")
        object = systembus.get_object(destination, objectpath)
        mired_get_handle = dbus.Interface(object, interface)
        ay = mired_get_handle.ReadValue([])

        x = bytes(reversed(ay)).hex()                       # Please comment!!!!!!!!!!!!!!!!!!!

        return int(x, 16)                                   # Please comment!!!!!!!!!!!!!!!!!!!
                        
                       





