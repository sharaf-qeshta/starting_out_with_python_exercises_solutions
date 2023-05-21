"""
4. Total Purchase
A customer in a store is purchasing five items. Write a program that asks for the price of
each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 7 percent.

@author Sharaf Qeshta
"""
item1_price = float(input("enter item 1 price: "))
item2_price = float(input("enter item 2 price: "))
item3_price = float(input("enter item 3 price: "))
item4_price = float(input("enter item 4 price: "))
item5_price = float(input("enter item 5 price: "))

subtotal = item1_price + item2_price + item3_price + item4_price + item5_price
sales_tax = subtotal * 0.07
print("subtotal:", format(subtotal, '.2f'))
print("sales tax:", format(sales_tax, '0.2f'))
print("total:", format(sales_tax + subtotal, '.2f'))
