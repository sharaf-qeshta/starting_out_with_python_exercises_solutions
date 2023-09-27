"""
11. Lo Shu Magic Square
The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-18. The
Lo Shu Magic Square has the following properties:
•	 The grid contains the numbers 1 through 9 exactly.
•	 The sum of each row, each column, and each diagonal all add up to the same number.
This is shown in Figure 7-19.
In a program you can simulate a magic square using a two-dimensional list.
Write a function that accepts a two-dimensional list as an argument and
 determines whether the list is
a Lo Shu Magic Square. Test the function in a program.



@author Sharaf Qeshta
"""


def is_lo_shu_magic_square(two_dimensional_list):
    first_diagonal_sum = two_dimensional_list[0][0] + \
        two_dimensional_list[1][1] + two_dimensional_list[2][2]
    second_diagonal_sum = two_dimensional_list[0][2] + \
        two_dimensional_list[1][1] + two_dimensional_list[2][0]
    if first_diagonal_sum != second_diagonal_sum:
        return False

    for i in range(3):
        row_sum = 0
        column_sum = 0
        for j in range(3):
            row_sum += two_dimensional_list[i][j]
            column_sum += two_dimensional_list[j][i]
        if row_sum != first_diagonal_sum:
            return False
        if column_sum != first_diagonal_sum:
            return False

    return True


array = [[4, 9, 2],
         [3, 5, 7],
         [8, 1, 6]]
print(is_lo_shu_magic_square(array))
