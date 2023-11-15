"""
3. File Encryption and Decryption
Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For
example:
codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .}
Using this example, the letter A would be assigned the symbol %, the letter a would be
assigned the number 9, the letter B would be assigned the symbol @, and so forth.
The program should open a specified text file, read its contents, then use the dictionary
to write an encrypted version of the file’s contents to a second file. Each character in the
second file should contain the code for the corresponding character in the first file.
Write a second program that opens an encrypted file and displays its decrypted contents
on the screen.


@author Sharaf Qeshta
"""

codes = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%', 'F': '^', 'G': '&', 'H': '*', 'I': '(',
         'J': ')', 'K': '-', 'L': '_', 'M': '+', 'N': '=', 'O': '`', 'P': '~', 'Q': '{', 'R': '[',
         'S': '}', 'T': ']', 'U': ':', 'V': ';', 'W': '"', 'X': '<', 'Y': '>', 'Z': '0', 'a': '1',
         'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '¤',
         'k': '¶', 'l': '§', 'm': 'Ç', 'n': 'ü', 'o': 'é', 'p': 'â', 'q': 'ä', 'r': 'à', 's': 'å',
         't': 'ç', 'u': 'ê', 'v': 'ë', 'w': 'è', 'x': 'æ', 'y': 'Æ', 'z': 'ô'}


def encrypt_file(file_name):
    try:
        source = open(file_name)
        target = open("target.txt", "a")
        for line in source:
            current_line = ""
            for character in line:
                current_line += codes.get(character, character)
            target.write(current_line + "\n")
    except Exception as error:
        print(error)


def decrypt_file(file_name):
    try:
        source = open(file_name)
        for line in source:
            current_line = ""
            for character in line:
                current_line += find_key_by_value(character)
            print(current_line)
    except Exception as error:
        print(error)


def find_key_by_value(value):
    for key, value1 in codes.items():
        if value1 == value:
            return key
    return value


encrypt_file("source.txt")
decrypt_file("target.txt")
