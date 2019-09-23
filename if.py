#!/usr/bin/python3

from time import ctime,sleep
from subprocess import getstatusoutput,getoutput,call
from os import mkdir
from os import path

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

elif int(choice) == 2:
	cmd = input("please enter any command : ")
	output = getoutput(cmd)
	print(output)

elif int(choice) == 3:
	d_name = input("enter directory name to create : ")
	while path.exists(d_name):
		call(['say', d_name+" directory name already exists. please enter a new name : "])
		#System Call to read the content in the brackets
		d_name = input("directory name already exists. please enter a new name : ")
	mkdir(d_name)
	print(d_name, " successfully created")
	call(['say', d_name+" succesfully created"])

elif choice == '5':
	web=input("enter website name to ping : ")
	print(getoutput("ping -c 5 "+web))
	
else:
	print("wrong option")