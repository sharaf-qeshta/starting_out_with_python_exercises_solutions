"""
11.Male and Female Percentages
Write a program that asks the user for the number of males and the number of females registered
 in a class. The program should display the percentage of males and females in the class.
Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the
class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage
of females can be calculated as 12 ÷ 20 = 0.6, or 60%.

@author Sharaf Qeshta
"""

males = int(input("enter the number of males:"))
females = int(input("enter the number of females:"))
total = males + females
print("Percentage of males :", males / total * 100, "%")
print("Percentage of females:", females / total * 100, "%")