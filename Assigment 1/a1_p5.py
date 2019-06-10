#JTSK-350112
# a1_p5.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

"""
    A program which implements the basic behaviour of a Stack 
"""

def push(list, el):
    """
        Pushes the el to the top of the Stack list
    """
    list.append(el)
    print("Pushing {}".format(el))

def pop(list):
    """
        pops a number from the top of the stack and prints it on the screen
    """
    if list == []:
        print("Stack underflow")
    else:
        delel = list.pop()
        print("Popping element {}".format(delel))
        return delel

def empty(list):
    """
        empties the stack by popping one element after the other
    """
    print("Emptying stack")
    while list != []:
        pop(list)

# main program
myList = []
while True:
    cmd = input("")
    if cmd == 'q':
        print("Good Bye!")
        break
    elif cmd == 's':
        num = int(input())
        push(myList, num)
    elif cmd == 'p':
        pop(myList)        
    elif cmd == 'e':
        empty(myList)
    else:
        print("Wrong command")