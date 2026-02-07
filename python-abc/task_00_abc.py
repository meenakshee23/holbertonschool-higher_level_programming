#!/usr/bin/env python3
"""
This module defines an abstract Animal class and two subclasses: Dog and Cat.
"""

from abc import ABC, abstractmethod



class Animal(ABC):
    """Represents an abstract class named Animal"""


    @abstractmethod
    def sound(self):
        """
        Implement the sound method in each subclass to
        return the strings “Bark” and “Meow"
        """
        pass


class Dog(Animal):
    """Inherits from the Animal class"""

    def sound(self):
        """return the string “Bark”"""
        return "Bark"


class Cat(Animal):
    """Inherits from the Animal class"""

    def sound(self):
        """return the string “Meow”"""
        return "Meow"
