"""
8. Average Word Length
Write a program with a loop that repeatedly asks the user to enter a word. The user should
enter nothing (press Enter without typing anything) to signal the end of the loop. Once the
loop ends, the program should display the average length of the words entered, rounded to
the nearest whole number.

@author Sharaf Qeshta
"""

total_words_length = 0
number_of_words = 0
while True:
    word = input("enter a word:")
    if len(word) == 0:
        break
    number_of_words += 1
    total_words_length += len(word)

print(f"the average word length is {format(total_words_length/number_of_words, '.2f')}")