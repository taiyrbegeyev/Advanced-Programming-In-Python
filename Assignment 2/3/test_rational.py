# JTSK-350112
# test_rational.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

"""
    a test program called that uses the class and 
    its methods to compute 1/2 + 1/8. 
    Print the result on the screen.
"""

from rational import Rational

# create two instances
r1 = Rational(1, 2)
r2 = Rational(1, 8)
# find the sum and print it
print(r1 + r2)
