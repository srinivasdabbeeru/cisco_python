#!/usr/bin/python3

import requests
from requests.auth import HTTPBasicAuth

cred=HTTPBasicAuth('root', 'cisco')


#h={'Accept':'application/json'}
h={'Accept':'text/html'}
# defining data from that API in JSON format
url="http://192.168.90.146/level/15/exec/-/show/ip/interface/brief/CR"

#Now connection to restconf OT http protocol
output=requests.get(url,headers=h,auth=cred)

print(output)
# only giving http response code

print(output.text)
#giving HTML Based repsonse