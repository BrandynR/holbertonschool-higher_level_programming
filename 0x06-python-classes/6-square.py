#!/usr/bin/python3
def errorCheck(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")


def errorCheckTuple(value):
    if not isinstance(value, tuple):
        raise TypeError("position must be a tuple of 2 positive integers")
    if len(value) != 2:
        raise TypeError("position must be a tuple of 2 positive integers")
    if not isinstance(value[0], int) or not isinstance(value[1], int):
        raise TypeError("position must be a tuple of 2 positive integers")
    if value[0] < 0 or value[1] < 0:
        raise TypeError("position must be a tuple of 2 positive integers")


class Square:

    def __init__(self, size=0, position=(0, 0)):
        errorCheck(size)
        errorCheckTuple(position)
        self.__size = size
        self._position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        errorCheck(value)
        self.__size = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        errorCheckTuple(value)
        self._position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if not self.__size:
            print()
            return
        for y in range(self._position[1]):
            print()
        for height in range(self.__size):
            for x in range(self._position[0]):
                print(" ", end="")
            for width in range(self.__size):
                print("#", end="")
            print()
