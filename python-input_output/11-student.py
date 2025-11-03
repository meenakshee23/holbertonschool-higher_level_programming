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
        if isinstance(attrs, list):
            new_dict = {}
            for a in attrs:
                if isinstance(a) == str and hasattr(self, a):
                    new_dict[a] = getattr(self, a)
                    return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance"""
        for key in json:
            self.__dict__[key] = json[key]
