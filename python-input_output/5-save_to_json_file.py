#!/usr/bin/python3
"""This module writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Represents the JSON"""
    with open(filename, 'w') as file:
        json.dump(my_obj, filename)
