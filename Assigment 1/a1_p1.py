#JTSK-350112
# problem 1.1.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

start_length = int(input("Enter the start length: "))
end_length = int(input("Enter the end length: "))
step_size = int(input("Enter the step size: "))

print("{0:>8} {1:>8}".format("inch", "cm"))
for i in range(start_length, end_length, step_size):
    print("{0:>8.1f} {1:>8.1f}".format(i, i * 2.54))