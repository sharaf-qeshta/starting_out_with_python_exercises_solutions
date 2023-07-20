"""
7. Stadium Seating
There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost
$15, and Class C seats cost $10. Write a program that asks how many tickets for each class
of seats were sold, then displays the amount of income generated from ticket sales.

@author Sharaf Qeshta
"""

class_a = int(input("enter class A tickets count:"))
class_b = int(input("enter class B tickets count:"))
class_c = int(input("enter class C tickets count:"))

revenue = class_a * 20 + class_b * 15 + class_c * 10
print(f"the income from the tickets sold is ${revenue}")