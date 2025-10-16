#!/usr/bin/python3
"""This module defines a class Square with a size attribute"""


class Square:
    """Represents a square defined by its size"""
    def __init__(self, size=0):
        """Initializes the square with a private size attribute"""

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
              
              if not isinstance(size, int):
                  raise TypeError("size must be an integer")
              if size < 0:
                  raise ValueError("size must be >= 0")

              self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
