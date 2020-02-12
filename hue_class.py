#!/usr/bin/env python3

class HueLamp:

    def __init__(self, address):
        self.address = address

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
        x = get_name_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))
        return ''.join([str(v) for v in x])

    def set_name(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0011/char0014")
        object = systembus.get_object(destination, objectpath)
        set_name_handle = dbus.Interface(object, interface)
        set_name_handle.WriteValue((dbus.Array([dbus.Byte(119), dbus.Byte(97), dbus.Byte(108), dbus.Byte(116), dbus.Byte(101), dbus.Byte(114)], dbus.Signature('y'))), (dbus.Dictionary([], dbus.Signature('sv'))))

    def on_off_switch(self, switch):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0026")
        object = systembus.get_object(destination, objectpath)
        on_off_handle = dbus.Interface(object, interface)
        on_off_handle.WriteValue((dbus.Array([dbus.Byte(switch)], dbus.Signature('y'))), (dbus.Dictionary([], dbus.Signature('sv'))))

    def on_off_state(self):
        import dbus
        from termcolor import colored
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0026")
        object = systembus.get_object(destination, objectpath)
        on_off_handle = dbus.Interface(object, interface)
        ay = on_off_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))

        return bool(ay[0])     # ReadValue returns an array of bytes now stored in the variable ay.
                               # There is only one item in the array, accessed with ay[0].
                               # Convert the byte into bool: bool(). Result is True or False.




