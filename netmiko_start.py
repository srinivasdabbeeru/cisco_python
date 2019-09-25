#!/usr/bin/python3

import netmiko
#multi-vendor library

#Device IPs I am connecting to today
#192.168.90.146
#192.168.90.147
#192.168.90.148

device1 = {

		   'username' : 'root',
		   'password' : 'cisco',
		   'device_type' : 'cisco_ios',
		   'host' : '192.168.90.146'

}

#  to connect target device
# by checking couple of things connecthandler will allow you to connect
'''
	.  device_type
	
'''
device_connect = netmiko.ConnectHandler(**device1)
print([i for i in dir(device_connect) if 'send' in i])
# now sending command
cmd = ["show ip int br", "show run | inc domain"]
for i in cmd:
	print("sending command ",i)
	print ("------------------")
	output = device_connect.send_command(i)
	print(output)