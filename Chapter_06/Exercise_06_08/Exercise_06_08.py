"""
8. Word List File Reader
This exercise assumes you have completed the Programming Exercise 7, Word List File
Writer. Write another program that reads the words from the file and displays the following data:
•	 The number of words in the file.
•	 The longest word in the file.
•	 The average length of all of the words in the file.


@author Sharaf Qeshta
"""


def main():
    try:
        file = open("names.txt")
        words_count = 0
        total_lengths = 0
        longest_word = ""
        for line in file:
            word_length = len(line) - 1
            words_count += 1
            total_lengths += word_length
            if len(longest_word) - 1 < word_length:
                longest_word = line
        print("The number of words in the file is", words_count)
        print("The longest word in the file", longest_word)
        print("The average length of all of the words in the file is", total_lengths / words_count)
    except Exception as error:
        print(error)


main()
