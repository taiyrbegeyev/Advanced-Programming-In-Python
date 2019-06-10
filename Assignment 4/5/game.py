# JTSK-350112
# game.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from craps import *
from graphics import *

def main():
    win = GraphWin("Craps", 300, 300)
    # Text fields
    dice_1 = Text(Point(80, 50), "Dice #1")
    dice_1_out = Text(Point(210, 60), "")
    dice_1_out_border = Rectangle(Point(180, 30), Point(240, 90))

    dice_2 = Text(Point(80, 130), "Dice #2")
    dice_2_out = Text(Point(210, 140), "")
    dice_2_out_border = Rectangle(Point(180, 110), Point(240, 170))

    sumOfDices = Text(Point(80, 210), "Sum")
    sumOfDices_out = Text(Point(200, 210), "")
    result = Text(Point(80, 230), "Results")
    result_out = Text(Point(200, 230), "")

    # draw text fields
    dice_1.draw(win)
    dice_1_out.draw(win)
    dice_1_out_border.draw(win)

    dice_2.draw(win)
    dice_2_out.draw(win)
    dice_2_out_border.draw(win)

    sumOfDices.draw(win)
    sumOfDices_out.draw(win)
    result.draw(win)
    result_out.draw(win)

    # create play again and exit buttons
    buttonPlayAgain = Text(Point(80, 270), "Play Again")
    buttonPlayAgainBorder = Rectangle(Point(30, 255), Point(130, 280))
    buttonPlayAgain.draw(win)
    buttonPlayAgainBorder.draw(win)

    buttonExit = Text(Point(220, 270), "Exit")
    buttonExitBorder = Rectangle(Point(170, 255), Point(270, 280))
    buttonExit.draw(win)
    buttonExitBorder.draw(win)

    # call the function from craps and get the results of the game
    while True:
        # unless exit pressed or the end of game, keep playing
        (rolls, isWin) = playOneGame()
        for x in rolls:
            # as long as there are dices
            dice_1_out.setText(str(x[0]))
            dice_2_out.setText(str(x[1]))
            sumOfDices_out.setText(str(x[0] + x[1]))
            p = win.getMouse()
            # if the Exit button is pressed
            if p.getX() >= 170 and p.getX() <= 270 \
                and p.getY() >= 255 and p.getY() <= 280:
                win.close()

        # print result, either "Won" or "Lost"
        result_out.setText(isWin)
        # wait for click
        p = win.getMouse()
        # if Play Again button is pressed
        if p.getX() >= 30 and p.getX() <= 130 \
            and p.getY() >= 255 and p.getY() <= 280:
            # clear outputs
            dice_1_out.setText("")
            dice_2_out.setText("")
            sumOfDices_out.setText("")
            result_out.setText("")
        else:
            win.close()

main()