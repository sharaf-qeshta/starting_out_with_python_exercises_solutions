"""
8. Paint Job Estimator
A painting company has determined that for every 112 square feet of wall space, one gallon
of paint and eight hours of labor will be required. The company charges $35.00 per hour
for labor. Write a program that asks the user to enter the square feet of wall space to be
painted and the price of the paint per gallon. The program should display the following data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job


@author Sharaf Qeshta
"""

wall_space = int(input("enter the square feet of wall space:"))
price_per_gallon = float(input("enter the price of the paint per gallon:"))

gallons_needed = wall_space / 112.0
labor_hours_needed = gallons_needed * 8
print(f"The number of gallons of paint required is {format(gallons_needed, '.2f')} gallons")
print(f"The hours of labor required is {format(labor_hours_needed, '.2f')} hours")
print(f"The cost of the paint is ${format(gallons_needed * price_per_gallon, '.2f')}")
print(f"The labor charges is ${format(labor_hours_needed * 35, '.2f')}")
print(
    f"The total cost of the paint job is ${format(gallons_needed * price_per_gallon + labor_hours_needed * 35, '.2f')}")
