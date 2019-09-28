# flake8: noqa

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
        self.test = NumericProperty()
        self.NTime = NumericProperty()
        self.Ncar = StringProperty()
        self.Nflags = NumericProperty()
        self.Ngear = StringProperty()
        self.Nplid = StringProperty()
        self.Nspeed = NumericProperty()
        self.Nrpm = NumericProperty(-1)
        self.Nturbo = NumericProperty()
        self.NengTemp = NumericProperty()
        self.Nfuel = NumericProperty()
        self.NoilPressure = NumericProperty()
        self.NoilTemp = NumericProperty()
        self.NdashLights = StringProperty()
        self.NshowLights = StringProperty()
        self.Nthrottle = NumericProperty()
        self.Nbrake = NumericProperty()
        self.Nclutch = NumericProperty()
        self.Ndisplay1 = StringProperty()
        self.Ndisplay2 = StringProperty()
        self.Nid = StringProperty()

        super(Test, self).__init__(**kwargs)

        #Clock.schedule_interval(self.op1, 0.5)
        Clock.schedule_interval(self.op2, 0.01)
        #Clock.schedule_interval(self, 0.01)

    def op1(self, _):
        self.data, addr = s.recvfrom(92)
        #dout = str(data)
        #t = data

        return self.data

        #datout = op1
    
    def op2(self, _=None):
        #datin = self.op1()
        #datin = str.encode()
        #data = decode(datin)
        #data = datin

        self.op1(_)
        Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id = struct.unpack('Bxxx4sHssfffffffBBfff16s16si', self.data)
        #self.test=str(int(self.test)+1)
        print(self.test)

    def update(self):
        pass

    #NDat = StringProperty(op2())
    #idat = rerun
    def build(self):
        return MainUI()

class MainUI(GridLayout):
    def build(self):
        pass

if __name__ == '__main__':
    Test().run()