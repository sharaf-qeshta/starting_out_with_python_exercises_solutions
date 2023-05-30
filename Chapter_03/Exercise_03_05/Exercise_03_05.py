"""
5. Mass and Weight
Scientists measure an object’s mass in kilograms and its weight in newtons. If you know
the amount of mass of an object in kilograms, you can calculate its weight in newtons with
the following formula:
weight 5 mass 3 9.8
Write a program that asks the user to enter an object’s mass, then calculates its weight. If
the object weighs more than 500 newtons, display a message indicating that it is too heavy.
If the object weighs less than 100 newtons, display a message indicating that it is too light.


@author Sharaf Qeshta
"""

mass = float(input("enter the object`s mass: "))
weight_in_newton = mass * 9.8
if weight_in_newton > 500:
    print("it is too heavy")
if weight_in_newton < 100:
    print("it is too light")
