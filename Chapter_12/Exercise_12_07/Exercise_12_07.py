"""
7. Recursive Power Method
Design a function that uses recursion to raise a number to a power. The function should
accept two arguments: the number to be raised, and the exponent. Assume the exponent is
a nonnegative integer.

@author Sharaf Qeshta
"""


def recursive_power(number, exponent):
    if exponent == 0:
        return 1
    return number * recursive_power(number, exponent - 1)


def main():
    print(recursive_power(2, 3))
    print(recursive_power(2, 5))
    print(recursive_power(5, 2))
    print(recursive_power(11, 3))


main()
