#!/usr/bin/python3
"""This module writes a class Student"""


class Student:
    """Represents a class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes student with instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the instance"""
        result = {}
        if isinstance(attrs, list):
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__.copy()
