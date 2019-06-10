# JTSK-350112
# circle.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

"""
File: test_circle.py
Test Circle class
"""

from circle import Circle

# create a new Circle
myCircle1 = Circle(10, "black")
myCircle2 = Circle()
myCircle3 = Circle()

# test Setters
myCircle3.setColor("yellow")
myCircle3.setRadius(15)

# test Getters
print("Circle 1:")
print("Radius = {}, Color = {}". \
    format(myCircle1.getRadius(), myCircle1.getColor()))
print("Perimeter = {}, Area = {}".\
    format(myCircle1.getPerimeter(), myCircle1.getArea()))

print("Circle 2:")
print("Radius = {}, Color = {}".\
    format(myCircle2.getRadius(), myCircle2.getColor()))
print("Perimeter = {}, Area = {}".\
    format(myCircle2.getPerimeter(), myCircle2.getArea()))

print("Circle 3:")
print("Radius = {}, Color = {}".\
    format(myCircle3.getRadius(), myCircle3.getColor()))
print("Perimeter = {}, Area = {}".\
    format(myCircle3.getPerimeter(), myCircle3.getArea()))

# test overloaded operators
print("Test +")
print("Circle 1 + Circle 2 = {}".format(myCircle1 + myCircle2))

print("Test -")
print("Circle 1 - Circle 2 = {}".format(myCircle1 - myCircle2))
