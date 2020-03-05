# hue_ble_python
Project controlling Philips Hue Bluetooth color and white bulbs. Python version.

Project controlling Philips Hue Bluetooth color and white bulbs using:
- Bluez
- Dbus
- Python 
- dbus-python
- Philips Hue Bluetooth color and white bulbs ( LCA001 tested),
  and with all other Philips Hue lamps with the same characteristics.

It is a learning project and there are many improvementes to make,
But you can:
- search for new Bulbs
- auto pair
- auto trust
- set an Bluez alias
- auto connect the bulbs
- switch the bulbs on and off
- set the ac_on_state
- set, increase/decrease brightness
- set, increase/decrease mired ( color tempereature )
- set the color for a single bulb or all
- have different color loops
- change transition time
- alarm funktion: ping or blink  
- set the bulb name (stored in the Bulb)

This project is in daily development.
Therefore it is not granted to work any time.

If you are just interested in what the characteristics do
watch the class HueLamp in the file hue_class.py.


Following prerequisites are required:

1. A running Linux system.

2. Dbus running with system bus and session bus.

3. The Linux bluetooth-stack Bluez build with Dbus.o

4. Python with dbus-python.

4.5. Notification daemon running (temporarily for testing and learning)

5. Philips Hue Bluetooth color and white light bulbs ( LCA001 ).
   Tested with 1, 2 and 3 Bulbs.


Once the prerequisites are in place you need to:

Go to the Project folder ...../hue
Install your lamps, make shure they're powered AC/ON (wall switch),
if so they are shining in a warm white color.
Start with hue_discover_pair_trust_alias.py
All Bulbs are discovered, paired, and trusted automatically.
And you are requested to input an Alias for the lamp which is
blinking fore that time. Setting an Alias is essential!
The further programm(s) depend on that.
Done that you are ready to roll.
For the moment use the programms one by one, ./hue_brightness_set.py,
for example.
 

Have fun controlling the bulbs: ./hue_...


TUNING

Append to /var/lib/bluetooth/"adapter_id"/"hue_bulb_id"/info :
 
[ConnectionParameters]

MinInterval=6

MaxInterval=7

Latency=0

Timeout=216
	
Reduces the response time for the dbus-send commands.


TODO

- Alter using different number of bulbs. [DONE]
- Automate discovering, pairing, trusting  [DONE]
- Connecting the bulbs in a better way, reconnect via ... ?
- collect it all in a shiny cli


QUESTION

Could anyone help with sending the color values the right way ???
See hue_color_loop.py and hue_color_set.py.


