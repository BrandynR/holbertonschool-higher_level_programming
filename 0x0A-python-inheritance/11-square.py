#!/usr/bin/python3
"""Class"""


class BaseGeometry():
    """Class"""
    def area(self):
        """Calculates the area of obj. Not implemented."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates 'value' and raises exceptions for fun."""
        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of rectangle."""
        return self.__height * self.__width

    def __str__(self):
        """Return a different thing"""
        return "[{}] {:d}/{:d}".format(type(self).__name__,
                                       self.__width, self.__height)


class Square(Rectangle):
    """Class square"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
