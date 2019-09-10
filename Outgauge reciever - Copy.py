# flake8: noqa
import socket
import time
import struct
from collections import namedtuple
#building socket
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 4444))
#main function
while True:
    data, addr=s.recvfrom(92)
    if data:
        #struct.unpack('BsHssfffffffBBffssi', data)
        #this part first declares the variable names, then unpacks the packet (data) according to the template.
        Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id =  struct.unpack('Bxxx4sHssfffffffBBfff16s16si', data)

        #This part converts the outputs from euro to burger units.
        oilTempconv = (oilTemp * 1.8 + 32 )
        engTempconv = (engTemp * 1.8 + 32 )
        speedconv = (speed / 0.44704 )
        #Convert conversion outputs to strings so they can be truncated.
        rpmstring = str(rpm)
        speedstring = str(speedconv)
        engTempstring = str(engTempconv)
        #Truncate values to be 4 numbers, plus the decimal point. Must be truncated to [:5] to work right. Decimal point moves automatically
        speedOut = speedstring [:5]
        engTempOut = engTempstring [:5]
        rpmOut = rpmstring [:6]

    #print("Speed (M/S)", speed, "M/S", end="\r", flush=True)
    print("Speed (MPH)", speedOut, "MPH","Coolant", engTempOut, "F",rpmOut,"RPM",end="\r",  flush=True)
    #print(rpmOut,"RPM", end=" \r", flush=True) 
    #print("Oil Temp C", oilTemp, "C", flush=True)
    #print("Oil Temp F", oilTempOut, "F", flush=True)
    #print("Coolant C", engTemp, "C", flush=True)
    #print("Coolant", engTempOut, "F",end="\r", flush=True) 


      #print ("[",data,"]")
      #time.sleep(0)
else:
  print("error")




