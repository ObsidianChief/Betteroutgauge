import kivy
kivy.require('1.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

import socket
import struct


class breakdown:

    def __init__(self, Time=0, car='', flags=0, gear=0, plid='', speed=0, rpm=0, turbo=0, engTemp=0, fuel=0, oilPressure=0, oilTemp=0, dashLights=0, showLights=0, throttle=0, brake=0, clutch=0, display1='', display2='', id=0):
        self.Time = Time
        self.car = car
        self.flags = flags
        self.gear = gear
        self.plid = plid
        self.speed = speed
        self.rpm = Time
        self.turbo = turbo
        self.engTemp = engTemp
        self.fuel = fuel
        self.oilPressure = oilPressure
        self.oilTemp = oilTemp
        self.dashLights = dashLights
        self.showLights = showLights
        self.throttle = throttle
        self.brake = brake
        self.clutch = clutch
        self.display1 = display1
        self.display2 = display2
        self.id = id

#    while True:
    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('127.0.0.1', 4444))

    def data_in(self, data):
        self.data

    def collect(self):
        self.data, addr=self.s.recvfrom(92)

    def unpack(self, data):
        Time, car, flags, gear, plid, speed, rpm, turbo, engTemp, fuel, oilPressure, oilTemp, dashLights, showLights, throttle, brake, clutch, display1, display2, id = struct.unpack('Bxxx4sHssfffffffBBfff16s16si', data)


class Test(App):
    title = "This is only a test"
    bk = breakdown()
#    info = breakdown.rpm
    rpmstr = str(bk.rpm)
    info = rpmstr
    bk = ObjectProperty(None)
#    trg1 = Clock.create_trigger(breakdown().connect())
#    trg1()
    breakdown().connect()
    Clock.schedule_interval(breakdown().collect, 1/60)
    Clock.schedule_interval(breakdown().unpack, 1/60)
    print(info)
    def build(self):
        return MainUI()


class Dtn:
    pass


class MainUI(GridLayout):
    pass


if __name__ == '__main__':
    Test().run()
