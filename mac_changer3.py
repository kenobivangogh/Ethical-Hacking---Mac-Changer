#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")

parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")

(user_inputs, arguments) = parse_object.parse_args()  # tuple

user_interface = user_inputs.interface
user_mac_address = user_inputs.mac_address

print("Mac Changer started!")

subprocess.call(["sudo", "ifconfig", user_interface, "down"])
subprocess.call(["sudo", "ifconfig", user_interface, "hw", "ether", user_mac_address])
subprocess.call(["sudo", "ifconfig", user_interface, "up"])
