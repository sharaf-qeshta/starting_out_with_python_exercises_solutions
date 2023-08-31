"""
2. Lottery Number Generator
Design a program that generates a seven-digit lottery number.
 The program should generate seven random numbers, each in
 the range of 0 through 9, and assign each number to a
list element. (Random numbers were discussed in Chapter 5.) Then write another loop that
displays the contents of the list.


@author Sharaf Qeshta
"""

from random import randint


def main():
    lottery_numbers = []
    for i in range(7):
        lottery_numbers.append(randint(0, 9))
        print(lottery_numbers[i])


main()
