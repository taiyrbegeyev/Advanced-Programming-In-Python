# JTSK-350112
# colorpixels.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from graphics import *

def main():
    win = GraphWin("Coloring pixels", 255, 255)
    counter = 0

    for i in range(0, 255):
        for j in range(0, 255):
            # every 150th pixel use plotPixel()
            if counter % 149 == 0:
                win.plotPixel(i, j, color_rgb(i, j, 8))
            else:
                win.plotPixelFast(i, j, color_rgb(i, j, 8))
            counter += 1
    win.close()
    
main()