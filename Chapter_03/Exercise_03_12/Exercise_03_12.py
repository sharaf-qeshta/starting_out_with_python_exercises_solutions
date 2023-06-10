"""
12. Software Sales
A software company sells a package that retails for $99. Quantity discounts are given
according to the following table:
Quantity Discount
10–19 10%
20–49 20%
50–99 30%
100 or more 40%
Write a program that asks the user to enter the number of packages purchased.
 The program should then display the amount of the discount (if any) and the total amount of the
purchase after the discount.

@author Sharaf Qeshta
"""

PACKAGE_PRICE = 99
packages_purchased = int(input("enter the number of packages purchased: "))

discount = 0

if packages_purchased < 10:
    discount = 0
elif packages_purchased < 20:
    discount = 0.1
elif packages_purchased < 50:
    discount = 0.2
elif packages_purchased < 100:
    discount = 0.3
else:
    discount = 0.4

total = PACKAGE_PRICE * packages_purchased
print("discount:", total * discount, "$")
print("total after discount:", total - (total * discount), "$")
