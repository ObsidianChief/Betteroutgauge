import kivy
kivy.require('1.1.0')


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup


#class RPM(GridLayout):


class MainMenu(GridLayout):
    info = StringProperty()

    def do_action(self):
        self.info.text = range(10000)

class HiddenPopUp(Popup):
    pass


class Display(App):
    title = "test of the emergency alert system"
    
    def build(self):
        return MainMenu()



if __name__ == '__main__':
    Display().run()  
