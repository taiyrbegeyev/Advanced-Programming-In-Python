# JTSK-350112
# robustness.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

def example1():
    # consider the case when denominator is 0
    for _ in range(3):
        x = int(input("enter a number: "))
        y = int(input("enter another number: "))
        print(x, '/', y, '=', x / y)

def example2(L):
    # When we reach the last element
    # from L, we can't get L[i + 1], due to the fact it doesn't
    # exist. So it leads to the IndexError
    print("\n\nExample 2")
    # sum = 0
    sumOfPairs = []
    for i in range(len(L) - 1):
        sumOfPairs.append(L[i] + L[i + 1])

    # here we got TypeError:  unsupported operand type(s) for +: 'int' and 'str',
    # which leads to TypeError. We need to covert int to str
    print("sumOfPairs = ", str(sumOfPairs))


def printUpperFile(fileName):
   file = open(fileName, "r")
   for line in file:
       print(line.upper())
   file.close()
    
def main():
    try: 
        example1()
        L = [10, 3, 5, 6, 9, 3]
        example2(L)
        # leads to TypeError
        # example2([10, 3, 5, 6, "NA", 3])
        example2([10, 3, 5, 6, 3])

        printUpperFile("doesNotExistYest.txt")
        printUpperFile("./Dessssktop/misspelled.txt")
    except ZeroDivisionError as exc:
        # consider the case when denominator is 0
        print("ZeroDivisionError: ", exc)
    except ValueError as exc:
        # Raised when an operation or function receives 
        # an argument that has the right type but an inappropriate value
        print("ValueError: ", exc)
    except IndexError as exc:
        # consider the case when a sequence subscript is out of range
        print("IndexError: ", exc)
    except TypeError as exc:
        # Passing arguments of the wrong type
        print("TypeError: ", exc)
    except FileNotFoundError as exc:
        # consider the case when the file is not found
        print("FileNotFoundError: ", exc)

main()