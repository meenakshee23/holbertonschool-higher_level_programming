#!/usr/bin/python3
"""This module defines a class Square with a size attribute"""


class Square:
    """Represents a square defined by its size"""
    def __init__(self, size=0):
        """Initializes the square with a private size attribute"""
        self.size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.size * self.size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
