"""
3. Line Numbers
Write a program that asks the user for the name of a file. The program should display the
contents of the file with each line preceded with a line number followed by a colon. The
line numbering should start at 1.

@author Sharaf Qeshta
"""


def main(file_name_):
    try:
        file = open(file_name_)
        line_number = 1
        for line in file:
            print(f"{line_number}: {line}", end='')
            line_number += 1
        file.close()
    except Exception as error:
        print(error)


file_name = input("enter file name: ")
main(file_name)
