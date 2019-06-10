# JTSK-350112
# circle.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

"""
File: circle.py
Resources to manage circles
"""

import math

class Circle(object):
    """Represents Circle"""
    def __init__(self, radius = 1.0, color = "red"):
        """
            takes a float argument for radius and a string argument 
            for the color with the default values of 1.0 for the radius 
            and ”red” for the color. Radius and color are private members
        """
        self.__radius = float(radius)
        self.__color = str(color)
    
    def setRadius(self, radius):
        """Set new radius"""
        self.__radius = float(radius)

    def setColor(self, color):
        """Set new color"""
        self.__color = str(color)

    def getRadius(self):
        """Returns the radius of the circle"""
        return self.__radius

    def getColor(self):
        """Returns the color of the circle"""
        return self.__color

    def getArea(self):
        """Returns the are of the circle"""
        return math.pi * self.__radius * self.__radius

    def getPerimeter(self):
        """Returns the perimeter of the circle"""
        return 2 * math.pi * self.__radius

    def __add__(self, other):
        """Overloaded + operator. Returns the sum of areas"""
        return self.getArea() + other.getArea()
    
    def __sub__(self, other):
        """Overloaded - operator. Returns the the diff of areas"""
        return self.getArea() - other.getArea()
