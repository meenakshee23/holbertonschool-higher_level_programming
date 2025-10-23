#!/usr/bin/python3
"""This module writes a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square class"""

    def __init__(self, size):
        """Initializes the size of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """The area of the square"""
        return self.__size ** 2

    def __str__(self):
        """The String representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
