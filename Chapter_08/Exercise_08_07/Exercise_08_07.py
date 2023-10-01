"""
7. Character Analysis
If you have downloaded the source code you will find a file named text.txt in the Chapter 08
folder. Write a program that reads the file’s contents and determines the following:
• The number of uppercase letters in the file
• The number of lowercase letters in the file
• The number of digits in the file
• The number of whitespace characters in the file


@author Sharaf Qeshta
"""


def main():
    try:
        file = open("text.txt")
        uppercase_letters = 0
        lowercase_letters = 0
        digits = 0
        whitespaces = 0
        for line in file:
            for character in line:
                if character.isspace():
                    whitespaces += 1
                elif character.isdigit():
                    digits += 1
                elif character.islower():
                    lowercase_letters += 1
                elif character.isupper():
                    uppercase_letters += 1
        print(f"The number of uppercase letters in the file is {uppercase_letters}")
        print(f"The number of lowercase letters in the file is {lowercase_letters}")
        print(f"The number of digits in the file is {digits}")
        print(f"The number of whitespace characters in the file is {whitespaces}")
    except Exception as error:
        print(error)


main()
