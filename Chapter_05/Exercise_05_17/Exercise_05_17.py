"""
17. Prime Numbers
A prime number is a number that is only evenly divisible by itself and 1. For example, the
number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, however,
is not prime because it can be divided evenly by 1, 2, 3, and 6.
Write a Boolean function named is_prime which takes an integer as an argument and
returns true if the argument is a prime number, or false otherwise. Use the function in
a program that prompts the user to enter a number then displays a message indicating
whether the number is prime.


@author Sharaf Qeshta
"""


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


number_ = int(input("enter a number: "))

if is_prime(number_):
    print(f"{number_} is prime")
else:
    print(f"{number_} is not prime")
