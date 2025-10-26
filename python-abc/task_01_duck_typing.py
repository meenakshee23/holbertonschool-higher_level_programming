#!/usr/bin/python3
"""This module defines abstract base class, Shape, and concrete implementations"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape"""
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """Initializes a circle with the radius"""
        self.radius = radius

    def area(self):
        """Return the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Defines the rectangle"""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print the area and perimeter of the shape passed to the function"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
