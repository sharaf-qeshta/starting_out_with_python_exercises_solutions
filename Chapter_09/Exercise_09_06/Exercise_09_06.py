"""
6. File Analysis
Write a program that reads the contents of two text files and compares them in the following ways:
• It should display a list of all the unique words contained in both files.
• It should display a list of the words that appear in both files.
• It should display a list of the words that appear in the first file but not the second.
• It should display a list of the words that appear in the second file but not the first.
• It should display a list of the words that appear in either the first or second file, but not
both.
Hint: Use set operations to perform these analyses.


@author Sharaf Qeshta
"""

first_file_words = set()
second_file_words = set()


def load_words(file_name_1, file_name_2):
    try:
        file1 = open(file_name_1)
        for line in file1:
            words = line.split(" ")
            for word in words:
                first_file_words.add(word)
        file1.close()

        file2 = open(file_name_2)
        for line in file2:
            words = line.split(" ")
            for word in words:
                second_file_words.add(word)
        file2.close()
    except Exception as error:
        print(error)


def print_words_in_both_files():
    print(f"words in the first file is {first_file_words}")
    print(f"words in the second file is {second_file_words}")


def print_words_appears_in_both_files():
    print(f"the words appears in both files is {first_file_words & second_file_words}")


def print_words_appears_in_the_first_file():
    print(f"the words appears in the first file only is {first_file_words.difference(second_file_words)}")


def print_words_appears_in_the_second_file():
    print(f"the words appears in the second file only is {second_file_words.difference(first_file_words)}")


def print_words_appears_in_either_files():
    print(
        f"the words appears in either files is {(first_file_words | second_file_words).difference(first_file_words & second_file_words)}")


load_words("source.txt", "target.txt")
print_words_in_both_files()
print_words_appears_in_both_files()
print_words_appears_in_the_first_file()
print_words_appears_in_the_second_file()
print_words_appears_in_either_files()
