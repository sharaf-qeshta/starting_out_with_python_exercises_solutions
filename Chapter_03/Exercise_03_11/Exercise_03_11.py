"""
11. Book Club Points
Serendipity Booksellers has a book club that awards points to its customers based on the
number of books purchased each month. The points are awarded as follows:
•	 If a customer purchases 0 books, he or she earns 0 points.
•	 If a customer purchases 2 books, he or she earns 5 points.
•	 If a customer purchases 4 books, he or she earns 15 points.
•	 If a customer purchases 6 books, he or she earns 30 points.
•	 If a customer purchases 8 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she has
 purchased this month, then displays the number of points awarded


@author Sharaf Qeshta
"""

books_purchased = int(input("enter the number of books purchased: "))

if books_purchased < 2:
    print("your points is 0")
elif books_purchased < 4:
    print("your points is 5")
elif books_purchased < 6:
    print("your points is 15")
elif books_purchased < 8:
    print("your points is 30")
else:
    print("your points is 60")