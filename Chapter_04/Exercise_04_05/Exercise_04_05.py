"""
5. Average Rainfall
Write a program that uses nested loops to collect data and calculate the average rainfall over
a period of years. The program should first ask for the number of years. The outer loop will
iterate once for each year. The inner loop will iterate twelve times, once for each month.
Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
After all iterations, the program should display the number of months, the total inches of
rainfall, and the average rainfall per month for the entire period.

@author Sharaf Keshta
"""

years = int(input("enter the number of years:"))

total_rain = 0
for i in range(years):
    for j in range(12):
        rain_in_inches = int(input(f"enter the amount of rain in inches for month {j+1} in year {i+1}:"))
        total_rain += rain_in_inches

print("the number of months is", years * 12, " months")
print("total rainfall in inches in this period is", total_rain, " inches")
print("the average rainfall for this period is ", format(total_rain/(years * 12), ".2f"), " inches per month")