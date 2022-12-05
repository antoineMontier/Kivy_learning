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

class MenuScreen(Widget):
    promptObject = TextInput()


class MyGrid(Widget):
    

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.p = Polynom()
        self.python_polynome_display.text = str(self.p)
        self.python_polynome_min_out.text = str(self.p.min)
        self.python_polynome_max_out.text = str(self.p.max)
        self.python_polynome_pace_out.text = str(self.p.precision)

    def min_uptdate(self):
        if(self.python_polynome_min_in.text[0] not in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']):#error handling
            return
        self.p.min = float(self.python_polynome_min_in.text)
        self.python_polynome_min_in.text = ""
        self.python_polynome_min_out.text = str(self.p.min)
        
    def max_uptdate(self):
        if(self.python_polynome_max_in.text[0] not in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']):#error handling
            return
        self.p.max = float(self.python_polynome_max_in.text)
        self.python_polynome_max_in.text = ""
        self.python_polynome_max_out.text = str(self.p.max)

    def pace_uptdate(self):
        if(self.python_polynome_pace_in.text[0] not in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']):#error handling
            return
        self.p.precision = float(self.python_polynome_pace_in.text)
        self.python_polynome_pace_in.text = ""
        self.python_polynome_pace_out.text = str(self.p.precision)
    
    def tangent_uptdate(self):
        if(self.python_polynome_tangent_in.text[0] not in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']):#error handling
            return
        a = float(self.python_polynome_tangent_in.text)
        #self.python_polynome_tangent_in.text = ""#don't clear input box
        self.python_polynome_tangent_out.text = str(self.p.tangent(a))
    

class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def build(self):
        return MyGrid()
    

if __name__ == '__main__':
    MyApp().run()

