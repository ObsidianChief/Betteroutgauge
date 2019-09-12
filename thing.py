import kivy
kivy.require('1.1.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.textinput import TextInput

class Test(App):
    title = "This is only a test"

    def build(self):
        return MainUI()

class MainUI(GridLayout):
    pass

if __name__ == '__main__':
    Test().run()
