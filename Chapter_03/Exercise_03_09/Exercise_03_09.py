"""
9. Roulette Wheel Colors
On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are
as follows:
•	 Pocket 0 is green.
•	 For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
pockets are black.
•	 For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered
pockets are red.
•	 For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered
pockets are black.
•	 For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered
pockets are red.
Write a program that asks the user to enter a pocket number and displays whether the
pocket is green, red, or black. The program should display an error message if the user
enters a number that is outside the range of 0 through 36.

@author Sharaf Qeshta
"""

pocket_number = int(input("Enter a pocket number: "))
if pocket_number < 0 or pocket_number > 36:
    print("pocket number must be between 0 and 36")
else:
    is_even = pocket_number % 2 == 0
    if pocket_number == 0:
        print("Green")
    elif pocket_number < 11:
        if is_even:
            print("black")
        else:
            print("red")
    elif pocket_number < 19:
        if is_even:
            print("red")
        else:
            print("black")
    elif pocket_number < 29:
        if is_even:
            print("black")
        else:
            print("red")
    else:
        if is_even:
            print("red")
        else:
            print("black")