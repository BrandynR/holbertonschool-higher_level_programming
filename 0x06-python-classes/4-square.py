#!/usr/bin/python3
def errorCheck(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")


class Square:

    def __init__(self, size=0):
        self.__size = size
        errorCheck(size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        errorCheck(value)
        self.__size = value

    def area(self):
        return self.__size ** 2
