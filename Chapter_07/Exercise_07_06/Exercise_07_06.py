"""
6. Dice Rolling Function
In a program, write a function named roll that accepts an integer argument number_
of_throws. The function should generate and return a sorted list of number_of_throws
random numbers between 1 and 6. The program should prompt the user to enter a positive
integer that is sent to the function, and then print the returned list.


@author Sharaf Qeshta
"""

from random import randint


def roll(number_of_throws):
    result = []
    for i in range(number_of_throws):
        result.append(randint(1, 6))
    return result


def main():
    number_of_throws = int(input("enter number of throws: "))
    result = roll(number_of_throws)
    for i in result:
        print(i, end=' ')


main()
