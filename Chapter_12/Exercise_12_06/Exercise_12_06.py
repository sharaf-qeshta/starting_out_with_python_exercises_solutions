"""
6. Determining Palindromes
Design a function that accepts a string as an argument. Assume that the string will contain
a single word. The function should use recursion to determine whether the word is a palindrome
 (a word that reads the same backwards as forward).
Hint: Use string slicing to refer to and compare the characters on either end of the string.

@author Sharaf Qeshta
"""


def determine_palindrome(string, end, palindrome):
    if end == 0:
        return string == palindrome + string[end]
    return determine_palindrome(string, end - 1, palindrome + string[end])


def main():
    print(determine_palindrome("cat", len("cat") - 1, ""))
    print(determine_palindrome("civic", len("civic") - 1, ""))
    print(determine_palindrome("kayak", len("kayak") - 1, ""))
    print(determine_palindrome("Sharaf", len("Sharaf") - 1, ""))
    print(determine_palindrome("level", len("level") - 1, ""))


main()
