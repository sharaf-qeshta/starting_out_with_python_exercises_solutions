"""
4. Automobile Costs
Write a program that asks the user to enter the monthly costs for the following expenses
incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
maintenance. The program should then display the total monthly cost of these expenses,
and the total annual cost of these expenses.

@author Sharaf Qeshta
"""

monthly_loan_payment = float(input("enter your monthly loan payment:"))
monthly_insurance = float(input("enter your monthly insurance:"))
monthly_gas = float(input("enter your monthly gas:"))
monthly_oil = float(input("enter your monthly oil:"))
monthly_tires = float(input("enter your monthly tires:"))
monthly_maintenance = float(input("enter your monthly maintenance:"))

total_monthly = monthly_loan_payment + monthly_insurance + monthly_gas + monthly_oil + monthly_tires + monthly_maintenance
total_annual = total_monthly * 12

print(f"your total payment in a month is ${total_monthly}")
print(f"your total payment in a year is ${total_annual}")
