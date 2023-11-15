"""
4. Unique Words
Write a program that opens a specified text file then displays a list of all the unique words
found in the file.
Hint: Store each word as an element of a set.


@author Sharaf Qeshta
"""


def display_unique_words(file_name):
    try:
        file = open(file_name)
        words = set()
        for line in file:
            words.update(line.split(" "))
        print(words)
    except Exception as error:
        print(error)


display_unique_words("source.txt")
