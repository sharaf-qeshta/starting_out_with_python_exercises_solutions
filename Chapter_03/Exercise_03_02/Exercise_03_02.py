"""
2. Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks
for the length and width of two rectangles. The program should tell the user
which rectangle has the greater area, or if the areas are the same.

@author Sharaf Qeshta
"""

rect1_width = float(input("enter rectangle 1 width:"))
rect1_length = float(input("enter rectangle 1 length:"))
rect2_width = float(input("enter rectangle 2 width:"))
rect2_length = float(input("enter rectangle 2 length:"))

rect1_area = rect1_width * rect1_length
rect2_area = rect2_width * rect2_length

if rect1_area < rect2_area:
    print("Rectangle 2 has a greater area")
elif rect1_area > rect2_area:
    print("Rectangle 1 has a greater area")
else:
    print("both rectangles have the same area")