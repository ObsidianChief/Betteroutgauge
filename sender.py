# flake8: noqa
import socket
import struct
import random
import time
from itertools import cycle
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
ip = "127.0.0.1"
port = 4444
class car:
    def __init__(self):
        self.Time=0
        self.car1="beam"
        self.flag=49152                     
        self.gear=0
        self.plid=0
        self.speed=0
        self.rpm=0
        self.turbo=0
        self.engTemp=0
        self.fuel=0
        self.oilPressure=0
        self.oilTemp=0
        self.dashLights=0
        self.showLights=0
        self.throttle=0
        self.brake=0
        self.clutch=0
        self.display1=0
        self.display2=0
        self.id="big dum"
        data = struct.pack('Bxxx4sHssfffffffBBfff16s16si',Time, car1, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2)
        s.sendto(data(92),(ip,port))

        self.__iter=0

        @property
        def iter(self):
            if self.__iter>150:
                self.__iter=0
            return self.__iter


    def sweeper(self):
        #return
        self.gear=self.__iter%6
        self.speed=(0.005*self.__iter)
        self.rpm=self.__iter
        self.engTemp=(100+self.__iter)
        self.fuel=(1-(self.__iter/1000))
        self.oilTemp=(100+1.05(self.__iter))

        self.__iter+=1


    def export(self):
        #return
        self.Time
        self.car1
        self.flag
        self.gear
        self.plid
        self.speed
        self.rpm
        self.turbo
        self.engTemp
        self.fuel
        self.oilPressure
        self.oilTemp
        self.dashLights
        self.showLights
        self.throttle
        self.brake
        self.clutch
        self.display1
        self.display2
        self.id
        data = struct.pack('Bxxx4sHssfffffffBBfff16s16si',Time, car1, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2)
        s.sendto(data(92),(ip,port))

#this is a test of the git integration software