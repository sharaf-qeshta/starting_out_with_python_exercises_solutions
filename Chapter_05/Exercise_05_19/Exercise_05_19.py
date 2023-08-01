"""
19. Loan Payments Calculator
Suppose you have taken out a loan for a certain amount of money with a fixed monthly interest
rate and monthly payments, and you want to determine the monthly payment amount
necessary to pay off the loan within a specific number of months. The formula is as follows:
P 5 R * A
1 2 (1 1 R)
2M
The terms in the formula are:
•	 P is the payment amount per month.
•	 R is the monthly interest rate, as a decimal (e.g. 2.5% 5 0.025).
•	 A is the amount of the loan.
•	 M is the number of months.
Write a program that prompts the user to enter the loan amount, monthly interest rate as
a percentage and desired number of months. The program should pass these values to a
function that returns the monthly payment amount necessary. The program should display
this amount.


@author Sharaf Qeshta
"""


def get_monthly_payment(interest_rate, amount, months):
    return (interest_rate * amount) / (1 - (1 / (1 + interest_rate) ** months))

loan_amount = float(input("enter the loan amount: "))
monthly_interest_rate = float(input("enter the monthly interest rate: "))
months_desired = float(input("enter the desired months: "))

print(f"you monthly payment will be ${format(get_monthly_payment(monthly_interest_rate, loan_amount, months_desired), '.2f')}")