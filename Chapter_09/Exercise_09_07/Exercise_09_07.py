"""
7. World Series Winners
In this chapter’s source code folder (available on the Premium Companion Website at www.
pearsonglobaleditions.com/gaddis), you will find a text file named WorldSeriesWinners.
txt. This file contains a chronological list of the World Series’ winning teams from 1903
through 2009. The first line in the file is the name of the team that won in 1903, and the
last line is the name of the team that won in 2009. (Note the World Series was not played
in 1904 or 1994. There are entries in the file indicating this.)
Write a program that reads this file and creates a dictionary in which the keys are the names
of the teams, and each key’s associated value is the number of times the team has won the
World Series. The program should also create a dictionary in which the keys are the years,
and each key’s associated value is the name of the team that won that year.
The program should prompt the user for a year in the range of 1903 through 2009. It
should then display the name of the team that won the World Series that year, and the
number of times that team has won the World Series.


@author Sharaf Qeshta
"""

number_of_winnings = {}
each_year_winnings = {}


def load_data():
    try:
        file = open("WorldSeriesWinners.txt")
        start_year = 1903
        for line in file:
            number_of_winnings[line] = number_of_winnings.get(line, 0) + 1
            if start_year == 1904 or start_year == 2007:
                start_year += 1
            each_year_winnings[start_year] = line
            start_year += 1
        file.close()
    except Exception as error:
        print(error)


def main():
    load_data()
    year = int(input("enter a year in the range of 1903 through 2009: "))
    winning_team = each_year_winnings.get(year, "No Name")
    print(
        f"the winning team in {year} is {winning_team} and it wins the world series {number_of_winnings.get(winning_team, 0)} times.")


main()
