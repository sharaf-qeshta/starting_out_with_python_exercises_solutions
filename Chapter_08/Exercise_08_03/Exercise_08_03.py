"""
3. Date Printer
Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.
It should print the date in the format March 12, 2018.


@author Sharaf Qeshta
"""


def get_month(month_number):
    if month_number == 1:
        return "January"
    elif month_number == 2:
        return "February"
    elif month_number == 3:
        return "March"
    elif month_number == 4:
        return "April"
    elif month_number == 5:
        return "May"
    elif month_number == 6:
        return "June"
    elif month_number == 7:
        return "July"
    elif month_number == 8:
        return "August"
    elif month_number == 9:
        return "September"
    elif month_number == 10:
        return "October"
    elif month_number == 11:
        return "November"
    elif month_number == 12:
        return "December"
    return "None"


def main():
    date = input("Enter a date in the form mm/dd/yyyy:")
    date_contents = date.split("/")
    month = get_month(int(date_contents[0]))
    day = date_contents[1]
    year = date_contents[2]
    print(f"{month} {day}, {year}")


main()
