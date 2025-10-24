#!/usr/bin/python3
from abc import ABC, abstractmethod

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
