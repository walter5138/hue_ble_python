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

def get_connection_status(lamp_address):
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
    from termcolor import colored, cprint
    for lamp_address in lamp_addresses:
        status = get_connection_status(lamp_address)
        if status == False:
            print('Lamp ' + lamp_address + colored(' connecting ', 'yellow', attrs=['blink']), end='\r')
            connect_lamp(lamp_address)
            status = get_connection_status(lamp_address)
        if status == True:
            print('Lamp ' + lamp_address + colored(' connected  ' , 'green'))
            
