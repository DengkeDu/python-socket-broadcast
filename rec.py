from socket import *
s=socket(AF_INET, SOCK_DGRAM)
s.bind(('',12345))
while 1:
    m=s.recvfrom(1024)
    print m[0]
