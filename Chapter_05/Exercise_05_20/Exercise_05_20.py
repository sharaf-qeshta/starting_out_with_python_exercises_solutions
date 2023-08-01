"""
20. Random Number Guessing Game
Write a program that generates a random number in the range of 1 through 100, and asks
the user to guess what the number is. If the user’s guess is higher than the random number,
the program should display “Too high, try again.” If the user’s guess is lower than the
random number, the program should display “Too low, try again.” If the user guesses the
number, the application should congratulate the user and generate a new random number
so the game can start over.
Optional Enhancement: Enhance the game so it keeps count of the number of guesses that
the user makes. When the user correctly guesses the random number, the program should
display the number of guesses.

@author Sharaf Qeshta
"""

from random import randint

number = randint(1, 100)
number_of_guesses = 0
while True:
    user_guess = int(input("enter a guess: "))
    if user_guess > number:
        print("Too high, try again.")
        number_of_guesses += 1
    elif user_guess < number:
        print("Too low, try again.")
        number_of_guesses += 1
    else:
        print("congratulation you got it right!")
        print("number of guesses is", number_of_guesses)
        number_of_guesses = 0
        number = randint(1, 100)