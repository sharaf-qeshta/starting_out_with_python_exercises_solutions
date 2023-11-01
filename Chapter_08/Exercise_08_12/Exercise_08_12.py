"""
12. Pig Latin
Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In
one version, to convert a word to Pig Latin, you remove the first letter and place that letter
at the end of the word. Then, you append the string “ay” to the word. Here is an example:
English: I SLEPT MOST OF THE NIGHT
Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY


@author Sharaf Qeshta
"""


def convert_to_pig_latin(word):
    first_character = word[0]
    pig_latin_form = ""
    for i in range(1, len(word)):
        pig_latin_form = pig_latin_form + word[i]

    pig_latin_form = pig_latin_form + first_character + "AY"
    return pig_latin_form


def main(sentence):
    words = sentence.split(" ")
    pig_latin_form = ""
    for word in words:
        pig_latin_form = pig_latin_form + convert_to_pig_latin(word) + " "
    print(pig_latin_form)


main("I SLEPT MOST OF THE NIGHT")  # IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY
