#!/usr/bin/python3

import paramiko,time,sys

# using as ssh client
client = paramiko.SSHClient()
# auto adjust  host key verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#create list of devices
device_ip = ["192.168.90.146", "192.168.90.146"]
u = 'root'
p = 'cisco'
# apply for loop

for i in device_ip:
	print("Connect with device : ",i)
	client.connect(i, username=u, password=p, allow_agent=False, look_for_keys=False)
	#we have to ask for shell
	device_access = client.invoke_shell()
	# now sending command
	device_access.send("term len 0\n")
	device_access.send("show run\n")
	#device_access.send("show version\n")
	#time.sleep(0.5)
	#device_access.send("\n")
	time.sleep(0.5)
	#assume command got executed so lest recv data
	output= device_access.recv(65000)
	# decoding byte-like string into string
	#print(type(output))
	print(output.decode('ascii'))
	print("-------------")
	print("-------------")
	with open(i+time.ctime(), "w+") as f:
		f.write(output.decode('ascii'))
		time.sleep(1)