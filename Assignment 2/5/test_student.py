# JTSK-350112
# test_student.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

"""
    Test the setter and getter methods for age
"""

from student import Student

# create a new Student and set the scores for quizzes
myStudent = Student("John", 18, 3)
myStudent.setScore(1, 100)
myStudent.setScore(2, 95)
myStudent.setScore(3, 50)

print("Before: ")
print(myStudent)

# change the age
myStudent.setAge(19)
print("Change the age to {}".format(myStudent.getAge()))

print("After: ")
print(myStudent)