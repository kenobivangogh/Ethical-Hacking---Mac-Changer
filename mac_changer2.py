#!/usr/bin/env python
# -*- coding: utf-8 -*-
import optparse

# object
parse_object = optparse.OptionParser()
parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
# *args: -i --interface
# **kwargs: destination, help

parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac address")

# print(parse_object.parse_args())

# option_dictionary = parse_object.parse_args()
# print(option_dictionary)

(user_inputs, arguments) = parse_object.parse_args()  # tuple

print(user_inputs.interface)
print(user_inputs.mac_address)

print("Mac Changer started!")
