"""
12. File Line Viewer
Write a program that asks the user for the name of a file. The program should read all of
the file’s data into a list and display the number of lines of data that the file contains, and
then ask the user to enter the number of the line that they want to view. The program should
display the specified line.
The program should handle the following exceptions by displaying an error message:
•	 IOError exceptions that are raised when the specified filename cannot be found or
opened.
•	 ValueError exceptions that are raised when a non-integer value is given as a line number.
•	 IndexError exceptions that are raised when the line number is outside the range of the
data list.


@author Sharaf Qeshta
"""


def main():
    try:
        file_name = input("Enter a file name: ")
        file = open(file_name)
        lines = []

        for line in file:
            lines.append(line)

        print("the file contains", len(lines), "Lines")
        line_number = int(input("enter a line number to view: ")) - 1
        print(lines[line_number])
    except IOError:
        print("the specified filename cannot be found or opened.")
    except ValueError:
        print("a non-integer value is given as a line number.")
    except IndexError:
        print("the line number is outside the range of the data list.")


main()
