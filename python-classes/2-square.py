#!/usr/bin/python3
"""Create a class named Square"""


class Square:
    """
    The class is created and named Square

    Args:
    size (int): The square is represented by an int size
    """
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
