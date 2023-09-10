"""
10. World Series Champions
If you have downloaded the source code you will find a file named WorldSeriesWinners.
txt in the Chapter 07 folder. This file contains a chronological list of the World Series
winning teams from 1903 through 2009. (The first line in the file is the name of the team that
won in 1903, and the last line is the name of the team that won in 2009. Note the World
Series was not played in 1904 or 1994.)
Write a program that lets the user enter the name of a team, then displays the number of
times that team has won the World Series in the time period from 1903 through 2009.


@author Sharaf Qeshta
"""


def main():
    winners = []
    try:
        file = open("WorldSeriesWinners.txt")
        for line in file:
            winners.append(line.strip())
    except Exception as error:
        print(error)

    team = input("enter a team to search for: ")
    num_of_wins = 0
    for winner in winners:
        if winner == team:
            num_of_wins += 1

    print(f"team {team} wins the world series {num_of_wins} times")


main()
