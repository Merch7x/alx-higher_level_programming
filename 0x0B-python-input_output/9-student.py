#!/usr/bin/python3
""" Class creation to work with json"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Instanciate a student object

        Args:
            first_name (str) - first name of student
            last_name (str) - last_name of student
            age (int) - age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict represenation of a student"""
        return self.__dict__
