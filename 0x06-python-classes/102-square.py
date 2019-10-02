#!/usr/bin/python3
"""
Square Module - for all your needs, as long as they include printing squares!
"""


class Square:
    """
    Square class now has cool setters and getters for the size!
    """
    def __init__(self, size=0):
        """
        Square class init! Takes in a size.
        """
        self.size = size

    @property
    def size(self):
        """
        Size getter, returns the private size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Size setter, sets the size.
        """
        self.__check_size__(value)
        self.__size = value

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __lt__(self, other):
        return self.size < other.size

    def __gt__(self, other):
        return self.size > other.size

    def __le__(self, other):
        return self.size <= other.size

    def __ge__(self, other):
        return self.size >= other.size

    def area(self):
        """
        Returns the area of the square.
        """
        return (self.__size ** 2)

    def __check_size__(self, size):
        """
        Size checking for squares!
        """
        if type(size) != int and type(size) != float:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
