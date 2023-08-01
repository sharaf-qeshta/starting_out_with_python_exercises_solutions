"""
16. Odd/Even Counter
In this chapter, you saw an example of how to write an algorithm that determines
whether a number is even or odd. Write a program that generates 100 random numbers
and keeps a count of how many of those random numbers are even, and how many of
them are odd.


@author Sharaf Qeshta
"""
from random import randint

odds_count = 0
even_count = 0

for i in range(100):
    number = randint(1, 1000)
    if number % 2 == 0:
        even_count += 1
    else:
        odds_count += 1

print(f"we got {odds_count} odd numbers and {even_count} even numbers between 100 random numbers")