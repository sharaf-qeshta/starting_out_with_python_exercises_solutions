"""
10. Most Frequent Character
Write a program that lets the user enter a string and displays the character that appears most
frequently in the string.

@author Sharaf Qeshta
"""


def count_the_most_occurrence(string):
    counter = [0] * 122
    for character in string:
        counter[ord(character)] += counter[ord(character)] + 1

    most_occurrence_count = 0
    most_occurrence_character = ''
    for character in string:
        if counter[ord(character)] > most_occurrence_count:
            most_occurrence_count = counter[ord(character)]
            most_occurrence_character = character
    print(most_occurrence_character)
    return most_occurrence_character


def main():
    string = input("Enter a string: ")
    print("The most occurred character in",
          string, "is", count_the_most_occurrence(string))


main()
