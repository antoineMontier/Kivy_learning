import kivy, random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

kivy.require('1.9.0')

class MyGrid(Widget):
    def print_a_number(self):
        print(random.randint(0, 100))
    pass

class MyApp(App):
    def build(self):
        return MyGrid()

    


MyApp().run()