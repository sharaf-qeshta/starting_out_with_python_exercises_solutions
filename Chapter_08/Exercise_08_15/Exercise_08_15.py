"""
15. Caesar Cipher
A “Caesar Cipher” is a simple way of encrypting a message by replacing each letter with a
letter a certain number of spaces up the alphabet. For example, if shifting the message by
13 an A would become an N, while an S would wrap around to the start of the alphabet to
become an F.
Write a program that asks the user for a message (a string) and a shift amount (an integer).
The values should be passed to a function that accepts a string and an integer as arguments,
and returns a string representing the original string encrypted by shifting the letters by the
integer. For example, a string of “BEWARE THE IDES OF MARCH” and an integer of 13
should result in a string of “ORJNER GUR VQRF BS ZNEPU”.


@author Sharaf Qeshta
"""

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']


def increment_by(number, by):
    if number + by > 25:
        return (number + by - 1) - 25
    return number + by


def encrypt(string, shifted_by):
    encrypted = ""
    for character in string:
        if character == ' ':
            encrypted += character
            continue
        encrypted += LETTERS[increment_by(ord(character) - 65, shifted_by)]
    return encrypted


def main():
    string = input("enter a string: ")
    shifted_by = int(input("enter an integer to shift letters by: "))
    print(encrypt(string, shifted_by))


main()
