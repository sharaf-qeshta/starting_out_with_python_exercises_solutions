"""
10. Word Index
Write a program that reads the contents of a text file. The program should create a dictionary
 in which the key-value pairs are described as follows:
• Key. The keys are the individual words found in the file.
• Values. Each value is a list that contains the line numbers in the file where the word
(the key) is found.

For example, suppose the word “robot” is found in lines 7, 18, 94, and 138. The dictionary
would contain an element in which the key was the string “robot”, and the value was a list
containing the numbers 7, 18, 94, and 138.
Once the dictionary is built, the program should create another text file, known as a word
index, listing the contents of the dictionary. The word index file should contain an alphabetical
 listing of the words that are stored as keys in the dictionary, along with the line
numbers where the words appear in the original file. Figure 9-1 shows an example of an
original text file (Kennedy.txt) and its index file (index.txt).

@author Sharaf Qeshta
"""

data = {}


def build_dictionary():
    try:
        file = open("kennedy.txt")
        line_number = 1
        for line in file:
            line = line.replace("\n", "")
            words = line.split(" ")
            for word in words:
                lines_list = data.get(word, [])
                lines_list.append(line_number)
                data[word] = lines_list
            line_number += 1
        file.close()
    except Exception as error:
        print(error)


def write_data():
    try:
        file = open("index.txt", "a")
        for key, value in data.items():
            string_to_write = key + ":"
            for line_number in value:
                string_to_write += f" {line_number}"
            file.write(f"{string_to_write}\n")
        file.close()
    except Exception as error:
        print(error)


def main():
    build_dictionary()
    write_data()


main()
