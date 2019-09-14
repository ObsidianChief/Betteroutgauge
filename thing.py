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
data, addr = s.recvfrom(92)
Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id = struct.unpack('Bxxx4sHssfffffffBBfff16s16si', data)


class Test(App):
    Ttitle = "This is only a test"
    TTime = NumericProperty(Time)
    Tcar = StringProperty(car)
    Tflags = NumericProperty(flags)
    Tgear = StringProperty(gear)
    Tplid = StringProperty(plid)
    Tspeed = NumericProperty(speed)
    Trpm = NumericProperty(rpm)
    Tturbo = NumericProperty(turbo)
    TengTemp = NumericProperty(engTemp)
    Tfuel = NumericProperty(fuel)
    ToilPressure = NumericProperty(oilPressure)
    ToilTemp = NumericProperty(oilTemp)
    TdashLights = StringProperty(dashLights)
    TshowLights = StringProperty(showLights)
    Tthrottle = NumericProperty(throttle)
    Tbrake = NumericProperty(brake)
    Tclutch = NumericProperty(clutch)
    Tdisplay1 = StringProperty(display1)
    Tdisplay2 = StringProperty(display2)
    Tid = StringProperty(id)

    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

#    def unpacker(self, data=bytes):
#        Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id = struct.unpack('Bxxx4sHssfffffffBBfff16s16si', data)

    def build(self):
        return MainUI()


class MED(EventDispatcher):
    T = Test()
    MTime = NumericProperty(T.Time)
    Mcar = StringProperty(T.Tcar)
    Mflags = NumericProperty(T.Tflags)
    Mgear = StringProperty(T.Tgear)
    Mplid = StringProperty(T.Tplid)
    Mspeed = NumericProperty(T.speed)
    Mrpm = NumericProperty(T.Trpm)
    Mturbo = NumericProperty(T.Tturbo)
    MengTemp = NumericProperty(T.TengTemp)
    Mfuel = NumericProperty(T.Tfuel)
    MoilPressure = NumericProperty(T.ToilPressure)
    MoilTemp = NumericProperty(T.ToilTemp)
    MdashLights = StringProperty(T.TdashLights)
    MshowLights = StringProperty(T.TshowLights)
    Mthrottle = NumericProperty(T.Tthrottle)
    Mbrake = NumericProperty(T.Tbrake)
    Mclutch = NumericProperty(T.Tclutch)
    Mdisplay1 = StringProperty(T.Tdisplay1)
    Mdisplay2 = StringProperty(T.Tdisplay2)
    Mid = StringProperty(T.Tid)

    def on_Mrpm(self, instance, value):
        app = App.get_running_app()
        app.rpm1.text = str(rpm)


class MainUI(GridLayout):
#    t = Test()
#    rout = t.rpm
    rpm1 = MED.Mrpm


if __name__ == '__main__':
    Test().run()
