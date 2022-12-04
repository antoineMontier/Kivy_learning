import kivy, random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from Polynom import *

kivy.require('1.9.0')

class MyGrid(Widget):
    python_polynome_min = ObjectProperty(None)
    python_polynome_max = ObjectProperty(None)
    python_polynome_pace = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.p = Polynom()
        self.python_polynome_display.text = str(self.p)
        self.python_polynome_min.text = str(self.p.min)
        self.python_polynome_max.text = str(self.p.max)
        self.python_polynome_pace.text = str(self.p.precision)

    def min_uptdate(self):
        self.p.min = float(self.python_polynome_min.text)
        self.python_polynome_min.text = str(self.p.min)
        

    def max_uptdate(self):
        self.p.max = float(self.python_polynome_max.text)
        self.python_polynome_max.text = str(self.p.max)

    def pace_uptdate(self):
        self.p.precision = float(self.python_polynome_pace.text)
        self.python_polynome_pace.text = str(self.p.precision)
    

class MyApp(App):

    def build(self):
        return MyGrid()
    



MyApp().run()