"""
14. Body Mass Index
Write a program that calculates and displays a person’s body mass index (BMI). The BMI
is often used to determine whether a person is overweight or underweight for his or her
height. A person’s BMI is calculated with the following formula:
BMI 5 weight 3 703/height2
where weight is measured in pounds and height is measured in inches. The program should
ask the user to enter his or her weight and height, then display the user’s BMI.
The program should also display a message indicating whether the person has optimal weight, is
underweight, or is overweight. A person’s weight is considered to be optimal if his or her
BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered to be
underweight. If the BMI value is greater than 25, the person is considered to be overweight.

@author Sharaf Qeshta
"""

weight = float(input("enter your weight in pounds:"))
height = float(input("enter your height in inches:"))

BMI = weight * (703 /(height * height))

if BMI < 18.5:
    print("you are underweight")
elif BMI <= 25:
    print("you have an optimal weight")
else:
    print("you are overweight")