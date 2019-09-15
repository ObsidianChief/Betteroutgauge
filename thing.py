import kivy
kivy.require('1.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.event import EventDispatcher

import string
import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sb = s.bind(('127.0.0.1', 4444))


class Test(App):
    title = "This is only a test"

    def __init__(self, **kwargs):
        self.data = ''
        NTime = NumericProperty()
        Ncar = StringProperty()
        Nflags = NumericProperty()
        Ngear = StringProperty()
        Nplid = StringProperty()
        Nspeed = NumericProperty()
        Nrpm = NumericProperty()
        Nturbo = NumericProperty()
        NengTemp = NumericProperty()
        Nfuel = NumericProperty()
        NoilPressure = NumericProperty()
        NoilTemp = NumericProperty()
        NdashLights = StringProperty()
        NshowLights = StringProperty()
        Nthrottle = NumericProperty()
        Nbrake = NumericProperty()
        Nclutch = NumericProperty()
        Ndisplay1 = StringProperty()
        Ndisplay2 = StringProperty()
        Nid = StringProperty()
        super(Test, self).__init__(**kwargs)

    def op1(self):
        data, addr = s.recvfrom(92)
        #dout = str(data)
        t = data

        return t

    datout = op1
    
    def op2(self):
        datin = Test.op1
        #datin = str.encode()
        #data = decode(datin)
        data = datin
        Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id = struct.unpack('Bxxx4sHssfffffffBBfff16s16si', data)
    
    Clock.schedule_interval(op1, 0.5)
    Clock.schedule_interval(op2, 0.5)
    NDat = StringProperty(op1)

    def build(self):
        return MainUI()


class MainUI(GridLayout):

    pass

#    op1 = data, addr = s.recvfrom(92)
#    op2 = Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id = struct.unpack('Bxxx4sHssfffffffBBfff16s16si', data)
    
    #NTime = NumericProperty(op2.Time)
    #Ncar = StringProperty(op2.car)
    #Nflags = NumericProperty(op2.flags)
    #Ngear = StringProperty(op2.gear)
    #Nplid = StringProperty(op2.plid)
    #Nspeed = NumericProperty(op2.speed)
    #Nrpm = NumericProperty(op2.rpm)
    #Nturbo = NumericProperty(op2.turbo)
    #NengTemp = NumericProperty(op2.engTemp)
    #Nfuel = NumericProperty(op2.fuel)
    #NoilPressure = NumericProperty(op2.oilPressure)
    #NoilTemp = NumericProperty(op2.oilTemp)
    #NdashLights = StringProperty(op2.dashLights)
    #NshowLights = StringProperty(op2.showLights)
    #Nthrottle = NumericProperty(op2.throttle)
    #Nbrake = NumericProperty(op2.brake)
    #Nclutch = NumericProperty(op2.clutch)
    #Ndisplay1 = StringProperty(op2.display1)
    #Ndisplay2 = StringProperty(op2.display2)
    #Nid = StringProperty(op2.id)


if __name__ == '__main__':
    Test().run()
