"""
1. Bug Collector
A bug collector collects bugs every day for five days. Write a program that keeps a running
total of the number of bugs collected during the five days. The loop should ask for the
number of bugs collected for each day, and when the loop is finished, the program should
display the total number of bugs collected.

@author Sharaf Qeshta
"""

total_bugs_collected = 0

for i in range(5):
    total_bugs_collected += int(input("enter the number of bugs collected today:"))

print("the total bugs collected in five days is", total_bugs_collected)