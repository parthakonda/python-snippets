# Fibonocci program

"""
Example:
fibonocci of 10 is

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
"""


def fibnocci(given_range):
    # Initial values
    x = 0
    y = 1

    for item in range(given_range):
        print(x)
        temp = x
        x = y
        y = temp + x


def fibnocci_optimized(given_range):
    x, y = 0, 1
    for _ in range(given_range):
        print(x)
        x, y = y, x+y


fibnocci(10)
fibnocci_optimized(10)
