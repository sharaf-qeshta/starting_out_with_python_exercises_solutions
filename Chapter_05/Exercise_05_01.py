"""
1. Kilometer Converter
Write a program that asks the user to enter a distance in kilometers, then converts that
distance to miles. The conversion formula is as follows:
Miles 5 Kilometers 3 0.6214

@author Sharaf Qeshta
"""


def convert_to_miles(kilometers):
    print(f"{kilometers} Kilometers = {kilometers * 0.6214} Miles")


kilometers = int(input("enter a kilometer distance to covert it to miles:"))
convert_to_miles(kilometers)
