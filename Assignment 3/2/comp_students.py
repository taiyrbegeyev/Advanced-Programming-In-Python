# JTSK-350112
# comp_students.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from student import Student
import random

def sortByName(val):
    return val.getName()

# create new instances and place them in a list

s1 = Student("Elon", 1)
s2 = Student("Mark", 1)
s3 = Student("Bill", 1)
s4 = Student("Larry", 1)
s5 = Student("Sergey", 1)
s6 = Student("Taiyr", 1)
s7 = Student("Temirlan", 1)
s8 = Student("Qwerty", 1)
s9 = Student("Tom", 1)
s10 = Student("Tim", 1)

myList = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

# shuffle
random.shuffle(myList)
for x in myList:
    print(x.getName())

print()

# use sort in the descending order based on their names.
myList.sort(reverse = True)
for x in myList:
    print(x.getName())