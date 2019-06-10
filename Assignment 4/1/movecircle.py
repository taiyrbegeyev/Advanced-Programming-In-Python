# JTSK-350112
# movecircle.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from graphics import *

def main():
	win = GraphWin()
	# shape = Circle(Point(50, 50), 20)
	# make to draw squares
	shape = Rectangle(Point(50, 50), 20)
	shape.setOutline("red")
	shape.setFill("red")
	shape.draw(win)
	for _ in range(10):
		# each successibe click should create 
		# an additional square
		shape.draw(win) 
	win.close()

main()