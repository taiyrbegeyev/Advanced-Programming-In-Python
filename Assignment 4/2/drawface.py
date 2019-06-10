# JTSK-350112
# drawface.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from graphics import *

def main():
    """Draw a human face"""

    win = GraphWin("I am human", 400, 400)

    # create head 
    face = Circle(Point(200, 150), 100)
    face.setFill(color_rgb(158, 104, 4))

    # create eye 1
    eye_1 = Circle (Point(160, 130), 20)

    # create eye 2
    eye_2 = eye_1.clone()
    eye_2.move(80, 0)

    eye_1.setFill("red")
    eye_2.setFill("red")

    # create nose
    nose = Polygon(Point(200, 160), Point(180, 190), Point(220, 190))
    nose.setFill(color_rgb(158, 4, 4))

    # create mouth
    mouth_1 = Polygon(Point(185, 215), Point(200, 240), Point(215, 215)) 
    mouth_2 = Circle(Point(200, 215), 15)
    mouth_1.setFill("red")
    mouth_2.setFill("yellow")

    # create ears
    ear_1 = Oval(Point(115, 100), Point(125, 150))
    ear_1.setFill(color_rgb(158, 4, 4))

    ear_2 = ear_1.clone()
    ear_2.move(160, 0)

    # draw eveything
    face.draw(win)
    eye_1.draw(win)
    eye_2.draw(win)
    nose.draw(win)
    mouth_1.draw(win)
    mouth_2.draw(win)
    ear_1.draw(win)
    ear_2.draw(win)

    win.getMouse()
    win.close()
main()