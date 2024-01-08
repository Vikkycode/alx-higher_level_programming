#!/usr/bin/python3
# 4-print_square.py

"""define a print square function """

def print_square(size):
    """ print square 

    Arg:
        size (int) : size to print
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
