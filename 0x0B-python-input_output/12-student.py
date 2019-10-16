#!/usr/bin/python3
"""Class for Student"""


class Student():
    """Class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns __dict__ of object."""
        x = self.__dict__
        if attrs is None:
            return self.__dict__
        if not type(attrs) is list:
            return self.__dict__
        for i in attrs:
            if not type(i) is str:
                return self.__dict__
        z = {}
        for k, v in x.items():
            if k in attrs:
                z.update({k: v})
        return z
