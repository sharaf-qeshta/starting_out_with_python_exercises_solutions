"""
1. Recursive Printing
Design a recursive function that accepts an integer argument, n, and prints every second
number from n down to a minimum of 0. Assume that n is always a positive integer.


@author Sharaf Qeshta
"""


def count_down_printing(n):
    if n < 0:
        return
    print(n)
    count_down_printing(n - 2)


def main():
    count_down_printing(10)
    count_down_printing(12)
    count_down_printing(7)


main()
