"""
7. Pennies for Pay
Write a program that calculates the amount of money a person would earn over a period of
time if his or her salary is one penny the first day, two pennies the second day, and continues
 to double each day. The program should ask the user for the number of days. Display
a table showing what the salary was for each day, then show the total pay at the end of the
period. The output should be displayed in a dollar amount, not the number of pennies.


@author Sharaf Qeshta
"""

days = int(input("enter the number of days:"))

total_salary = 0
current_salary = 1

print("days\t\tsalary")
for i in range(days):
    print(f"{i+1}\t\t\t${current_salary/100}")
    total_salary += current_salary
    current_salary *= 2

print(f"total salary after {days} days is ${total_salary/100}")