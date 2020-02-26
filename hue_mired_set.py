#!/usr/bin/env python3

"""Sets the mired of the Hue Lamp(s)."""

#from time import sleep
from termcolor import colored
from hue_class import HueLamp
from hue_config import lamp_dict

for a, n in lamp_dict.items():
    globals()[n] = HueLamp(a, n)

print("\n######  Sets the mired of the Hue Lamp(s).  ######\n")

for lamp in lamp_dict.values():
    hl_obj = globals()[lamp]
    print("Lamp %s has mired %s." % (colored(hl_obj.name, 'yellow'), colored(hl_obj.mired_get(), 'green')))

print()

while True:
    x = input("Please input color temerature in mired from 153 (cold light) to 500 (warm light) : ")
    print()
    try:
        mir = int(x)
        if mir in range(153, 501):
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
        globals()[k[0]].mired_set(mir)
        #print("Lamp %s got mired %s in %s seconds." % (colored(hl_obj.name, 'yellow'), colored(hl_1.mired_get(), 'green'),  colored(hl_1.transitiontime_get(), 'green')))
        break
    elif kbd_inp == "a":
        for lamp in lamp_dict.values():
            globals()[lamp].mired_set(mir)
        break
    else:
        s = "Please just input "
        for name in lamp_dict.values():
            s = s + "(%s) " % name[5]
        if len(lamp_dict) > 1:
            s = s + "or (a) : "
        else:
            s = s + " : "

for lamp in lamp_dict.values():
    hl_obj = globals()[lamp]
    print("Lamp %s got mired %s in %s seconds." % (colored(hl_obj.name, 'yellow'), colored(hl_obj.mired_get(), 'green'),  colored(hl_obj.transitiontime_get(), 'green')))

    hl_obj.prop_chg_notify.kill()

print()

