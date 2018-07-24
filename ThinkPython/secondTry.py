#!/usr/bin/python3

import os
import json

var = os.popen("/usr/local/openvpn_as/scripts/sacli ConfigQuery")

currentConfig = var.read()


new_dict = json.loads(currentConfig)

if new_dict["vpn.client.routing.reroute_dns"] == "true":
    print("Can you now start?")




# new = currentConfig.split('"')


"""
#print(type(new))
#print("=======")

for element in new:
    if element != ":" and element != ',':
        print(element)
        
"""