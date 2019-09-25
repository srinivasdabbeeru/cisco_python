#!/usr/bin/python3

import netmiko,time
#multi-vendor library

device1 = {

		   'username' : 'root',
		   'password' : 'cisco',
		   'device_type' : 'cisco_ios',
		   'host' : '192.168.90.146'

}


#to connect target device
#by checking couple of thing connect handler will allow you to connect
'''

	. device_type

'''

device_connect = netmiko.ConnectHandler(**device1)
output = device_connect.send_command("show ip int br")
print("\n")
print(output)
print("\n")
output1 = device_connect.send_command("show ip int br", use_textfsm = True)
print(output1)
print("\n")

for i in output1:
	print ("The interface is ",i['intf']," and its IP address is ",i['ipaddr'])
	time.sleep(1)

print("\n")