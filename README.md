# hue_ble_python
Project controlling Philips Hue Bluetooth color and white bulbs. Python version.

Project controlling Philips Hue Bluetooth color and white bulbs using:
- Bluez
- Dbus
- Python 
- Philips Hue Bluetooth color and white bulbs ( LCA001 tested),
  and with all other Philips Hue lamps with the same characteristics.

It is a learning project and there are many improvementes to make,
But you can:
- connect the bulbs
- switch the bulbs on and off
- set the ac_on_state
- set, increase/decrease brightness
- set, increase/decrease mired ( color tempereature )
- set the color for a single bulb or all
- have different color loops
- change transition time
- alarm funktion: ping or blink  
- set the bulb name

It demonstrates what the characteristics do.
Aware of that you can use them in your own projects.

This project is in daily development.
Therefore it is not granted to work for everybody.

If you are just interested in what the characteristics do
watch the class HueLamp in the file hue_class.py.


Following prerequisites are required:

1. A running Linux system.

2. Dbus running with system bus

3. The Linux bluetooth-stack Bluez build with Dbus

3,5. Notification daemon running (temporarily for testing and learning)

4. 3 Philips Hue Bluetooth color and white light bulbs ( LCA001 )
   If you have more or less than 3 Bulbs you have to alter some scripts
   at the moment. See TODO.


Get it working:

Once the prerequisites are in place you need to:

Use bluetoothctl to pair and connect the bulbs:
- go to a terminal
- at the prompt input bluetoothctl
- check if the Bluetoothcontroller is available: list
- power on the bluetoothcontroller: power on 
  If you want the bluetoothcontroller to be powered on as soon it's available (while boot)
  go to /etc/bluetooth/main.conf and uncomment "AutoEnable=true" at the bottom of the file
- make the controller pairable: pairable on
- scan for new devices: scan on
- pair the bulb with the address: pair XX:XX:XX:XX:XX:XX
- trust the bulb: trust XX:XX:XX:XX:XX:XX

Have fun controlling the bulbs: ./hue_...


Tuning

Append to /var/lib/bluetooth/"adapter_id"/"hue_bulb_id"/info :
 
[ConnectionParameters]

MinInterval=6

MaxInterval=7

Latency=0

Timeout=216
	
Reduces the response time for the dbus-send commands.


TODO

- Alter using different number of bulbs. [DONE]
- Connecting the bulbs in a better way.
- Automate pairing 
