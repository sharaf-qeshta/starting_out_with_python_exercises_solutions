"""
15. 1994 Weekly Gas Graph
In the student sample programs for this book, you will find a text file named 1994_Weekly_
Gas_Averages.txt. The file contains the average gas price for each week in the year 1994.
(There are 52 lines in the file.) Using matplotlib, write a Python program that reads the
contents of the file then plots the data as either a line graph or a bar chart. Be sure to display
meaningful labels along the X and Y axes, as well as the tick marks.


@author Sharaf Qeshta
"""

import matplotlib.pyplot as plt


def main():
    data = []
    try:
        file = open("1994_Weekly_Gas_Average.txt")
        for line in file:
            data.append(int(line))
    except Exception as error:
        print(error)

    x_coordinates = data
    y_coordinates = []
    for i in range(len(data)):
        y_coordinates.append(i + 1)
    plt.plot(x_coordinates, y_coordinates)
    plt.title("1994 Weekly Gas Graph")
    plt.xlabel("Gas Prices")
    plt.ylabel("Weeks")
    plt.grid(True)
    plt.show()


main()
