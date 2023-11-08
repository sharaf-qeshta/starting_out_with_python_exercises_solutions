"""
14. Gas Prices
In the student sample program files for this chapter, you will find a text file named
GasPrices.txt. The file contains the weekly average prices for a gallon of gas in the
United States, beginning on April 5th, 1993, and ending on August 26th, 2013. Figure 8-7
shows an example of the first few lines of the file’s contents:
Each line in the file contains the average price for a gallon of gas on a specific date. Each line
is formatted in the following way:
 MM-DD-YYYY:Price
MM is the two-digit month, DD is the two-digit day, and YYYY is the four-digit year. Price is
the average price per gallon of gas on the specified date.
For this assignment, you are to write one or more programs that read the contents of the file
and perform the following calculations:
Average Price Per Year: Calculate the average price of gas per year, for each year in the file.
(The file’s data starts in April of 1993, and it ends in August 2013. Use the data that is present
for the years 1993 and 2013.)
Average Price Per Month: Calculate the average price for each month in the file.
Highest and Lowest Prices Per Year: For each year in the file, determine the date and amount
for the lowest price, and the highest price.
List of Prices, Lowest to Highest: Generate a text file that lists the dates and prices, sorted
from the lowest price to the highest.
List of Prices, Highest to lowest: Generate a text file that lists the dates and prices, sorted
from the highest price to the lowest.
You can write one program to perform all of these calculations, or you can write different
programs, one for each calculation.


@author Sharaf Qeshta
"""

DATA = []


def load_data():
    try:
        file = open("GasPrices.txt")
        for line in file:
            data = line.split(":")
            price = float(data[1])
            date_data = data[0].split("-")
            year = int(date_data[2])
            month = int(date_data[0])
            day = int(date_data[1])
            current_week = [day, month, year, price]
            DATA.append(current_week)
    except Exception as error:
        print(error)


def print_average_price_per_year():
    current_year = 1993
    total = 0
    number_of_weeks = 0
    for week in DATA:
        if current_year != week[2]:
            print(f"the average gas prices in {current_year} is {total / number_of_weeks}")
            current_year = week[2]
            total = week[3]
            number_of_weeks = 1
        else:
            total += week[3]
            number_of_weeks += 1
    print(f"the average gas prices in {current_year} is {total / number_of_weeks}")


def print_average_price_per_month():
    current_month = 4 # April
    total = 0
    number_of_weeks = 0
    for week in DATA:
        if current_month != week[1]:
            print(f"the average gas prices in {current_month} is {total / number_of_weeks}")
            current_month = week[1]
            total = week[3]
            number_of_weeks = 1
        else:
            total += week[3]
            number_of_weeks += 1
    print(f"the average gas prices in {current_month} is {total / number_of_weeks}")


def print_highest_and_lowest_price_per_year():
    current_year = 1993
    current_max_price = DATA[0][3]
    current_min_price = DATA[0][3]
    for week in DATA:
        if current_year == week[2]:
            if week[3] > current_max_price:
                current_max_price = week[3]
            if week[3] < current_min_price:
                current_min_price = week[3]
        else:
            print(
                f"The maximum price in {current_year} is ${current_max_price} and the lowest price is ${current_min_price}")
            current_year = week[2]
            current_max_price = week[3]
            current_min_price = week[3]


def sort_data_asc():
    sorted = False
    while (not sorted):
        sorted = True
        for i in range(len(DATA) - 1):
            if DATA[i][3] > DATA[i + 1][3]:
                sorted = False
                temp_row = DATA[i]
                DATA[i] = DATA[i + 1]
                DATA[i + 1] = temp_row

    print(DATA)


def from_highest_to_lowest():
    try:
        file = open("highest_to_lowest.txt", "a")
        for i in reversed(range(len(DATA))):
            file.write(f"{DATA[i][1]}-{DATA[i][0]}-{DATA[i][2]}:{DATA[i][3]}\n")
        file.close()
    except Exception as error:
        print(error)


def from_lowest_to_highest():
    try:
        file = open("lowest_to_highest.txt", "a")
        for i in range(len(DATA)):
            file.write(f"{DATA[i][1]}-{DATA[i][0]}-{DATA[i][2]}:{DATA[i][3]}\n")
        file.close()
    except Exception as error:
        print(error)


# call the functions in this order
load_data()
print_average_price_per_year()
print_average_price_per_month()
print_highest_and_lowest_price_per_year()
sort_data_asc()
from_lowest_to_highest()
from_highest_to_lowest()
