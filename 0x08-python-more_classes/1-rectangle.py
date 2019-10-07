#!/usr/bin/python3
"""
Defines an empty class, Rectangle
"""


def errorChecks(value, name):
    """
    Error check function for rectangles
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
