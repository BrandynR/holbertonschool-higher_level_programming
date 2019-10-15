#!/usr/bin/python3
"""Class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """init"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of obj"""
        return self.__width * self.__height

    def __str__(self):
        """Returns str"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def print(self):
        """Print"""
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
