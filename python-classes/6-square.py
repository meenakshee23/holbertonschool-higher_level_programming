#!/usr/bin/python3
"""This module defines a class Square with a size attribute"""


class Square:
    """Represents a square defined by its size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size and position"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.size * self.size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.size):
                print(' ' * self.__position[0] + '#' * self.size)
