#!/usr/bin/python3

from napalm import get_network_driver

device1 = get_network_driver('ios')
#connecting to device
device=device1('192.168.90.146','root','cisco')
print([i for i in dir(device) if 'load' in i])
#open session with device
device.open()
#merging configuration
print(device.load_merge_candidate(filename='/Users/sdabbeer/Documents/GitHub/cisco_python/input_commands.txt'))
# check the diff
print(device.compare_config())

#now to commit the applied configuration

c=input("Confirm with y|n to apply configuration ; ")

if c == 'y' or c =='Y' :
	print("Committing the configuration ")
	device.commit_config()
	res = input("Do you want to rollback changes : y|n")
	if res == 'y' or res == 'Y':
		device.rollback()
	else:
		print("no rollbacks applied")
elif c == 'n' or c == 'N' :
	print("Discarding the configuration ")
	device.discard_config()
else:
	print("please type only y or n")
	
#close connection as well
device.close()