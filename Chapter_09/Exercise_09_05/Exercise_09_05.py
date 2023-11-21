"""
5. Random Number Frequencies
Write a program that generates 100 random numbers between 1 and 10. The program
should store the frequency of each number generated in a dictionary with the number as
the key and the amount of times it has occurred as the value. For example, if the program
generates the number 6 a total of 11 times, the dictionary will contain a key of 6 with an
associated value of 11. Once all of the numbers have been generated, display information
about the frequency of each number.


@author Sharaf Qeshta
"""

import random


def main():
    data = {}
    for i in range(100):
        current_number = random.randint(1, 10)
        data[current_number] = data.get(current_number, 0) + 1
    print(data)


main()
