"""
12. Maximum of Two Values
Write a function named max that accepts two integer values as arguments and returns the
value that is the greater of the two. For example, if 7 and 12 are passed as arguments to
the function, the function should return 12. Use the function in a program that prompts the
user to enter two integer values. The program should display the value that is the greater
of the two.


@author Sharaf Qeshta
"""

def max(x, y):
    if x >= y:
        return x
    return y

num1 = int(input("enter num2: "))
num2 = int(input("enter num2: "))
print(f"the maximum number between {num1} and {num2} is {max(num1, num2)}")