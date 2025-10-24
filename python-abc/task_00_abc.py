#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Abstract Base Classes (ABCs) ensure that derived classes implement specific methods"""

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Implement the sound method in each subclass"""
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
