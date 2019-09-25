#!/usr/bin/python3

import netmiko
#multi-vendor library
from getpass import getpass

sec = getpass("please enter passowrd for device : ")
#Device IPs I am connecting to today
#192.168.90.146
#192.168.90.147
#192.168.90.148

device1 = {

		   'username' : 'root',
		   'password' : sec,
		   'device_type' : 'cisco_ios',
		   'host' : '192.168.90.146'

}

device2 = {

		   'username' : 'root',
		   'password' : sec,
		   'device_type' : 'cisco_ios',
		   'host' : '192.168.90.147'

}

device3 = {

		   'username' : 'root',
		   'password' : sec,
		   'device_type' : 'cisco_ios',
		   'host' : '192.168.90.148'

}

for i in [device1,device2,device3] :
	try:
		print ("                  ")
		print (i['host'])
		print ("------------------")
		print("Connecting to : ",i['host'])
		device_connect = netmiko.ConnectHandler(**i)
		# now sending command
		print ("Successfully logged in to ",i['host'])
		print ("\n")
		output = device_connect.send_command("show ip int br")
		print (i['host'], "#show ip int br")
		print(output)
		print ("                  ")
	except netmiko.ssh_exception.NetMikoTimeoutException:
		print("Connection timed out. Please check if the host is reachable : ",i['host'])
		print ("\n")
	except netmiko.ssh_exception.NetMikoAuthenticationException:
		print("Authentication error. Please check your username credentials : ",i['host'])
		print ("\n")
	except:
		print("Please check devicetype or values in Host ",i['host'])
		print ("\n")
	

#cmd = ["show ip int br", "show run | inc domain"]
#for i in cmd:
	#print("sending command ",i)
	#print ("------------------")
	#output = device_connect.send_command(i)
	
