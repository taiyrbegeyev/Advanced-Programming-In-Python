# JTSK-350112
# age.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

import datetime

def calculate_age(birthYear, birthMonth, birthDay):
    """Function for calculating the age based on the date of birth"""
    today_date = datetime.date.today()
    age = today_date.year - birthYear - ((today_date.month, today_date.day)
        < (birthMonth, birthDay))
    return age

def main():
    date_of_birth_text = input("Enter the date of birth: ")
    # split strings into lists with corresponding separators
    try:
        date_of_birth = date_of_birth_text.split(".")
        birthYear = int(date_of_birth[2])
        birthMonth = int(date_of_birth[1])
        birthDay = int(date_of_birth[0])
    except:
        date_of_birth = date_of_birth_text.split("-")
        birthYear = int(date_of_birth[0])
        birthMonth = int(date_of_birth[1])
        birthDay = int(date_of_birth[2])

    print("Age = {}".format(calculate_age(birthYear, birthMonth, birthDay)))    

main()