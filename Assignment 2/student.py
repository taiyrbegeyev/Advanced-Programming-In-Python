#JTSK-350112
# student.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
   """Represents a student."""

   def __init__(self, name, number):
      """All scores are initially 0."""
      # print Constructor being called every time it is called 
      print("Constructor being called")
      self._name = name
      self._scores = []
      for count in range(number):
         self._scores.append(0)

   def getName(self):
      """Returns the student's name."""
      return self._name
  
   def setScore(self, i, score):
      """Resets the ith score, counting from 1."""
      self._scores[i - 1] = score

   def getScore(self, i):
      """Returns the ith score, counting from 1."""
      return self._scores[i - 1]
   
   def getAverage(self):
      """Returns the average score."""
      return sum(self._scores) / len(self._scores)
    
   def getHighScore(self):
      """Returns the highest score."""
      return max(self._scores)
 
   def __str__(self):
      """Returns the string representation of the student."""
      return "Name: " + self._name  + "\nScores: " + \
             " ".join(map(str, self._scores))

# main program
# test the class

# create three students
student1 = Student("Jenny", 2)
student2 = Student("Steve", 2)
student3 = Student("Celine", 2)

# insert the grades for first 2 quizzes(95 and 90)
student1.setScore(1, 95)
student2.setScore(1, 95)
student3.setScore(1, 95)

student1.setScore(2, 90)
student2.setScore(2, 90)
student3.setScore(2, 90)

# print
print(student1)
print(student2)
print(student3)