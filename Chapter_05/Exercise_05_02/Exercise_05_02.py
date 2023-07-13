"""
2. String Repeater
Python allows you to repeat a string by multiplying it by an integer, e.g. 'Hi' * 3 will give
'HiHiHi'. Pretend that this feature does not exist, and instead write a function named
repeat that accepts a string and an integer as arguments. The function should return a
string of the original string repeated the specified number of times, e.g. repeat('Hi', 3)
should return 'HiHiHi'.

@author Sharaf Qeshta
"""


def repeat(word, times):
    returned = ""
    for i in range(times):
        returned += word
    return returned


print(repeat("Hi", 3))
