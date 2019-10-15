#!/usr/bin/python3
"""Class"""


class BaseGeometry:
    """Class"""
    def area(self):
        """Calculates the area of obj"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates 'value' and raises exceptions"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
