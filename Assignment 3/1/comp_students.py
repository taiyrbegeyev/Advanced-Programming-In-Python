# JTSK-350112
# comp_students.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

from student import Student
# create two instances
s1 = Student("Elon", 2)
s2 = Student("Mark", 2)
s1.setScore(1, 100)
s1.setScore(2, 95)
s2.setScore(1, 100)
s2.setScore(2, 95)

print("Equal = {}".format(s1 == s2))
print("Not Equal = {}".format(s1 != s2))
print("< {}".format(s1 < s2))
print("<= {}".format(s1 <= s2))
print("> {}".format(s1 > s2))
print(">= {}".format(s1 >= s2))