from LinkedList import *
class Monom:
    def __init__(self, coefficient=float, power=int):
        assert power >= 0
        self._coef = coefficient
        self._pow = power
    def __str__(self):
        if(self._pow > 1):
            return "%.2fx^%d" % (self._coef, self._pow)
        elif(self._pow > 0):
            return "%.2fx" % (self._coef)
        else:
            return "%.2f" % (self._coef)
    def __mul__(self, toAdd):
        if(self._coef == 0 or toAdd.get_coef() == 0):
            return Monom(0, 0)
        return Monom(self._coef * toAdd.get_coef(), self._pow + toAdd.get_pow())
    def get_coef(self):
        return self._coef
    def set_coef(self, coefficient):
        self._coef = coefficient
    def get_pow(self):
        return self._pow
    def set_pow(self, power):
        self._pow = power