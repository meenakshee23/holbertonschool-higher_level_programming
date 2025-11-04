#!/usr/bin/python3
"""This module shows how to serialize and deseralizee custom Python objects"""
import pickle


class CustomObject:
    """Represents a CustomObject class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out attributes of the object with the following format"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance of the object and save it"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """load and return an instance of the CustomObject"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
