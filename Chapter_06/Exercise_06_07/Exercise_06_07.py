"""
7. Word List File Writer
Write a program that asks the user how many words they would like to write to a file, and
then asks the user to enter that many words, one at a time. The words should be written
to a file.


@author Sharaf Qeshta
"""


def main():
    words_count = int(input("how many words you want to insert: "))
    try:
        file = open("names.txt", "w")
        for i in range(words_count):
            file.write(input("enter a word: ") + "\n")
    except Exception as error:
        print(error)

main()