"""
6. Average Number of Words
If you have downloaded the source code from the Premium Companion Website you will
find a file named text.txt in the Chapter 08 folder. The text that is in the file is stored
as one sentence per line. Write a program that reads the file’s contents and calculates the
average number of words per sentence.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com/gaddis.)

@author Sharaf Qeshta
"""


def main():
    try:
        file = open("text.txt")
        words_count = 0
        lines_count = 0
        for line in file:
            words_count += len(line.split(" "))
            lines_count += 1
        print("The average words in a sentence in this file is", words_count / lines_count)
    except Exception as error:
        print(error)


main()
