#!/usr/bin/python3

import sys
from time import sleep
import math
'''
x=input("type number : ")
print(x)
'''

import sys
data = sys.argv[1:]

sum=0
for i in data :
	sum = sum + int(i)

print(sum)