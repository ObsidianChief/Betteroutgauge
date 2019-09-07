import socket
#import sys
#import time
pt = open("Spoofer.txt", "a+")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 4444))
if True:
#build a socket to sniff data with toggle:
    while True:
        data, addr=s.recvfrom(92)
        if data:
            datastr = str(data)
            pt.writelines(datastr)
            pt.write("\n")