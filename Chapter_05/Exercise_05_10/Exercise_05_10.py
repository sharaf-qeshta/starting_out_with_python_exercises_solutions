"""
10. Feet to Inches
One foot equals 12 inches. Write a function named feet_to_inches that accepts a number
of feet as an argument and returns the number of inches in that many feet. Use the function
in a program that prompts the user to enter a number of feet then displays the number of
inches in that many feet.

@author Sharaf Qeshta
"""


def feet_to_inches(feet):
    return feet * 12


number_of_feet = int(input("enter the a number of feet:"))
print(f"{number_of_feet} feet is equal to {feet_to_inches(number_of_feet)} inches")
