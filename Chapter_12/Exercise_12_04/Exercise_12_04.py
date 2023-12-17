"""
4. Largest List Item
Design a function that accepts a list as an argument and returns the largest value in the list.
The function should use recursion to find the largest item.


@author Sharaf Qeshta
"""


def find_largest_item(list_of_items, current, largest):
    if current == -1:
        print(list_of_items[largest])
        return
    if list_of_items[current] > list_of_items[largest]:
        find_largest_item(list_of_items, current - 1, current)
    else:
        find_largest_item(list_of_items, current - 1, largest)


def main():
    items = [45, 1, 7, 9, 6, 102, -5, -1, 0, 99]
    find_largest_item(items, len(items) - 1, 0)


main()
