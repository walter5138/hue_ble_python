#!/usr/bin/env python3

class HueLamp:

    def __init__(self, address, name="Hue_Lamp"):
        self.address = address
        self.connect()
        self.set_name(name)
        self.name = self.get_name()
        print('%s = %s, connection state: %s' % (address, name, self.connection_state()))

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

        if ay[0] == 0:        # ReadValue returns an array of bytes now stored in the variable ay.
            return "off"      # There is only one item in the array, accessed with ay[0].  
        elif ay[0] == 1:
            return "on"

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
                        
    def alert_set(self, state):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0032")
        object = systembus.get_object(destination, objectpath)
        alert_handle = dbus.Interface(object, interface)
        alert_handle.WriteValue([state], [])
                       
    def brightness_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0029")
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
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0029")
        object = systembus.get_object(destination, objectpath)
        brightness_handle = dbus.Interface(object, interface)
        brightness_handle.WriteValue([bri], [])

    def transitiontime_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0037")
        object = systembus.get_object(destination, objectpath)
        transitiontime_state_handle = dbus.Interface(object, interface)
        ay = transitiontime_state_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))

        return float(ay[0] * 0.1)     # ReadValue returns an array of bytes now stored in the variable ay.
                                      # There is only one item in the array, accessed with ay[0].
                                      # Return value is in miliseconds. "* 0.1" converts it in seconds,
                                      # so the return value is, for example, usable in "time.sleep(0.4)".
                                      # Convert the byte into float: float().

    def transitiontime_set(self, trans):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        interface = ('org.bluez.GattCharacteristic1')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0037")
        object = systembus.get_object(destination, objectpath)
        transitiontime_handle = dbus.Interface(object, interface)
        transitiontime_handle.WriteValue([trans, 0], [])




