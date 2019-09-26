#!/usr/bin/python3

import time
from ncclient import manager
#this code will act as netonf client
#use connect function in manager to connect to Netconf enabled devices
device=manager.connect(host='192.168.90.146', username = 'root', password = 'cisco',port=22)
#device=manager.connect(host='192.168.90.146', username = 'root', password = 'cisco',port=22,allow_agent=False,look_for_keys=False)
print(device)
print("-------------------")
print("-------------------")
time.sleep(2)
print(dir(device))
print("@@@@@@@@@@@")
time.sleep(1)
print(device.get_config('running').data_xml)