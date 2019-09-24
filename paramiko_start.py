#!/usr/bin/python3

import paramiko,time

# using as ssh client
client = paramiko.SSHClient()
# auto adjust  host key verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#time for connecting to remote ciscoIOS
address = input("Enter your router IP : ")
u =  "root"
p = "cisco"
client.connect(address, username=u, password=p, allow_agent=False, look_for_keys=False)
#we have to ask for shell
device_access = client.invoke_shell()
# now sending command
device_access.send("show ip int br\n")
time.sleep(0.15)
#assume command got executed so lest recv data
output= device_access.recv(65000)
# decoding byte-like string into string
#print(type(output))
print(output.decode('ascii'))