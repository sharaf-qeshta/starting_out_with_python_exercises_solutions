"""
5. Alphabetic Telephone Number Translator
Many companies use telephone numbers like 555-GET-FOOD so the number is easier for
their customers to remember. On a standard telephone, the alphabetic letters are mapped to
numbers in the following fashion:
A, B, and C = 2
D, E, and F = 3
G, H, and I = 4
J, K, and L = 5
M, N, and O = 6
P, Q, R, and S = 7
T, U, and V = 8
W, X, Y, and Z = 9
Write a program that asks the user to enter a 10-character telephone number in the format
 XXX-XXX-XXXX. The application should display the telephone number with any
alphabetic characters that appeared in the original translated to their numeric equivalent.
 For example, if the user enters 555-GET-FOOD, the application should display
555-438-3663.


@author Sharaf Qeshta
"""

keyboard = \
    {
        "A": 2, "B": 2, "C": 2,
        "D": 3, "E": 3, "F": 3,
        "G": 4, "H": 4, "I": 4,
        "J": 5, "K": 5, "L": 5,
        "M": 6, "N": 6, "O": 6,
        "P": 7, "Q": 7, "R": 7, "S": 7,
        "T": 8, "U": 8, "V": 8,
        "W": 9, "X": 9, "Y": 9, "Z": 9
    }


def get_a_number(phone_number):
    phone_number = phone_number.upper()
    original_phone_number = ""
    for character in phone_number:
        if character.isdigit() or character == "-":
            original_phone_number += character
        else:
            original_phone_number += str(keyboard[character])
    return original_phone_number


def main():
    phone_number = input("enter a phone number: ")
    print(get_a_number(phone_number))


main()
