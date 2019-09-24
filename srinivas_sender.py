#!/usr/bin/python3

import socket,time
# checking for socket functions

print([i for i in dir(socket) if 'socket' in i])

# now creating udp socket
#ipv4 socket -- ipv4 + 2 byte port
#ipv6 socket -- ipv6 + 2 byte port

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#             for IPv4,      for UDP socket)

#socket.socket(socket.AF_INET,socket.SOCK_STREAM) # for tcp

###
while True:
    #enter message
    msg = input("enter data to send : ")
    #coverting data into byte-like string format
    newmsg = msg.encode('ascii')
    #lets send data to target
    s.sendto(newmsg,("127.0.0.1",8894))
    data = s.recvfrom(1000)
    Data_received= data[0] # here 1000 is the buffer size.
    print(Data_received)

s.close()
