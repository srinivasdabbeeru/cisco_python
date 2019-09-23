#!/usr/bin/python3

from subprocess import getoutput
import sys
data = sys.argv[1:]

for i in data :
	print("PING  request for server : "+i)
        print(getoutput("ping -c 3 "+i))
        print("____________________")
        print("--------------------")

print(sum)
