"""
5. Recursive List Sum
Design a function that accepts a list of numbers as an argument. The function should recursively
calculate the sum of all the numbers in the list and return that value.

@author Sharaf Qeshta
"""


def recursive_sum(list_of_items, index):
    if index == -1:
        return 0
    return list_of_items[index] + recursive_sum(list_of_items, index - 1)


def main():
    items = [1, 2, 3, 4, 5, 6]
    print(recursive_sum(items, len(items) - 1))


main()
