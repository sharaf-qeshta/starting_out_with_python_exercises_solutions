"""
9. Exception Handing
Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
•	 It should handle any IOError exceptions that are raised when the file is opened and data
is read from it.
•	 It should handle any ValueError exceptions that are raised when the items that are read
from the file are converted to a number.


@author Sharaf Qeshta
"""


def main():
    try:
        file = open("numbers.txt")
        total = 0
        count = 0
        for line in file:
            count += 1
            total += float(line)
        print(f"Average : {total / count}")
    except IOError as ioError:
        print(ioError)
    except ValueError as valueError:
        print(valueError)
    except Exception as error:
        print(error)


main()
