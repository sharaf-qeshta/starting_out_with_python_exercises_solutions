"""
1. File Display
Assume a file containing a series of integers is named numbers.txt
 and exists on the computer’s disk. Write a program that displays all of the numbers in the file.


 @author Sharaf Qeshta
"""


def main():
    try:
        infile = open("numbers.txt")
        for line in infile:
            print(line, end='')
    except Exception as error:
        print(error)


main()
