"""
9. Monthly Sales Tax
A retail company must file a monthly sales tax report listing the total sales for the month,
and the amount of state and county sales tax collected. The state sales tax rate is 5 percent
and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter
the total sales for the month. From this figure, the application should calculate and display
the following:
• The amount of county sales tax
• The amount of state sales tax
• The total sales tax (county plus state)


@author Sharaf Qeshta
"""

total_sales = float(input("enter the total sales for the month"))

state_sales_tax = total_sales * 0.05
total_sales -= state_sales_tax
county_sales_tax = total_sales * 0.025
total_sales -= county_sales_tax

print(f"The amount of county sales tax is ${county_sales_tax}")
print(f"The amount of state sales tax is ${state_sales_tax}")
print(f"The total sales tax is ${county_sales_tax + state_sales_tax}")