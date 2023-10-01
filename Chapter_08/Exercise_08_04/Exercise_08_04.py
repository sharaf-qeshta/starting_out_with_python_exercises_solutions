"""
4. Morse Code Converter
Morse code is a code where each letter of the English alphabet, each digit, and various
punctuation characters are represented by a series of dots and dashes. Table 8-4 shows part
of the code.
Write a program that asks the user to enter a string, then converts that string to Morse code.


@author Sharaf Qeshta
"""

morse_dictionary = \
    {
        " ": "  ",
        ",": "– – . . – –",
        ".": ". – . – . –",
        "?": ". . – – . .",
        "0": "– – – – –",
        "1": ". – – – –",
        "2": ". . – – –",
        "3": ". . . – –",
        "4": ". . . . –",
        "5": ". . . . .",
        "6": "– . . . .",
        "7": "– – . . .",
        "8": "– – – . .",
        "9": "– – – – .",
        "A": ". – ",
        "B": "– . . .",
        "C": "– . – .",
        "D": "– . .",
        "E": ".",
        "F": ". . – .",
        "G": "– – .",
        "H": ". . . .",
        "I": ". .",
        "J": ". – – –",
        "K": "– . –",
        "L": ". – . .",
        "M": "– –",
        "N": "– .",
        "O": "– – –",
        "P": ". – – .",
        "Q": "– – . –",
        "R": ". – .",
        "S": ". . .",
        "T": "-",
        "U": ". . –",
        "V": ". . . –",
        "W": ". – –",
        "X": "– . . –",
        "Y": "– . –",
        "Z": "– – . ."
    }


def convert_to_morse_code(string):
    morse_string = ""
    string = string.upper()
    for character in string:
        morse_string += morse_dictionary[character]
    return morse_string


def main():
    plain_text = input("enter a string: ")
    print(convert_to_morse_code(plain_text))


main()
