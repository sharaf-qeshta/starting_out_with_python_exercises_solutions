"""
11. Sleep Debt
A “sleep debt” represents the difference between a person’s desirable and actual amount
of sleep. Write a program that prompts the user to enter how many hours they slept each
day over a period of seven days. Using 8 hours per day as the desirable amount of sleep,
determine their sleep debt by calculating the total hours of sleep they got over the seven-day
period and subtracting that from the total hours of sleep they should have got. If the user
does not have a sleep debt, display a message expressing your jealousy.

@author Sharaf Qeshta
"""

total_hours = 0
for i in range(7):
    total_hours += int(input(f"how many hours you sleep on day {i+1}:"))

desirable_hours = 8 * 7


if total_hours >= desirable_hours:
    # no sleep debt
    print("that`s good man")
else:
    print("you should sleep enough")