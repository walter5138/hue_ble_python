#!/usr/bin/env python3

class HueLamp:
    """HueLamp class representing and interact with Philips Bluetooth Hue Lamps."""

    def __init__(self, address, name="Hue_Lamp"):
        import time
        import subprocess
        self.address = address
        self.prop_chg_notify = subprocess.Popen(["./hue_sig_res.py", self.address, name])
        print("subprocess %s pid is %s" % (self.prop_chg_notify.args, self.prop_chg_notify.pid))
        self.connect()
        time.sleep(4)
        self.name_set(name)
        self.name = self.name_get()
        print('%s = %s, connection state: %s' % (self.address, self.name, self.connection_state()))

    def connection_state(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ('/org/bluez/hci0/dev_' + self.address)
        interface = ('org.freedesktop.DBus.Properties')
        object = systembus.get_object(destination, objectpath)
        connection_state_handle = dbus.Interface(object, interface)
        x = connection_state_handle.Get((dbus.String('org.bluez.Device1')), (dbus.String('Connected')))
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
        name_get_handle = dbus.Interface(object, interface)
        x = name_get_handle.ReadValue([])
        return ''.join([str(v) for v in x])

    def name_set(self, name):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0011/char0014")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        name_set_handle = dbus.Interface(object, interface)
        
        ascii_list = [ord(c) for c in name]                 # comment

        name_set_handle.WriteValue(ascii_list, [])

    def on_off_switch(self, switch):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0026")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        on_off_switch_handle = dbus.Interface(object, interface)
        on_off_switch_handle.WriteValue([switch], [])

    def on_off_state(self):
        import dbus
        from termcolor import colored
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0026")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        on_off_state_handle = dbus.Interface(object, interface)
        ay = on_off_state_handle.ReadValue([])

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
        alert_set_handle = dbus.Interface(object, interface)
        alert_set_handle.WriteValue([state], [])
                       
    def brightness_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0029")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        brightness_get_handle = dbus.Interface(object, interface)
        ay = brightness_get_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))

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
        brightness_set_handle = dbus.Interface(object, interface)
        brightness_set_handle.WriteValue([bri], [])

    def transitiontime_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char0037")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        transitiontime_get_handle = dbus.Interface(object, interface)
        ay = transitiontime_get_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))

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
        transitiontime_set_handle = dbus.Interface(object, interface)
        transitiontime_set_handle.WriteValue([trans, 0], [])

    def color_get(self):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char002f")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        color_get_handle = dbus.Interface(object, interface)
        col = color_get_handle.ReadValue([])

        return [int(z) for z in col]

    def color_set(self, col):
        import dbus
        systembus = dbus.SystemBus()
        destination = ('org.bluez')
        objectpath = ("/org/bluez/hci0/dev_" + self.address + "/service0023/char002f")
        interface = ('org.bluez.GattCharacteristic1')
        object = systembus.get_object(destination, objectpath)
        color_set_handle = dbus.Interface(object, interface)
        color_set_handle.WriteValue(col, [])                   # comment



