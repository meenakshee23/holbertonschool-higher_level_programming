#!/usr/bin/python3
"""This module writes a Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initializes a Square instance
        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """Return the square description"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
