#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

print("Mac Changer started!")

interface = "eth0"
mac_address = "00:01:c5:6d:88:27"

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["sudo", "ifconfig", interface, "up"])
