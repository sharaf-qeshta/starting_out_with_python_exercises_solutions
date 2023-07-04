"""
6. Miles to Kilometers Table
Write a program that displays a table of distances in miles and their equivalent distances in
kilometers, rounded to 2 decimal places. One mile is equivalent to 1.60934 kilometers. The
table should be generated using a loop, and should include values in 10 mile increments from
10 to 80.

@author Sharaf Keshta
"""

print("Miles\t\tKilometers")
for i in range(8):
    miles = (i+1) * 10
    print(f"{miles}\t\t\t{format(miles * 1.60934, '.2f')}")
