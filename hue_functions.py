#!/usr/bin/env python3

def connect_lamp(lamp_address):
     import dbus
     systembus = dbus.SystemBus()
     destination = ('org.bluez')
     interface = ('org.bluez.Device1')
     objectpath = ('/org/bluez/hci0/dev_' + lamp_address)
     object = systembus.get_object(destination, objectpath)
     connection_handle = dbus.Interface(object, interface)
     connection_handle.Connect()

def connection_state(lamp_address):
    import dbus
    systembus = dbus.SystemBus()
    destination = ('org.bluez')
    interface = ('org.freedesktop.DBus.Properties')
    objectpath = ('/org/bluez/hci0/dev_' + lamp_address)
    object = systembus.get_object(destination, objectpath)
    connection_test_handle = dbus.Interface(object, interface)
    x = connection_test_handle.Get((dbus.String('org.bluez.Device1')), (dbus.String('Connected')))
    return (bool(x))
       
def connect(lamp_addresses):
    from termcolor import colored
    for lamp_address in lamp_addresses:
        state = connection_state(lamp_address)
        if state == False:
            print('Lamp ' + lamp_address + colored(' connecting ', 'yellow', attrs=['blink']), end='\r')
            connect_lamp(lamp_address)
            status = connection_state(lamp_address)
        if state == True:
            print('Lamp ' + lamp_address + colored(' connected  ' , 'green'))
            
def on_off_switch(lamp_address, switch):
    import dbus
    systembus = dbus.SystemBus()
    destination = ('org.bluez')
    interface = ('org.bluez.GattCharacteristic1')
    objectpath = ("/org/bluez/hci0/dev_" + lamp_address + "/service0023/char0026")
    object = systembus.get_object(destination, objectpath)
    on_off_handle = dbus.Interface(object, interface)
    on_off_handle.WriteValue((dbus.Array([dbus.Byte(switch)], dbus.Signature('y'))), (dbus.Dictionary([], dbus.Signature('sv'))))

def on_off_state(lamp_address):
    import dbus
    from termcolor import colored
    systembus = dbus.SystemBus()
    destination = ('org.bluez')
    interface = ('org.bluez.GattCharacteristic1')
    objectpath = ("/org/bluez/hci0/dev_" + lamp_address + "/service0023/char0026")
    object = systembus.get_object(destination, objectpath)
    on_off_handle = dbus.Interface(object, interface)
    ay = on_off_handle.ReadValue(dbus.Dictionary([], dbus.Signature('sv')))

    state = bool(ay[0])     # ReadValue returns an array of bytes now stored in the variable ay.
                            # There is only one item in the array, accessed with ay[0].
                            # Convert the byte into bool: bool(). Result is True or False, stored in state.
    if state == False:
        print("Lamp " + lamp_address + " is %s." % colored('off', 'red'))
    if state == True:
        print("Lamp " + lamp_address + " is %s." % colored('on', 'green'))

def alert(lamp_address, state):
    import dbus
    systembus = dbus.SystemBus()
    destination = ('org.bluez')
    interface = ('org.bluez.GattCharacteristic1')
    objectpath = ("/org/bluez/hci0/dev_" + lamp_address + "/service0023/char0032")
    object = systembus.get_object(destination, objectpath)
    alert_handle = dbus.Interface(object, interface)
    alert_handle.WriteValue((dbus.Array([dbus.Byte(state)], dbus.Signature('y'))), (dbus.Dictionary([], dbus.Signature('sv'))))
