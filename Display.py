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

class Main(App):
    def build(self):
        return MainUI()

class MainUI(GridLayout):
    title = "This is only a test"

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
#    button.pressed = false

    def __init__(self, **kwargs):
        super(MainUI, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 0.01)

    def update(self, _=None):
#        DONT DECOMMENT THIS, IT WILL BREAK THE LOOP AND RETURN 0
#        if button.pressed:
#        data, addr = s.recvfrom(92)
#        return data

        data, addr = s.recvfrom(92)
        Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id = struct.unpack('Bxxx4sHssfffffffBBfff16s16si', data)

        self.NTime=str(Time)
        self.Ncar=str(car)
        self.Nflags=str(flags)
        self.Ngear=str(gear)
        self.Nplid=str(plid)
        self.Nspeed=str(speed)
        self.Nrpm=str(rpm)
        self.Nturbo=str(turbo)
        self.NengTemp=str(engTemp)
        self.Nfuel=str(fuel)
        self.NoilPressure=str(oilPressure)
        self.NoilTemp=str(oilTemp)
        self.NdashLights=str(dashLights)
        self.NshowLights=str(showLights)
        self.Nthrottle=str(throttle)
        self.Nbrake=str(brake)
        self.Nclutch=str(clutch)
        self.Ndisplay1=str(display1)
        self.Ndisplay2=str(display2)
        self.Nid=str(id)

if __name__ == '__main__':
    Main().run()