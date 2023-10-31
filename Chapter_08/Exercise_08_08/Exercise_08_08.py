"""
 8. Sentence Capitalizer
 Write a program with a function that accepts a string as an argument and returns a copy
of the string with the first character of each sentence capitalized. For instance, if the argu
ment is “hello. my name is Joe. what is your name?” the function should return the string
“Hello. My name is Joe. What is your name?” The program should let the user enter
a string and then pass it to the function. The modified string should be displayed.


@author Sharaf Qeshta
"""

def capitalize_first_letters(text):
    sentences = text.split(". ")
    newText = ""
    for sentence in sentences:
        first_letter_capitalized = sentence[0].upper()
        newText += first_letter_capitalized + sentence[1:] + ". "
    return newText[0:-2]
    
def main():
    print(capitalize_first_letters("hello. my name is Joe. what is your name?"))

main()