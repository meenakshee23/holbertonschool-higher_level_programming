#!/usr/bin/python3
"""This module defines an empty class BaseGeometry"""


class BaseGeometry:
    """Represents an empty class BaseGeometry"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Gives  a validate value"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """The Rectangle class is defined by its width and height"""

    def __init__(self, width, height):
        """Initializes the width and height"""
        self.integer_validator("width", width)  
        self.integer_validator("height", height)
        self._width = width
        self._height = height

print(dir(Rectangle))
