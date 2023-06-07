"""
10. Money Counting Game
Create a change-counting game that gets the user to enter the number of coins required
to make exactly one dollar. The program should prompt the user to enter the number of
pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one
dollar, the program should congratulate the user for winning the game. Otherwise, the
program should display a message indicating whether the amount entered was more than
or less than one dollar.

@author Sharaf Qeshta
"""

pennies = int(input("enter the amount of pennies:"))  # 1 cent
nickels = int(input("enter the amount of nickels:"))  # 5 cents
dimes = int(input("enter the amount of dimes:"))  # 10 cents
quarters = int(input("enter the amount of quarters:"))  # 25 cents

total = pennies + nickels * 5 + dimes * 10 + quarters * 25

if total == 100:
    print("Congratulation you won the game")
elif total < 100:
    print("the amount entered is less than one dollar")
else:
    print("the amount entered is more than one dollar")

