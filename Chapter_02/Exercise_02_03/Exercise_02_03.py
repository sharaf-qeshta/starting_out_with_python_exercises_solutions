"""
3. Pounds to Kilograms
One pound is equivalent to 0.454 kilograms. Write a program that asks the user to enter
the mass of an object in pounds and then calculates and displays the mass of the object in
kilograms.

@author Sharaf Qeshta
"""

object_weight_pounds = float(input("enter object mass weight in pounds: "))
print("object weight in kilograms: ", format(object_weight_pounds * 0.454, '.2f'))
