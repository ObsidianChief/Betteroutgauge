import socket
import time 
ptr=open("Spoofer.txt", "a+")
LAN=False
Read=True
Write=False
#build a socket to sniff data with toggle
while LAN==True:
    s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
    s.bind (("127.0.0.1", 4444))
#write function with toggle
while Write==True:
        data, addr=s.recvfrom(92)
        if data:
            datastr = str(data)
            ptr.writelines(datastr,end = "\n")
#read function function with toggle
while Read==True:
    print=ptr.readline()
    print



#else print("Error")