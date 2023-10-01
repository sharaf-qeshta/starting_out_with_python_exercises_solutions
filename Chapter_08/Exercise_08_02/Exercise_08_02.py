"""
2. Sum of Digits in a String
Write a program that asks the user to enter a series of single-digit numbers with nothing
separating them. The program should display the sum of all the single digit numbers in the
string. For example, if the user enters 2514, the method should return 12, which is the sum
of 2, 5, 1, and 4.


@author Sharaf Qeshta
"""


def sum_all_digits(string):
    total = 0
    for character in string:
        total += int(character)
    return total


def main():
    digits = input("Enter digits: ")
    print(sum_all_digits(digits))


main()
