"""
8. Name Search
If you have downloaded the source code you will find the following files in the Chapter 07
folder:
•	 GirlNames.txt This file contains a list of the 200 most popular names given to girls
born in the United States from the year 2000 through 2009.
•	 BoyNames.txt This file contains a list of the 200 most popular names given to boys
born in the United States from the year 2000 through 2009.
Write a program that reads the contents of the two files into two separate lists. The user
should be able to enter a boy’s name, a girl’s name, or both, and the application will display
messages indicating whether the names were among the most popular.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com/gaddis.)


@author Sharaf Qeshta
"""


def main():
    boys_names = []
    girls_names = []
    try:
        boys_file = open("BoyNames.txt")
        for line in boys_file:
            boys_names.append(line.strip())
        girls_file = open("GirlNames.txt")
        for line in girls_file:
            girls_names.append(line)
    except Exception as error:
        print(error)

    name = input("Enter a name: ")
    if name in boys_names or name in girls_names:
        print(f"the name {name} exist among the most popular names")
    else:
        print(f"the name {name} is not exist among the most popular names")


main()
