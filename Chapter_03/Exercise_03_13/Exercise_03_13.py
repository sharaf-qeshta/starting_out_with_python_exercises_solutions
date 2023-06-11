"""
13. Shipping Charges
The Fast Freight Shipping Company charges the following rates:
Weight of Package Rate per Pound
2 pounds or less $1.50
Over 2 pounds but not more than 6 pounds $3.00
Over 6 pounds but not more than 10 pounds $4.00
Over 10 pounds $4.75
Write a program that asks the user to enter the weight of a
package then displays the shipping charges.

@author Sharaf Qeshta
"""

weight_of_package = float(input("enter the weight of a package:"))

if weight_of_package < 2:
    print("you are charged $1.5")
elif weight_of_package < 6:
    print("you are charged $3.0")
elif weight_of_package < 10:
    print("you are charged $4.0")
else:
    print("you are charged $4.75")