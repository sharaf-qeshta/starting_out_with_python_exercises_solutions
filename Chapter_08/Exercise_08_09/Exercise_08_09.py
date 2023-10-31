"""
9. Vowels and Consonants
Write a program with a function that accepts a string as an argument and returns the
number of vowels that the string contains. The application should have another function
that accepts a string as an argument and returns the number of consonants that the string
contains. The application should let the user enter a string, and should display the number
of vowels and the number of consonants it contains.

@author Sharaf Qeshta
"""


def count_vowels(string):
    vowels = ['a', 'i', 'o', 'e', 'y']
    vowels_count = 0
    for character in string:
        if character in vowels:
            vowels_count += 1
    return vowels_count


def count_consonants(string):
    consonants_count = 0
    vowels = ['a', 'i', 'o', 'e', 'y']
    for character in string:
        if character.isalpha() and character not in vowels:
            consonants_count += 1
    return consonants_count


print(count_consonants("Sharaf"))  # 4
print(count_vowels("Sharaf"))  # 2
