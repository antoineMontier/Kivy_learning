import kivy, random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from parse import *
from kivy.properties import ObjectProperty
from Polynom import *

kivy.require('1.9.0')

class MenuScreen(Widget):
    promptObject = TextInput()

def parse_number(text):
    if text.replace(".", "", 1).isdigit():
        return float(text)

class MyGrid(Widget):
    

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.prev_im = 0.0
        self.p = Polynom()
        self.python_polynome_min_out.text = "min\n" + str(self.p.min)
        self.python_polynome_max_out.text = "max\n" + str(self.p.max)
        self.python_polynome_pace_out.text = "pace\n"+ str(self.p.precision)

    def min_uptdate(self):
        if(self.python_polynome_min_in.text == "" or self.python_polynome_min_in.text[0] not in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '-']):#error handling
            return
        self.p.min = float(self.python_polynome_min_in.text)
        self.python_polynome_min_in.text = ""
        self.python_polynome_min_out.text = "min\n" + str(self.p.min)
        
    def max_uptdate(self):
        if(self.python_polynome_max_in.text == "" or self.python_polynome_max_in.text[0] not in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0', '-']):#error handling
            return
        self.p.max = float(self.python_polynome_max_in.text)
        self.python_polynome_max_in.text = ""
        self.python_polynome_max_out.text = "max\n" + str(self.p.max)

    def pace_uptdate(self):
        if(self.python_polynome_pace_in.text == "" or self.python_polynome_pace_in.text[0] not in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']):#error handling
            return
        self.p.precision = float(self.python_polynome_pace_in.text)
        self.python_polynome_pace_in.text = ""
        self.python_polynome_pace_out.text = "pace\n"+ str(self.p.precision)
    
    def tangent_uptdate(self):
        if(self.python_polynome_tangent_in.text == "" or self.python_polynome_tangent_in.text[0] not in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']):#error handling
            return
        a = float(self.python_polynome_tangent_in.text)
        #self.python_polynome_tangent_in.text = ""#don't clear input box
        self.python_polynome_tangent_out.text = str(self.p.tangent(a))

    def polynom_uptdate(self):
        if(self.python_polynome_in.text == "" or self.python_polynome_in.text[0] not in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0', 'x', '-', '+']):#error handling
            return
        s_p = self.python_polynome_in.text
        #self.python_polynome_in.text = ""
        self.p.reset()
        #read polynom.....
        a = b = 0.0
        tmp = ""
        readExp = False
        positive = True
        #s_p += " "
        for i in s_p:
            if i in ['+', '-']:
                s_p=s_p.replace(i," "+i+" ")
        if ' ' in s_p:
            arr = s_p.split(" ")
        else:
            arr = [s_p]
        print(arr)
        for exp in arr:
            #8 possibilities : - + XXxXX XXx xXX x XX ' '
            if(exp == ' ' or exp == ''):                #' '
                continue
            elif(exp == '+'):                           #-
                positive = positive
            elif(exp == '-'):                           #+
                positive = not positive
            elif not 'x' in exp and exp.replace(".", "", 1).isdigit():      #XX
                tab = parse("{a:Number}", exp, dict(Number=parse_number))
                if(positive):
                    self.p.add(tab['a'], 0)
                    positive = True
                else:
                    self.p.add(-tab['a'], 0)
                    positive = True
            elif 'x' in exp and len(exp) == 1:          #x
                if(positive):
                    self.p.add(1, 1)
                    positive = True
                else:
                    self.p.add(-1, 1)
                    positive = True
            elif 'x' in exp and exp[0] == 'x':          #xXX
                tab = parse("x{b:Number}", exp, dict(Number=parse_number))
                if(positive):
                    self.p.add(1, tab['b'])
                    positive = True
                else:
                    self.p.add(-1, tab['b'])
                    positive = True
            elif 'x' in exp and exp[len(exp)-1] == 'x': #XXx
                tab = parse("{a:Number}x", exp, dict(Number=parse_number))
                if(positive):
                    self.p.add(tab['a'], 1)
                    positive = True
                else:
                    self.p.add(-tab['a'], 1)
                    positive = True
            elif 'x' in exp:                            #XXxXX
                tab = parse("{a:Number}x{b:Number}", exp, dict(Number=parse_number))
                if(positive):
                    self.p.add(tab['a'], tab['b'])
                    positive = True
                else:
                    self.p.add(-tab['a'], tab['b'])
                    positive = True

        self.p.clean()
        self.python_polynome_out.text = "f(x) = " + str(self.p)
        self.python_polynome_derivate_out.text = "f'(x) = " + str(self.p.derivate())
        self.python_polynome_primitive_out.text = "F(x) = " + str(self.p.primitive())
        self.python_polynome_even_out.text = str(self.p.even())
        self.python_polynome_uneven_out.text = str(self.p.uneven())

    def show_roots(self):
        if(self.prev_im != self.p.evaluate(-0.23551569)):#avoid recalculation
            self.python_polynome_roots_out.text = "roots : " + str(self.p.roots())
            self.prev_im = self.p.evaluate(-0.23551569)

    def evaluation(self):
        txt = self.python_polynome_im_in.text
        if(not txt.replace(".", "", 1).replace("-", "", 1).isdigit()):#error handling
            return
        x = float(txt)
        self.python_polynome_im_in.text = ""
        self.python_polynome_im_out.text = ") = " +  str(self.p.evaluate(x))

    def integral_calculation(self):
        a = self.python_polynome_a_in.text
        b = self.python_polynome_b_in.text
        if(not a.replace(".", "", 1).replace("-", "", 1).isdigit()):#error handling
            return
        if(not b.replace(".", "", 1).replace("-", "", 1).isdigit()):#error handling
            return
        x = float(a)
        y = float(b)
        self.python_polynome_integral_out.text = str(self.p.integral(x, y))

class MyApp(App):

    button = [0.411, 0.47, 0.68]
    on_bg_font_color = [0, 1, 0, 1]
    on_button_font_color = [1, 1, 0, 1]
    on_layout_font_color = [1, 0, 1, 1]
    label_color = [0, 0, 0, 1]
    text_input_fg_color = [0, 1, 0.5, 1]
    text_input_bg_color = [0.5, 0, 0.5, 1]
    button_color = [0.5, 0, 0.5, 1]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def build(self):
        Window.clearcolor = (1, 0, 1, 1)#bg color
        return MyGrid()
    

if __name__ == '__main__':
    MyApp().run()

