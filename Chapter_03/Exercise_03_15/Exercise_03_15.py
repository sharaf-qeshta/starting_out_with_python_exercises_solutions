"""
15. Time Calculator
Write a program that asks the user to enter a number of seconds and works as follows:
•	 There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should convert the number of seconds to minutes and
seconds.
•	 There are 3,600 seconds in an hour. If the number of seconds entered by the user is
greater than or equal to 3,600, the program should convert the number of seconds to
hours, minutes, and seconds.
•	 There are 86,400 seconds in a day. If the number of seconds entered by the user is
greater than or equal to 86,400, the program should convert the number of seconds to
days, hours, minutes, and seconds.


@author Sharaf Qeshta
"""
seconds = int(input("enter seconds:"))

days = int(seconds / 86400)
seconds = seconds % 86400
hours = int(seconds / 3600)
seconds = seconds % 3600
minutes = int(seconds / 60)
seconds = seconds % 60

print(days, "days,", hours, "hours,", minutes, "minutes,", seconds, "seconds")