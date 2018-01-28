#!/usr/bin/python

#small script to receive current ip address and send a message to broadcast address of the network.

# import socket
# hostname=socket.gethostname()
# IPAddr=socket.gethostbyname(hostname)
# print("Your Computer Name is:"+hostname)
# print("Your Computer IP Address is:"+IPAddr)

# flag sent to broadcast address
from socket import *
cs = socket(AF_INET, SOCK_DGRAM)
cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
cs.sendto('Flag1{base64=}', ('<broadcast>', 54545))
print("flag sent")

