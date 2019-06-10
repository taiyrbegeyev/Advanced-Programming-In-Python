# JTSK-350112
# appropi.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from graphics import *
from random import randrange

def main():
    print("Enter the length of the window")
    d = int(input())
    # create a square window with the side length of d (400x400).
    win = GraphWin("Approximate Pie", d, d)
    # repeatedly create and draw 10000 random points
    counter = 0
    for i in range(1, 10001):
        # random number generator
        x = randrange(0, d)
        y = randrange(0, d)
        if i % 100 == 0:
           # ratio of the points inside the circle and the total number of points and * 4
           ratio = counter / i  * 4
           # print the value on the screen
           print("Pie = {}".format(ratio))
        elif ((x - d / 2) ** 2) + ((y - d / 2) ** 2) <= (d ** 2) / 4:
            # if generated point is inside the circle
            win.plotPixelFast(x, y, "red")
            counter += 1
        else:
            win.plotPixelFast(x, y, "blue")

    # use the plotPixel() method to plot at least one pixel to actually show results
    win.plotPixel(100, 100, "green")

    win.getMouse()
    win.close()

main()