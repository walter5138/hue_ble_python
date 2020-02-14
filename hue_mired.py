#!/usr/bin/env python3

"""Sets the brightness of the Hue Lamp(s)."""

from hue_class import HueLamp

hl_1 = HueLamp("F6_0A_34_1A_BC_6F", "lamp_kitchen   ")
hl_2 = HueLamp("EC_D6_5A_2D_93_CC", "lamp_livingroom")
hl_3 = HueLamp("DF_CA_54_1B_39_A8", "lamp_homeoffice")

hl_1.connect()
hl_2.connect()
hl_3.connect()

print(hl_1.connection_state())
print(hl_2.connection_state())
print(hl_3.connection_state())

print(hl_1.mired_get())
print(hl_2.mired_get())
print(hl_3.mired_get())

while True:
    x = input("Please input color temerature in mired from 153 (cold light) to 500 (warm light) : ")
    try:
        y = int(x)
        if y in range(153, 501):
            bri = y
            break
        else:
            print("Value out of range.")
    except ValueError:
        print('"%s" is not a number. Try again.' % x)

while True:
    x = input("Where to send: (k)itchen, (l)ivingroom, (h)omeoffice or (a)ll : ")
    if x == 'k':
        hl_1.mired_set(y)
        break
    if x == 'kl':
        hl_1.mired_set(y)
        hl_2.mired_set(y)
        break
    elif x == 'l':
        hl_2.mired_set(y)
        break
    if x == 'lh':
        hl_2.mired_set(y)
        hl_3.mired_set(y)
        break
    elif x == 'h':
        hl_3.mired_set(y)
        break
    if x == 'hk':
        hl_3.mired_set(y)
        hl_1.mired_set(y)
        break
    elif x == 'a':
        hl_1.mired_set(y)
        hl_2.mired_set(y)
        hl_3.mired_set(y)
        break
    else:
        print("Please just input k, l, h or a.")

print("Lamp %s has mired %s." % (hl_1.name, hl_1.mired_get()))
print("Lamp %s has mired %s." % (hl_2.name, hl_2.mired_get()))
print("Lamp %s has mired %s." % (hl_3.name, hl_3.mired_get()))
