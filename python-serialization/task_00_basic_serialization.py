#!/usr/bin/env python3
"""
This module creates a basic serialization module that adds the functionality
to serialize a Python dictionary to a JSON
file and deserialize the JSON file to recreate the Python Dictionary
"""

import json


def serialize_and_save_to_file(data, filename):
   """Serialize and save data to the specified file"""
   with open(filename, "w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """load and deserialize data from the specified file"""
    with open(filename, "r") as file:
        return json.load(file)
