"""
3. Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a
list. The program should calculate and display the total rainfall for the year, the average
monthly rainfall, the months with the highest and lowest amounts.


@author Sharaf Qeshta
"""


def main():
    rainfall_data = []
    for i in range(12):
        rainfall_data.append(int(input(f"enter the amount of rain in {i + 1}: ")))

    total = 0
    highest = rainfall_data[0]
    highest_number = 0
    lowest = rainfall_data[0]
    lowest_number = 0

    for i in range(12):
        total += rainfall_data[i]
        if rainfall_data[i] > highest:
            highest_number = i
            highest = rainfall_data[i]
        if rainfall_data[i] < lowest:
            lowest = rainfall_data[i]
            lowest_number = i

    print(f"the total amount of rainfall this year is {total}")
    print(f"the average amount of rainfall this year is {total / 12}")
    print(f"the month with the highest rainfall is {highest_number + 1} which is {highest}")
    print(f"the month with the lowest rainfall is {lowest_number + 1} which is {lowest}")


main()
