"""
13.Planting Grapevines
A vineyard owner is planting several new rows of grapevines, and needs to know how many
grapevines to plant in each row. She has determined that after measuring the length of a
future row, she can use the following formula to calculate the number of vines that will fit
in the row, along with the trellis end-post assemblies that will need to be constructed at
each end of the row:
V 5 R 2 2E
 S
The terms in the formula are:
V is the number of grapevines that will fit in the row.
R is the length of the row, in feet.
E is the amount of space, in feet, used by an end-post assembly.
S is the space between vines, in feet.
Write a program that makes the calculation for the vineyard owner. The program should
ask the user to input the following:
• The length of the row, in feet
• The amount of space used by an end-post assembly, in feet
• The amount of space between the vines, in feet
Once the input data has been entered, the program should calculate and display
 the number of grapevines that will fit in the row.

@author Sharaf Qeshta
"""

R = float(input("enter the length of the row, in feet:"))
E = float(input("enter the amount of space used by an end-post assembly, in feet:"))
S = float(input("enter the amount of space between the vines, in feet:"))
V = (R - 2 * E) / S
print("the number of grapevines that will fit in the row is", V)
