# JTSK-350112
# complex.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

class Complex(object):
    """
        Handles operations with complex numbers
    """

    def __init__(self, re = 0, im = 0):
        """Constructor"""
        self._re = re
        self._im = im

    def __add__(self, other):
        """finds the sum of two complex numbers"""
        result = Complex(self._re + other._re, self._im + other._im)
        return result

    def __sub__(self, other):
        """finds the difference between two complex numbers"""
        result = Complex(self._re - other._re, self._im - other._im)
        return result

    def __mul__(self, other):
        """finds the product of two complex numbers"""
        result = Complex((self._re * other._re - self._im * other._im), \
            (self._re * other._im + self._im * other._re))
        return result

    def __truediv__(self, other):
        """finds the quotient of two numbers"""
        result = Complex(((self._re * other._re + self._im * other._im) / \
            (other._re ** 2 + other._im ** 2)),\
            ((self._im * other._re - self._re * other._im) / \
            (other._re ** 2 + other._im ** 2)))
        return result
    
    def __eq__(self, other):
        """shows if the complex numbers are equal"""
        return self._re == other._re and self._im == other._re

    def __ne__(self, other):
        """show if the complex numbers are not equal"""
        return self._re != other._re or self._im != other._re

    def __str__(self):
        """
            returns the complex number
        """
        if self._im == 0:
            result = str(self._re)
        elif self._im >= 0:
            if self._im == 1:
                result = str(self._re) + "+i"
            else:
                result = str(self._re) + "+" + str(self._im) + "i"
        else:
            if self._im == -1:
                result = str(self._re) + "-i"
            else:
                result = str(self._re) + str(self._im) + "i"
        return result