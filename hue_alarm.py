#!/usr/bin/env python3

"""Makes the Hue Lamp(s) ping or blink."""

from hue_class import HueLamp

hl_1 = HueLamp("F6_0A_34_1A_BC_6F", "kitchen   ")
hl_2 = HueLamp("EC_D6_5A_2D_93_CC", "livingroom")
hl_3 = HueLamp("DF_CA_54_1B_39_A8", "homeoffice")

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
    
while True:
    x = input("Where to send: (k)itchen, (l)ivingroom, (h)omeoffice or (a)ll : ")
    print()
    if x == 'k':
        hl_1.alert_set(state)
        break
    elif x == 'kl' or x == 'lk':
        hl_1.alert_set(state)
        hl_2.alert_set(state)
        break
    elif x == 'l':
        hl_2.alert_set(state)
        break
    elif x == 'lh' or x == 'hl':
        hl_2.alert_set(state)
        hl_3.alert_set(state)
        break
    elif x == 'h':
        hl_3.alert_set(state)
        break
    elif x == 'hk' or x == 'kh':
        hl_3.alert_set(state)
        hl_1.alert_set(state)
        break
    elif x == 'a':
        hl_1.alert_set(state)
        hl_2.alert_set(state)
        hl_3.alert_set(state)
        break
    else:
        print("Please just input k, l, h or a.\n")
   
