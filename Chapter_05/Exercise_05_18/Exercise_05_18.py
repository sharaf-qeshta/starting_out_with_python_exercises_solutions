"""
18. Prime Number List
This exercise assumes that you have already written the is_prime function in Programming
Exercise 17. Write another program that displays all of the prime numbers from 1 to 100.
The program should have a loop that calls the is_prime function.

@author Sharaf Qeshta
"""


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


for i in range(2, 101):
    if is_prime(i):
        print(i)
