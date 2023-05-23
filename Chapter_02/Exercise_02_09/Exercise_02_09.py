"""
9. Circle Measurements
Write a program that asks the user to enter the radius of a circle.
The program should calculate and display the area and circumference of the circle using πr2
for the area and 2πr
for the circumference.
Hint: You can either use 3.14159 as the value of pi (π), or add the statement "import math"
to the start of the program and then use "math.pi" wherever you need the value of pi in
the program.

@author Sharaf Qeshta
"""

PI = 3.14159
radius = float(input("Enter the radius of the circle:"))
print("Circle Area :", format(radius * radius * PI, "0.2f"))
print("Circle Circumference :", format(2 * PI * radius, "0.2f"))