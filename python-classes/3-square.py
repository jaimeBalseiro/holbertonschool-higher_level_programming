#!/usr/bin/python3
"""Create a class named Square"""


class Square:
    """
    Created the class named Square that defines a square

    Args: size (int): The class is represented by an int size
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the square's area"""
        return self.__size ** 2
