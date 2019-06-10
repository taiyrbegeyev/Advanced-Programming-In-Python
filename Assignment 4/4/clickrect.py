# JTSK-350112
# clickrect.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from graphics import *
import math

def perimeter(length, width):
    """compute the perimeter of the rectangle""" 
    return 2 * (length + width)

def area(length, width):
    """Compute the area of the rectangle"""
    return (length * width)


def main():
    win = GraphWin("Rectangle by click", 400, 400)

    corner_1 = win.getMouse()
    corner_2 = win.getMouse()

    # create a rectangle with given points
    rect = Rectangle(Point(corner_1.getX(), corner_1.getY()), 
        Point(corner_2.getX(), corner_2.getY()))

    rect.setFill("yellow")
    # draw rectangle
    rect.draw(win)
    # determine rectangle's width and length
    length = abs(corner_2.getX() - corner_1.getX())
    width = abs(corner_2.getY() - corner_1.getY())
    # compute perimeter and area, and print them
    label = Text(Point(175, 350), "Perimeter = {}\nArea = {}"
        .format(perimeter(length, width), area(length, width)))
    label.draw(win)

    win.getMouse()
    win.close()

main()