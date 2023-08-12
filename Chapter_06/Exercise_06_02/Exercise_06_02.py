"""
2. File Head Display
Write a program that asks the user for the name of a file. The program should display only
the first five lines of the file’s contents. If the file contains less than five lines, it should
display the file’s entire contents.

@author Sharaf Qeshta
"""


def main(file_name_):
    try:
        file = open(file_name_)
        lines = 0
        for line in file:
            print(line, end='')
            lines += 1
            if lines == 5:
                break
        file.close()
    except Exception as error:
        print(error)


file_name = input("enter file name: ")
main(file_name)
