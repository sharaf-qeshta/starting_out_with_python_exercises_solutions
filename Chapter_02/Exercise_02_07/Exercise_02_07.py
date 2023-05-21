"""
7. Miles-per-Gallon
A car's miles-per-gallon (MPG) can be calculated with the following formula:
MPG 5 Miles driven 4 Gallons of gas used
Write a program that asks the user for the number of miles driven and the gallons of gas
used. It should calculate the car's MPG and display the result.

@author Sharaf Qeshta
"""

miles_driven = float(input("enter the miles driven: "))
amount_of_gas_used = float(input("enter amount of gas used 'in gallons': "))
print("the car MPG will be: ", miles_driven/amount_of_gas_used)