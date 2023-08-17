"""
5. Sum of Numbers
Assume a file containing a series of integers is named numbers.txt and exists on the
computer’s disk. Write a program that reads all of the numbers stored in the file and calculates
their total.


@author Sharaf Qeshta
"""


def main():
    try:
        file = open("numbers.txt")
        total = 0
        for line in file:
            total += float(line)
        print(f"total : {total}")
    except Exception as error:
        print(error)


main()
