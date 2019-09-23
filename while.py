#!/usr/bin/python3
#!/usr/local/bin/Python3

from time import sleep
from threading import Thread

def firstfunction():
	while 5 > 3 :
		print ("Hello world")
		sleep(2)

def secondfunction():
	while True:
		print("execute me plz....")
		sleep(2)

thread1 = Thread(target=firstfunction)
thread1.start()
sleep(1)
thread2 = Thread(target=secondfunction)
thread2.start()