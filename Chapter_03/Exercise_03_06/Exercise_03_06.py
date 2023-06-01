"""
6. Magic Dates
The date June 10, 1960, is special because when it is written in the following format, the
month times the day equals the year:
6/10/60
Design a program that asks the user to enter a month (in numeric form), a day, and a two digit
year. The program should then determine whether the month times the day equals the
year. If so, it should display a message saying the date is magic. Otherwise, it should display
a message saying the date is not magic.


@author Sharaf Qeshta
"""

day = int(input("enter a day:"))
month = int(input("enter a month"))
year = int(input("enter a two digit year:"))
if day * month == year:
    print("the date is magic")
else:
    print("the date is not magic")