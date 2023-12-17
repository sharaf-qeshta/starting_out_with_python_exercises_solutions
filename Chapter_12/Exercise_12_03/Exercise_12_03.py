"""
3. Recursive Lines
Write a recursive function that accepts an integer argument, n. The function should display
n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
showing 2 asterisks, up to the nth line which shows n asterisks.

@author Sharaf Qeshta
"""


def recursive_lines(n):
    if n == 0:
        return
    recursive_lines(n - 1)
    print("*" * n)


def main():
    recursive_lines(5)
    recursive_lines(8)
    recursive_lines(12)


main()
