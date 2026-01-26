#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """Represents a class Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for item in value:
            if not isinstance(item, int):
                raise TypeError("position must be a tuple of 2 positive integers")
            if item < 0:
                raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        y = self.__position[1]
        x = self.__position[0]

        while y > 0:
            print()
            y -= 1

        for i in range(self.__size):
            print(" " * x + "#" * self.__size)
