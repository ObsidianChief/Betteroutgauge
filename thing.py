import kivy
kivy.require('1.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput

import socket


class Test(App):
    title = "This is only a test"

    def build(self):
        return MainUI()


class datcol:
    def __init__(self, data):
        self.data = UDPconnect.s.recvfrom(92)


class UDPconnect:

    def __init__(self, s, sb):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sb = s.bind(('127.0.0.1', 4444))


print(datcol.data)


class Dtn:
    pass


#Dtn.dtime = Time
#Dtn.dcar = car
#Dtn.dflags = flags
#Dtn.dgear = gear
#Dtn.dplid = plid
#Dtn.dspeed = speed
#Dtn.drpm = rpm
#Dtn.dturbo = turbo
#Dtn.dengtemp = engTemp
#Dtn.dfuel = fuel
#Dtn.doilPressure = oilPressure
#Dtn.doilTemp = oilTemp
#Dtn.ddashLights = dashLights
#Dtn.dshowLights = showLights
#Dtn.dthrottle = throttle
#Dtn.dbrake = brake
#Dtn.dclutch = clutch
#Dtn.ddisplay1 = display1
#Dtn.ddisplay2 = display2
#Dtn.did = id


class MainUI(GridLayout):
    pass


if __name__ == '__main__':
    Test().run()
