# JTSK-350112
# test_student.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

"""
    Test the setter method setName
"""

from student import Student

# create a new Student and set the scores for quizzes
myStudent = Student("John", 3)
myStudent.setScore(1, 100)
myStudent.setScore(2, 95)
myStudent.setScore(3, 50)

print("Before: ")
print(myStudent)

# change his name
myStudent.setName("Jack")

print("After: ")
print(myStudent)