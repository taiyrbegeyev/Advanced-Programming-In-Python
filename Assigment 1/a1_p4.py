#JTSK-350112
# problem 1.4.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

"""
    Make your terminal's window full screen
"""

def border():
    for _ in range(0, 90):
        print('-', end = '')
    print()

# store data at the list of tuples
data = [
    ("T-101", "Tesla Model S", 10000, 68750, "Fremont, California"), 
    ("T-102", "Tesla Model 3", 5000, 31450, "Fremont, California"), 
    ("T-103", "Tesla Model X", 3000, 85300, "Fremont, California"), 
    ("T-104", "Tesla Model Y", 2000, 56000, "Fremont, California"), 
    ("T-105", "Tesla Model Roadster", 1, 200000, "Fremont, California") 
]

# widths for columns:
# 6 for ID
# 30 for name
# 8 for quantity
# 10 for price
# 30 for location

border()
print("|{:<6}|{:<30}|{:>8}|{:>10}|{:>30}|"\
    .format("ID", "Name", "Quantity", "Price", "Location"))
border()

for i in data:
    print("|{:0<6}|{:<30}|{:>8}|{:>10,.2f}|{:>30}|"\
        .format(i[0], i[1], i[2], i[3], i[4]))

border()