#!/usr/bin/env python3

"""Sets the mired of the Hue Lamp(s)."""

import dbus
from hue_config import instances
from hue_class import mired_set, mired_get

for instance in instances:
    instance.connect()
