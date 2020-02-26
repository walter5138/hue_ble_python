#!/usr/bin/env python3

"""Sets the brightness of the Hue Lamp(s)."""

from termcolor import colored
from hue_class import HueLamp
from hue_config import lamp_dict

for a, n in lamp_dict.items():
    globals()[n] = HueLamp(a, n)

print("\n######  Sets the brightness of the Hue Lamp(s). ######\n")

for lamp in lamp_dict.values():
    hl_obj = globals()[lamp]
    print("Lamp %s has brightness %s." % (colored(hl_obj.name, 'yellow'), colored(hl_obj.brightness_get(), 'green')))

print()

while True:
    x = input("Please input the brightness from 1 to 254 : ")
    print()
    try:
        y = int(x)
        if y in range(1, 255):
            bri = y
            break
        else:
            print("Value out of range.\n")
    except ValueError:
        print('"%s" is not a number. Try again.\n' % x)

s = "Where to send ? "
for name in lamp_dict.values():
    y = name[5:]
    s = s + "%s " % y.replace(y[0], "(%s)" % y[0], 1)
if len(lamp_dict) > 1:
    s = s + "or (a)ll : "
else:
    s = s + " : "

while True:
    kbd_inp = input(s)
    print()
    first_letter_list = [y[5] for y in lamp_dict.values()]
    if kbd_inp in first_letter_list:
        k = [y for y in lamp_dict.values() if kbd_inp == y[5]]
        globals()[k[0]].brightness_set(bri)
        break
    elif kbd_inp == "a":
        for lamp in lamp_dict.values():
            globals()[lamp].brightness_set(bri)
        break
    else:
        s = "Please just input "
        for name in lamp_dict.values():
            s = s + "(%s) " % name[5]
        if len(lamp_dict) > 1:
            s = s + "or (a) : "
        else:
            s = s + " : "

#time.sleep(0.5)   # if transitiontime is long values needs time to settle.

for lamp in lamp_dict.values():
    hl_obj = globals()[lamp]
    print("Lamp %s got brightness %s in %s seconds." % (colored(hl_obj.name, 'yellow'), colored(hl_obj.brightness_get(), 'green'),  colored(hl_obj.transitiontime_get(), 'green')))

    hl_obj.prop_chg_notify.kill()

print()
