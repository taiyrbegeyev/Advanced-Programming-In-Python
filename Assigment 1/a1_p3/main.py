#JTSK-350112
# main.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de
import mod_conversion

start_length = int(input("Enter the start length: "))
end_length = int(input("Enter the end length: "))
step_size = int(input("Enter the step size: "))

# decision making
print("Enter s to print the result on the screen. \
Choose any other to generate conversion HTML table")
choice = input()

if choice == 's':
    # call function from imported module
    mod_conversion.in2cm_table(start_length, end_length, step_size)
else:
    # call function from imported module
    mod_conversion.in2cm_table_html(start_length, end_length, step_size)
    print("Open the html file :)")   