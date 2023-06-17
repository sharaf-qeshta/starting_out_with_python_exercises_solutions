"""
18. Restaurant Selector
You have a group of friends coming to visit for your high school reunion, and you want
to take them out to eat at a local restaurant. You aren’t sure if any of them have dietary
restrictions, but your restaurant choices are as follows:
Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
Write a program that asks whether any members of your party are vegetarian, vegan, or
gluten-free, to which then displays only the restaurants to which you may take the group.
Here is an example of the program’s output:
Is anyone in your party a vegetarian? yes Enter
Is anyone in your party a vegan? no Enter
Is anyone in your party gluten-free? yes Enter
Here are your restaurant choices:
 Main Street Pizza Company
 Corner Cafe
 The Chef's Kitchen
Here is another example of the program’s output:
Is anyone in your party a vegetarian? yes Enter
Is anyone in your party a vegan? yes Enter
Is anyone in your party gluten-free? yes Enter
Here are your restaurant choices:
 Corner Cafe
 The Chef's Kitchen


@author Sharaf Qeshta
"""

exclude_JGB = False
exclude_MSPC = False
exclude_CC = False
exclude_MFI = False
exclude_CK = False

vegetarian = input("Is anyone in your party a vegetarian?")
if vegetarian == "yes":
    exclude_JGB = True
vegan = input("Is anyone in your party a vegan?")
if vegan == "yes":
    exclude_JGB = True
    exclude_MSPC = True
    exclude_MFI = True
gluten_free = input("Is anyone in your party gluten-free?")
if gluten_free == "yes":
    exclude_JGB = True
    exclude_MFI = True

print("Here are your restaurant choices:")
if not exclude_JGB:
    print("\tJoe’s Gourmet Burgers")
if not exclude_MSPC:
    print("\tMain Street Pizza Company")
if not exclude_CC:
    print("\tCorner Café")
if not exclude_MFI:
    print("\tMama’s Fine Italian")
if not exclude_CK:
    print("\tThe Chef’s Kitchen")