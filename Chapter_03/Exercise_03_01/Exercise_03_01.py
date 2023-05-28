"""
1. Number Analyser
Write a program that asks the user to enter an integer. The program should display
“Positive” if the number is greater than 0, “Negative” if the number is less than 0, and
“Zero” if the number is equal to 0. The program should then display “Even” if the number
is even, and “Odd” if the number is odd.

@author Sharaf Qeshta
"""

integer = int(input("enter a number: "))
if integer < 0:
    print("Negative")
elif integer > 0:
    print("Positive")
else:
    print("Zero")

if integer % 2 == 0:
    print("Even")
else:
    print("Odd")