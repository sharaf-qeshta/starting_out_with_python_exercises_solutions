"""
15. Write a program that uses nested loops to draw this pattern:
##
# #
# #
# #
# #
# #


@author Sharaf Qeshta
"""

for i in range(6):
    output = ""
    for j in range(i):
        output += " "
    print(f"#{output}#")

