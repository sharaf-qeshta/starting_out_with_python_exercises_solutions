"""
2. Calories Burned
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

@author Sharaf Keshta
"""

for i in range(10, 31):
    if i % 5 == 0:
        print("after", i, "minutes you burned ", format(i * 4.2, ".2f"), "calories")
