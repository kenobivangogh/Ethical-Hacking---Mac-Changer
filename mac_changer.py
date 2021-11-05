#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

print("Mac Changer started!")

subprocess.call(["sudo", "ifconfig", "eth0", "down"])
subprocess.call(["sudo", "ifconfig", "eth0", "hw", "ether", "00:14:23:69:8e:c7"])
subprocess.call(["sudo", "ifconfig", "eth0", "up"])
