#!/usr/bin/python3

import paramiko,time,sys

# using as ssh client
client = paramiko.SSHClient()
# auto adjust  host key verification with yes or no
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#time for connecting to remote ciscoIOS
address = sys.argv[1] #First argument as IP address
u =  sys.argv[2] #username as second argument
p =  sys.argv[3] #password as third argument
#connected with ssh session
client.connect(address, username=u, password=p, allow_agent=False, look_for_keys=False)
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
# now want to save output in a file
with open("csr100v.txt", "w+") as f:
	f.write(output.decode('ascii'))