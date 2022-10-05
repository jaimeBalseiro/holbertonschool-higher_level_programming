#!/usr/bin/python3
"""Create a class named Square"""


class Square:
    """
    Created the class named Square

    Args: size (int): The class represents the size of int
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        size = self.size
        if size == 0:
            print("")
        else:
            for row in range(size):
                for item in range(size):
                    print("#", end="")
                print("")
