#!/usr/bin/python3
"""This module Write a class Student"""


class Student:
    """Defines a class Student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__.copy()

        filtered_dict = {}
        for key in attrs:
            if key in self.__dict__:
                filtered_dict[key] = self.__dict__[key]
        return filtered_dict
