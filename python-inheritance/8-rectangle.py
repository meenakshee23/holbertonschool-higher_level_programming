#!/usr/bin/python3
"""This module defines an empty class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The Rectangle class is defined by its width and height"""

    def __init__(self, width, height):
        """Initializes the width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
