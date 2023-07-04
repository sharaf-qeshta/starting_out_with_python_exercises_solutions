"""
9. Ocean Levels
Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
application that displays the number of millimeters that the ocean will have risen each year
for the next 25 years.


@author Sharaf Qeshta
"""

RISING_FACTOR = 1.6

print("Year\t\tRising")
for i in range(25):
    print(f"{i+1}\t\t\t{format((i+1) * RISING_FACTOR, '.2f')}")