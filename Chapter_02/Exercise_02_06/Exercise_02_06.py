"""
6. Payment Instalments
Write a program that asks the user to enter the amount of a purchase and the desired
number of payment instalments. The program should add 5 percent to the amount to get
the total purchase amount, and then divide it by the desired number of instalments, then
display messages telling the user the total amount of the purchase and how much each
instalment will cost.

@author Sharaf Qeshta
"""

amount_of_purchase = float(input("enter the amount of the purchase: "))
number_of_instalments = float(input("enter the number of instalments: "))
total_amount_of_purchase = amount_of_purchase + amount_of_purchase * 0.05
print("total:", total_amount_of_purchase)
print("instalment amount:", format(total_amount_of_purchase / number_of_instalments, "0.2f"))
