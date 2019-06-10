# JTSK-350112
# raise_exc.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

# three different exception classes derived from Exception
class OwnException1(Exception): pass
class OwnException2(Exception): pass
class OwnException3(Exception): pass

def something(choice):
    """
        Throw exceptions depending on the value of choice
    """
    if choice == 1:
        raise OwnException1(999)
    elif choice == 2:
        raise OwnException2("Error has happened")
    elif choice == 3:
        raise OwnException3(1.23)

def main():
    # call the function 5 times
    try:
        something(4)
        something(5)
        something(1)
        something(2)
        something(3)
    except OwnException1 as exc:
        print(exc)
    except OwnException2 as exc:
        print(exc)
    except OwnException3 as exc:
        print(exc)
    else:
        print("No exception occured")
    finally:
        print("Execution is finished")

main()