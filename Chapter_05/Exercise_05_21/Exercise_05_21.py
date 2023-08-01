"""
21. Rock, Paper, Scissors Game
Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.
 The program should work as follows:
1. When the program begins, a random number in the range of 1 through 3 is generated.
If the number is 1, then the computer has chosen rock. If the number is 2, then the
computer has chosen paper. If the number is 3, then the computer has chosen scissors.
(Don’t display the computer’s choice yet.)
2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.
3. The computer’s choice is displayed.
4. A winner is selected according to the following rules:
•	 If one player chooses rock and the other player chooses scissors, then rock wins.
(Rock smashes scissors.)
•	 If one player chooses scissors and the other player chooses paper, then scissors wins.
(Scissors cuts paper.)
•	 If one player chooses paper and the other player chooses rock, then paper wins.
(Paper wraps rock.)
•	 If both players make the same choice, the game must be played again to determine
the winner.


@author Sharaf Qeshta
"""

from random import randint


def get_choice_name(choice):
    if choice == 1:
        return "Rock"
    if choice == 2:
        return "Paper"
    return "Scissor"


def determine_winner(computer_choice_int, user_choice_int):
    difference = abs(computer_choice_int - user_choice_int)
    if difference == 1:
        if computer_choice_int > user_choice_int:
            return "computer win"
        else:
            return "user win"
    if difference == 2:
        if computer_choice_int < user_choice_int:
            return "computer win"
        else:
            return "user win"
    return "Draw"


computer_choice = randint(1, 3)
user_choice = int(input("enter your choice Rock 1, Paper 2, Scissor 3: "))
print("the computer choose", get_choice_name(computer_choice))
print(determine_winner(computer_choice, user_choice))