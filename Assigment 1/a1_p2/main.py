#JTSK-350112
# main.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de
import mod_conversion

start_length = int(input("Enter the start length: "))
end_length = int(input("Enter the end length: "))
step_size = int(input("Enter the step size: "))
# call function from imported module
mod_conversion.in2cm_table(start_length, end_length, step_size)