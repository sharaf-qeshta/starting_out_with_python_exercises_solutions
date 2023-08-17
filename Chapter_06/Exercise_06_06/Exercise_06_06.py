"""
6. Average of Numbers
Assume a file containing a series of integers is named numbers.txt and exists on the
computer’s disk. Write a program that calculates the average of all the numbers stored in
the file


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
    except Exception as error:
        print(error)


main()
