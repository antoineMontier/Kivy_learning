import kivy, random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

kivy.require('1.9.0')

class Myroot(BoxLayout):
    def __init__(self, **kwargs):
        super(Myroot, self).__init__(**kwargs)

        
        
    def generate_number(self):
        self.python_random.text = str(random.randint(0, 10))


class RandomNumber(App):
    def build(self):
        return Myroot()

rn = RandomNumber()
rn.run()