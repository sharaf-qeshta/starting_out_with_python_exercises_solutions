"""
11. Word Separator
Write a program that accepts as input a sentence in which all of the words are run together,
but the first character of each word is uppercase. Convert the sentence to a string in which
the words are separated by spaces, and only the first word starts with an uppercase letter. For
example the string “StopAndSmellTheRoses.” would be converted to “Stop and smell
the roses.”

@author Sharaf Qeshta
"""


def separate_words(string):
    current_word = ""
    final_string = ""
    for character in string:
        if character.isupper():
            final_string = final_string + current_word + " "
            current_word = character
        else:
            current_word = current_word + character
    final_string = final_string + current_word
    return final_string


def main():
    print(separate_words("StopAndSmellTheRoses."))


main()
