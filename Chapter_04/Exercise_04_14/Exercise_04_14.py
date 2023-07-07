"""
14. Write a program that uses nested loops to draw this pattern:
*******
******
*****
****
***
**
*

@author Sharaf Qeshta
"""

for i in range(7):
    output = ""
    for j in range(7 - i):
        output += "*"
    print(output)
