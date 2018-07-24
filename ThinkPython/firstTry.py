#!/usr/bin/python3

import os


var = os.popen("/usr/local/openvpn_as/scripts/sacli version")

current_configuration = var.read()

print("Access Server version is ", current_configuration)

