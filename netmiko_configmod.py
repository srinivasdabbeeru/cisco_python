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


#to connect target device
#by checking couple of thing connect handler will allow you to connect
'''

	. device_type

'''

device_connect = netmiko.ConnectHandler(**device1)
print([i for i in dir(device_connect) if 'send' in i])

#now sending configuration for device
configuration = ["hostname R1", "username hello priv 15 password cisco"]
output = device_connect.send_config_set(configuration)
print(output)

#sending configuration from file
output1 = device_connect.send_config_from_file('input_commands.txt')
print(output1)