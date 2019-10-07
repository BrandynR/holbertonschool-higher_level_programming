#!/usr/bin/python3
"""
Defines an empty class, Rectangle
"""


def errorChecks(value, name):
    """
    Error check function
    """
    if not isinstance(value, int):
        raise TypeError(name + " must be an integer")
    if value < 0:
        raise ValueError(name + " must be >= 0")


class Rectangle:
    """
    Class Rectangle
    """
    def __init__(self, width=0, height=0):
        errorChecks(width, "width")
        errorChecks(height, "height")
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        errorChecks(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        errorChecks(value, "height")
        self.__height = value

    def area(self):
        """
        returns the area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
