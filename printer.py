import socket
import struct
#import sys
#import time
pt = open("Spoofer", "br+")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 4444))
if True:
#build a socket to sniff data with toggle:
    while True:
        data, addr=s.recvfrom(92)
        if data:
            Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id =  struct.unpack('Bxxx4sHssfffffffBBfff16s16si', data)
            pt.write(struct.pack('Bxxx4sHssfffffffBBfff16s16si', Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id))
            
            
            
            #pt.write(data)
            #datastr = str(data)
            #pt.writelines(datastr)
            #pt.write("\n")