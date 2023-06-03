"""
8. Hot Dog Cookout Calculator
Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a
program that calculates the number of packages of hot dogs and the number of packages of
hot dog buns needed for a cookout, with the minimum amount of leftovers. The program
should ask the user for the number of people attending the cookout and the number of hot
dogs each person will be given. The program should display the following details:
•	 The minimum number of packages of hot dogs required
•	 The minimum number of packages of hot dog buns required
•	 The number of hot dogs that will be left over
•	 The number of hot dog buns that will be left over


@author Sharaf Qeshta
"""
people = int(input("enter the number of people attending the cookout:"))
hotdog_for_each = int(input("enter the number of hotdogs given to each person:"))

hotdog_count = people * hotdog_for_each

hotdog_packages = int(hotdog_count / 10)
if hotdog_packages % 10 > 0:
    hotdog_packages = hotdog_packages + 1

bun_packages = int(hotdog_count / 8)
if bun_packages % 8 > 0:
    bun_packages = bun_packages + 1

print("The minimum number of packages of hot dogs required is", hotdog_packages)
print("The minimum number of packages of hot dog buns required is", bun_packages)
print("The number of hot dogs that will be left over is", hotdog_packages * 10 % hotdog_count)
print("The number of hot dog buns that will be left over", bun_packages * 8 % hotdog_count)

