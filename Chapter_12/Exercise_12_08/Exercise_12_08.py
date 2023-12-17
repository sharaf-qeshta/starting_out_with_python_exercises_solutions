"""
8. Ackermann’s Function
Ackermann’s Function is a recursive mathematical algorithm that can be used to test how
well a system optimizes its performance of recursion. Design a function ackermann(m, n),
which solves Ackermann’s function. Use the following logic in your function:
If m 5 0 then return n 1 1
If n 5 0 then return ackermann(m 2 1, 1)
Otherwise, return ackermann(m 2 1, ackermann(m, n 2 1))
Once you’ve designed your function, test it by calling it with small values for m and n.


@author Sharaf Qeshta
"""


def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


def main():
    print(ackermann(1, 2))


main()
