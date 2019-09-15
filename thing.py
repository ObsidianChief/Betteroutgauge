import kivy
kivy.require('1.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.event import EventDispatcher

import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sb = s.bind(('127.0.0.1', 4444))


class Test(App):
    title = "This is only a test"

    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

    def build(self):
        return MainUI()


class MainUI(GridLayout):

    op1 = data, addr = s.recvfrom(92)
    op2 = Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id = struct.unpack('Bxxx4sHssfffffffBBfff16s16si', data)
    Clock.schedule_interval(op1, 0.5)
    Clock.schedule_interval(op2, 0.5)
    NTime = NumericProperty(Time)
    Ncar = StringProperty(car)
    Nflags = NumericProperty(flags)
    Ngear = StringProperty(gear)
    Nplid = StringProperty(plid)
    Nspeed = NumericProperty(speed)
    Nrpm = NumericProperty(rpm)
    Nturbo = NumericProperty(turbo)
    NengTemp = NumericProperty(engTemp)
    Nfuel = NumericProperty(fuel)
    NoilPressure = NumericProperty(oilPressure)
    NoilTemp = NumericProperty(oilTemp)
    NdashLights = StringProperty(dashLights)
    NshowLights = StringProperty(showLights)
    Nthrottle = NumericProperty(throttle)
    Nbrake = NumericProperty(brake)
    Nclutch = NumericProperty(clutch)
    Ndisplay1 = StringProperty(display1)
    Ndisplay2 = StringProperty(display2)
    Nid = StringProperty(id)


if __name__ == '__main__':
    Test().run()
