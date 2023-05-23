"""
8. Tip, Tax, and Total
Write a program that calculates the total amount of a meal purchased at a restaurant. The
program should ask the user to enter the charge for the food, then calculate the amounts
of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

@author Sharaf Qeshta
"""

price = float(input("enter the charge for the food:"))
tip = price * 0.18
tax = price * 0.07
print("Price =>", price)
print("Tip =>", tip)
print("Tax =>", tax)
print("Total =>", tax + price + tip)