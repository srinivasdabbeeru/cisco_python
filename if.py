#!/usr/bin/python3

from time import ctime,sleep
from subprocess import getstatusoutput,getoutput

#only importing desired dunctions

options='''
press 1 to check current date and time:
press 2 to run any command in your current os:
press 3 to create a directory:
press 4 to start a train:
press 5 to ping any website:
'''
print(options)
# to capture input from user
choice=input()
print ("you have chosen ", choice)

#conditional statement with if

if choice == '1':
	print(ctime())
else:
	print("wrong option")