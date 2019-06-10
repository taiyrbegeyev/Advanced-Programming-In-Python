# JTSK-350112
# unpicling.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

import sys
import pickle

# open file
try:
    file = open("object.txt", "rb")
except:
    sys.exit("Couldn't open the file")

# unpickle and print
s = pickle.load(file)
print(s)
# close the file
file.close()

# reopen the same file, read line by line 
try:
    file = open("object.txt", "rb")
except:
    sys.exit("Couldn't open the file")

line = file.readline()
sum = 0
while line:
    # print the line and its size
    print("{} {}".format(line, sys.getsizeof(line)))
    sum += sys.getsizeof(line)
    # move to the next line
    line = file.readline()

# print the sum
print("Sum = {}".format(sum))

#close the file
file.close()