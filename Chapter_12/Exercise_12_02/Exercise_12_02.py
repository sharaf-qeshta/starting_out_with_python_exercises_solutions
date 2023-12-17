"""
2. Recursive Multiplication
Design a recursive function that accepts two arguments into the parameters x and y. The
function should return the value of x times y. Remember, multiplication can be performed
as repeated addition as follows:
7 3 4 5 4 1 4 1 4 1 4 1 4 1 4 1 4
(To keep the function simple, assume x and y will always hold positive nonzero integers.)


@author Sharaf Qeshta
"""


def recursive_multiplication(x, y):
    if y == 0:
        return 0
    else:
        return x + recursive_multiplication(x, y - 1)


def main():
    print(recursive_multiplication(2, 3))  # 6
    print(recursive_multiplication(7, 8))  # 56
    print(recursive_multiplication(12, 11))  # 132
    print(recursive_multiplication(5, 25))  # 125
    print(recursive_multiplication(24, 20))  # 480
    print(recursive_multiplication(33, 3))  # 99


main()
