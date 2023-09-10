"""
9. Population Data
If you have downloaded the source code you will find a file named USPopulation.txt
in the Chapter 07 folder. The file contains the midyear population of the United States, in
thousands, during the years 1950 through 1990. The first line in the file contains the
population for 1950, the second line contains the population for 1951, and so forth.
Write a program that reads the file’s contents into a list. The program should display the
following data:
•	 The average annual change in population during the time period
•	 The year with the greatest increase in population during the time period
•	 The year with the smallest increase in population during the time period


@author Sharaf Qeshta
"""


def main():
    data = []
    try:
        file = open("USPopulation.txt")
        for line in file:
            data.append(int(line.strip()))
    except Exception as error:
        print(error)

    total_annual_change = 0
    the_greatest_change = data[1] - data[0]
    the_greatest_change_year = 1951
    the_smallest_change = data[1] - data[0]
    the_smallest_change_year = 1951

    for i in range(len(data) - 1):
        annual_change = data[i + 1] - data[i]
        total_annual_change += annual_change

        if annual_change > the_greatest_change:
            the_greatest_change = annual_change
            the_greatest_change_year = i + 1 + 1950
        if annual_change < the_smallest_change:
            the_smallest_change = annual_change
            the_smallest_change_year = i + 1 + 1950

    print("The average annual change in population during the time period is",
          total_annual_change / 40)
    print("The year with the greatest increase in population during the time period is",
          the_greatest_change_year)
    print("The year with the smallest increase in population during the time period is",
          the_smallest_change_year)


main()
