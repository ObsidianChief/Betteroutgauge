import struct
import socket
import time
#import bytesio
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
port = 4444
#n = 1
#b = Bytesio()
f = open("Spoofer", "br")
while True:
    data = f.read(92)
    time.sleep(0.02)
    print(data)
    s.sendto(data,(ip,port))