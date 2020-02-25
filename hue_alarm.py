#!/usr/bin/env python3

"""Makes the Hue Lamp(s) ping or blink."""

from hue_class import HueLamp
from hue_config import lamp_dict

for a, n in lamp_dict.items():
    globals()[n] = HueLamp(a, n)

print("\n######  Makes the Hue Lamp(s) ping or blink.  ######\n") 

while True:
    x = input("You can make the lamps (p)ing once or (b)link 15 times and (s)top blinking while blinking : ")
    print()
    if x == 'p':
        state = 1
        break
    elif x == 'b':
        state = 2
        break
    elif x == 's':
        state = 0
        break
    else:
        print("Please just input (p)ing, (b)link or (s)top.\n")

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
        globals()[k[0]].alert_set(state)
        break
    elif kbd_inp == "a":
        for lamp in lamp_dict.values():
            globals()[lamp].alert_set(state)
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

    hl_obj.prop_chg_notify.kill()

print()

