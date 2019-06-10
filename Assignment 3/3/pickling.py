# JTSK-350112
# pickling.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

import sys
import pickle
from student import *

# create a student object with some properties
s1 = Student("Elon", 2)
s1.setScore(1, 100)
s1.setScore(2, 100)

# print the object and the size of it in bytes
print(s1)
print("Size = {}".format(sys.getsizeof(s1)))

# open file
try:
    file = open("object.txt", "wb")
except:
    sys.exit("Couldn't open the file")

# pickle the object
pickle.dump(s1, file)
# close the file
file.close()