# JTSK-350112
# eclipse.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

import datetime

eclipse_date = datetime.date(2017, 8, 21)
today_date = datetime.date.today()

print("{} days have passed since last eclipse"
    .format(abs(today_date - eclipse_date).days))