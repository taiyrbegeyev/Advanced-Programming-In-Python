# JTSK-350112
# calculator.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from graphics import *

def main():
    win = GraphWin("Calculator", 300, 250)

    # label fields
    number1 = Text(Point(50, 30), "number 1")
    number2 = Text(Point(50, 70), "number 2")
    operation = Text(Point(50, 110), "operation")
    result = Text(Point(50, 160), "Result")
    result_out = Text(Point(200, 160), "")

    # draw label fields
    number1.draw(win)
    number2.draw(win)
    operation.draw(win)
    result.draw(win)
    result_out.draw(win)

    # input fields
    number_1_input = Entry(Point(200, 30), 20)
    number_2_input = Entry(Point(200, 70), 20)
    operation_input = Entry(Point(200, 110), 20)

    # draw input fields
    number_1_input.draw(win)
    number_2_input.draw(win)
    operation_input.draw(win)

    # exit button
    buttonExit = Text(Point(220, 220), "Exit")
    buttonExitBorder = Rectangle(Point(170, 205), Point(270, 230))
    buttonExit.draw(win)
    buttonExitBorder.draw(win)

    # calculator
    while True:
        p = win.getMouse()
        # if exit button pressed
        if p.getX() >= 170 and p.getX() <= 270 and p.getY() >= 205 \
            and p.getY() <= 230:
            win.close()
        # convert input
        try:
            a = eval(number_1_input.getText())
            b = eval(number_2_input.getText())
            oper = operation_input.getText()
        except ValueError as exc:
            result_out.setText("ValueError: {}".format(exc))
        except TypeError as exc:
            result_out.setText("TypeError: {}".format(exc))

        try:
            if oper == "+":
                result_out.setText(str(a + b))
            elif oper == "-":
                result_out.setText(str(a - b))
            elif oper == "*":
                result_out.setText(str(a * b))
            elif oper == "/":
                result_out.setText(str(a / b))
            else:
                result_out.setText("Wrong operation")
        except ZeroDivisionError as exc:
            result_out.setText("ZeroDivisionError: {}".format(exc))
        except ValueError as exc:
            result_out.setText("ValueError: {}".format(exc))
        except TypeError as exc:
            result_out.setText("TypeError: {}".format(exc))

    win.close()
main()