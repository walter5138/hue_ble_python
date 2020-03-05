#!/usr/bin/env python3

class HueLamp:
    """HueLamp class representing and interact with Philips Hue Bluetooth Lamps."""

    def __init__(self, address, name="Hue_Lamp"):
        import time
        import subprocess
        self.address = address
        self.prop_chg_notify = subprocess.Popen(["./hue_props_dev_chg_notify.py", self.address, name])
        print("subprocess %s pid is %s" % (self.prop_chg_notify.args, self.prop_chg_notify.pid))
        self.connect()
        time.sleep(1)
        self.name_set(name)
        self.name = self.name_get()
        print('%s = %s, connection state: %s' % (self.address, self.name, self.connection_state()))

    def connection_state(self):
        import dbus
        systembus = dbus.SystemBus()
        #            ..._handle = dbus.Interface(systembus.get_object('destination', 'objectpath                         '), 'interface                      ')
        connection_state_handle = dbus.Interface(systembus.get_object('org.bluez'  , '/org/bluez/hci0/dev_' + self.address), 'org.freedesktop.DBus.Properties')
        x = connection_state_handle.Get('org.bluez.Device1', 'Connected')
        return (bool(x))

    def connect(self):
        import dbus
        systembus = dbus.SystemBus()
        connect_handle = dbus.Interface(systembus.get_object('org.bluez', '/org/bluez/hci0/dev_' + self.address), 'org.bluez.Device1')
        connect_handle.Connect()

    def name_get(self):
        import dbus
        systembus = dbus.SystemBus()
        name_get_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0011/char0014"), 'org.bluez.GattCharacteristic1')
        x = name_get_handle.ReadValue([])
        return ''.join([str(v) for v in x])

    def name_set(self, name):
        import dbus
        systembus = dbus.SystemBus()
        name_set_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0011/char0014"), 'org.bluez.GattCharacteristic1')
        
        ascii_list = [ord(c) for c in name]                 # comment

        name_set_handle.WriteValue(ascii_list, [])

    def on_off_switch(self, switch):
        import dbus
        systembus = dbus.SystemBus()
        on_off_switch_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char0026"), 'org.bluez.GattCharacteristic1')
        on_off_switch_handle.WriteValue([switch], [])

    def on_off_state(self):
        import dbus
        from termcolor import colored
        systembus = dbus.SystemBus()
        on_off_state_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char0026"), 'org.bluez.GattCharacteristic1')
        ay = on_off_state_handle.ReadValue([])

        if ay[0] == 0:        # ReadValue returns an array of bytes now stored in the variable ay.
            return "off"      # There is only one item in the array, accessed with ay[0].  
        elif ay[0] == 1:
            return "on"

    def mired_set(self, mired):
        import dbus
        systembus = dbus.SystemBus()
        mired_set_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char002c"), 'org.bluez.GattCharacteristic1')

        y = mired.to_bytes(2, 'little')                     # comment

        mired_set_handle.WriteValue([y[:1], y[1:]], [])     # comment

    def mired_get(self):
        import dbus
        systembus = dbus.SystemBus()
        mired_get_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char002c"), 'org.bluez.GattCharacteristic1')
        ay = mired_get_handle.ReadValue([])

        x = bytes(reversed(ay)).hex()                       # comment

        return int(x, 16)                                   # comment
                        
    def alert_set(self, state):
        import dbus
        systembus = dbus.SystemBus()
        alert_set_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char0032"), 'org.bluez.GattCharacteristic1')
        alert_set_handle.WriteValue([state], [])
                       
    def brightness_get(self):
        import dbus
        systembus = dbus.SystemBus()
        brightness_get_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char0029"), 'org.bluez.GattCharacteristic1')
        ay = brightness_get_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))

        return int(ay[0])     # ReadValue returns an array of bytes now stored in the variable ay.
                              # There is only one item in the array, accessed with ay[0].
                              # Convert the byte into int: int().

    def brightness_set(self, bri):
        import dbus
        systembus = dbus.SystemBus()
        brightness_set_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char0029"), 'org.bluez.GattCharacteristic1')
        brightness_set_handle.WriteValue([bri], [])

    def transitiontime_get(self):
        import dbus
        systembus = dbus.SystemBus()
        transitiontime_get_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char0037"), 'org.bluez.GattCharacteristic1')
        ay = transitiontime_get_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))

        return float(ay[0] / 10)                # ReadValue returns an array of bytes now stored in the variable ay.
                                                # There is only one item in the array, accessed with ay[0].
                                                # Return value is in miliseconds. "/10" converts it in seconds,
                                                # so the return value is, for example, usable in "time.sleep(0.4)".
                                                # Convert the byte into float: float().

    def transitiontime_set(self, trans):
        import dbus
        systembus = dbus.SystemBus()
        transitiontime_set_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char0037"), 'org.bluez.GattCharacteristic1')
        transitiontime_set_handle.WriteValue([trans, 0], [])

    def color_get(self):
        import dbus
        systembus = dbus.SystemBus()
        color_get_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char002f"), 'org.bluez.GattCharacteristic1')
        col = color_get_handle.ReadValue([])

        return [int(z) for z in col]

    def color_set(self, col):
        import dbus
        systembus = dbus.SystemBus()
        color_set_handle = dbus.Interface(systembus.get_object('org.bluez', "/org/bluez/hci0/dev_" + self.address + "/service0023/char002f"), 'org.bluez.GattCharacteristic1')
        color_set_handle.WriteValue(col, [])                   # comment



