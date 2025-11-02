#!/usr/bin/python3
"""This module writes a class Student that defines a student"""
StudentBase = __import__('9-student').Student


class Student(StudentBase):
    """Defines a student"""
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__.copy()
        
        filtered_dict = {}
        for key in attrs:
            if key in self.__dict__:
                filtered_dict[key] = self.__dict__[key]
        return filtered_dict
