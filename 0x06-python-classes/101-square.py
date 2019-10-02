#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Square init, with position """

        self.size = size
        self.position = position

    def __repr__(self):

        if self.__size == 0:
            return("")
        return(("\n" * self.__position[1]) +
               ("\n".join((" " * self.__position[0]) +
                          "#" * self.__size for i in range(self.__size))))

    @property
    def size(self):
        """Getter for the size of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for setting sqwar size"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position of your square"""

        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter for square position"""

        if (type(value) != tuple or len(value) != 2 or
            type(value[0]) != int or type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of square"""

        return (self.__size ** 2)

    def my_print(self):
        """Prints the square including postion"""

        if (self.__size == 0):
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join((" " * self.__position[0]) + "#" * self.__size
                            for i in range(self.__size)))
