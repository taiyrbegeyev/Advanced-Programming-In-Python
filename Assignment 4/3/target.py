# JTSK-350112
# target.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from graphics import *

def draw_archery(circles, win):
    """Draws several circles forming the target"""
    # yellow circle
    yellowCircle = Circle(Point(circles[0][0], circles[0][1]), circles[0][2])
    yellowCircle.setFill("yellow")
    yellowCircle.setOutline("yellow")

    # red circle
    redCircle = Circle(Point(circles[1][0], circles[1][1]), circles[1][2])
    redCircle.setFill("red")
    redCircle.setOutline("red")

    # blue circle
    blueCircle = Circle(Point(circles[2][0], circles[2][1]), circles[2][2])
    blueCircle.setFill("blue")
    blueCircle.setOutline("blue")

    # black circle
    blackCircle = Circle(Point(circles[3][0], circles[3][1]), circles[3][2])
    blackCircle.setFill("black")
    blackCircle.setOutline("black")

    # white circle
    whiteCircle = Circle(Point(circles[4][0], circles[4][1]), circles[4][2])
    whiteCircle.setFill("white")
    whiteCircle.setOutline("white")

    # draw circles
    whiteCircle.draw(win)
    blackCircle.draw(win)
    blueCircle.draw(win)
    redCircle.draw(win)
    yellowCircle.draw(win)

def main():
    win = GraphWin("Archery Target", 200, 200)

    draw_archery([(100, 100, 15), (100, 100, 30), (100, 100, 45),
        (100, 100, 60), (100, 100, 75)], win)

    win.getMouse()
    win.close()

main()