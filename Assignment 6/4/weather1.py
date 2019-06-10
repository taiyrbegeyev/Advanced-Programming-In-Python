# JTSK-350112
# weather1.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

import sys
import urllib.request

month = int(input("Enter a month number as integer: "))
if month < 10:
    url = "https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp20080{}.csv"\
        .format(month)
else:
    url = "https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp2008{}.csv"\
        .format(month)

# fetch data
try:
    u = urllib.request.urlretrieve(url, "wdata1.csv")
except:
    print("Error fetching URL: ", url)
    sys.exit(1)