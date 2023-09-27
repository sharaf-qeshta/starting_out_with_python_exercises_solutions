"""
14. Expense Pie Chart
Create a text file that contains your expenses for last month in the following categories:
•	 Rent
•	 Gas
•	 Food
•	 Clothing
•	 Car payment
•	 Misc
Write a Python program that reads the data from the file and uses matplotlib to plot a pie
chart showing how you spend your money.


@author Sharaf Qeshta
"""

import matplotlib.pyplot as plt


def main():
    try:
        file = open("expenses.txt")
        expenses = []
        for line in file:
            expenses.append(int(line))
        labels = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Misc"]
        plt.pie(expenses, labels=labels)
        plt.title("Expense Pie Chart")
        plt.show()
    except Exception as error:
        print(error)


main()
