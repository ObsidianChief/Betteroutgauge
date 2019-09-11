

import socket
import time
import struct
from collections import namedtuple
import kivy
kivy.require('1.1.0')
#building socket
s = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 4444))
#main function

class MainFunction:

    def __init__(self, data):
        self.d=data



from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup


class Display(App):
    title = "test of the emergency alert system"
    
    def build(self):
        return MainMenu()


class MainMenu(GridLayout):
    info = StringProperty()
    rpmout = ObjectProperty(None)

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

mf=MainFunction(rpm)
mf.d

    def do_action(self):
        self.info.text = mf.d


if __name__ == '__main__':
    Display().run()  

