"""
5. Property Tax
A county collects property taxes on the assessment value of property, which is 60 percent of
the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment
 value is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the
actual value of a piece of property and displays the assessment value and property tax.

@author Sharaf Qeshta
"""


actual_price = int(input("enter the actual price of the property:"))
assessment_value = actual_price * 0.6
property_tax = assessment_value * 0.0072

print(f"Assessment Value is ${assessment_value}")
print(f"Property Tax is ${property_tax}")