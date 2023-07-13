"""
3. How Much Insurance?
Many financial experts advise that property owners should insure their homes or buildings
for at least 80 percent of the amount it would cost to replace the structure. Write a program
that asks the user to enter the replacement cost of a building, then displays the minimum
amount of insurance he or she should buy for the property.

@author Sharaf Qeshta
"""


def calculate_insurance(replacement_cost):
    return replacement_cost * 0.8


replacement_cost = float(input("enter the replacement cost of a building"))
print(f"you should buy an insurance that at least cost you ${calculate_insurance(replacement_cost)}")
