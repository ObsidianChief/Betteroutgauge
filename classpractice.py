import socket
import time
import struct

#define Variables
ip = '127.0.0.1'
port = 4444

#set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip, port))

class prt:

    def __init__(self, data):
        self.f=data
    
while True:
    info, addr=s.recvfrom(92)
    t=prt(info)
    #print(t.f)
    abc = t.f
    print(abc)