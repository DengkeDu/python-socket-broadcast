from socket import *

s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while 1:
    s.sendto('testing',('255.255.255.255',12345))
