"""
10.Ingredient Adjuster
A cookie recipe calls for the following ingredients:
• 1.5 cups of sugar
• 1 cup of butter
• 2.75 cups of flour
The recipe produces 48 cookies with this amount of the ingredients. Write a program that
asks the user how many cookies he or she wants to make, then displays the number of cups
of each ingredient needed for the specified number of cookies.

@author Sharaf Qeshta
"""

sugar_for_one_cookie = 1.5 / 48
butter_for_one_cookie = 1 / 48
flour_for_one_cookie = 2.75 / 48

amount_of_cookies = int(input("enter the number of cookies you want:"))
print(format(sugar_for_one_cookie * amount_of_cookies, "0.2f"), "cups of sugar")
print(format(butter_for_one_cookie * amount_of_cookies, "0.2f"), "cups of butter")
print(format(flour_for_one_cookie * amount_of_cookies, "0.2f"), "cups of flour")
