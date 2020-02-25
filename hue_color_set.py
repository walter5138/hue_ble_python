#!/usr/bin/env python3

"""Sets the color of the Hue Lamp(s)."""

from termcolor import colored
from hue_class import HueLamp
from hue_config import lamp_dict

for a, n in lamp_dict.items():
    globals()[n] = HueLamp(a, n)

print("\n######  Sets the color of the Hue Lamp(s). ######\n")

for lamp in lamp_dict.values():
    hl_obj = globals()[lamp]
    print("Lamp %s has color %s." % (colored(hl_obj.name, 'yellow'), colored(hl_obj.color_get(), 'green')))

print()

while True:
    x = input("Please input one color: (w)hite, (r)ed, (y)ellow, (g)reen, (c)yan, (b)lue, (m)agenta: ")
    print()
    if x == "white" or x == "w":
        col = (0x01, 0x55, 0x55, 0x55)
        break
    elif x == "red" or x == "r":
        col = (0x01, 0xfe, 0x00, 0x01)
        break
    elif x == "green" or x == "g":
        col = (0x01, 0x00, 0x01, 0xfe)
        break
    elif x == "blue" or x == "b":
        col = (0x01, 0x00, 0xfe, 0x01)
        break
    elif x == "yellow" or x == "y":
        col = (0x01, 0x7f, 0x00, 0x7f)
        break
    elif x == "cyan" or x == "c":
        col = (0x01, 0x00, 0x7f, 0x7f)
        break
    elif x == "magenta" or x == "m":
        col = (0x01, 0x7f, 0x7f, 0x00)
        break
    else:
        print("Wrong input!\n")

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
        globals()[k[0]].color_set(col)
        break
    elif kbd_inp == "a":
        for lamp in lamp_dict.values():
            globals()[lamp].color_set(col)
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
    print("Lamp %s has color %s." % (colored(hl_obj.name, 'yellow'), colored(hl_obj.color_get(), 'green')))

    hl_obj.prop_chg_notify.kill()

print()
