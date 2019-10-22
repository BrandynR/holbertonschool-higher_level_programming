#!/usr/bin/python3
"""Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square inherits from class Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Called when a new instance of this class is created.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloads normal str.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates attributes values using a list or dictionary.
        """
        atts = ["id", "size", "x", "y"]
        [setattr(self, a, b) for a, b in zip(atts, args)]
        [setattr(self, a, b) for a, b in kwargs.items()]

    @property
    def size(self):
        """size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """size setter
        """
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Creats a dictionary of an object
        """
        hold = {}
        for key, val in self.__dict__.items():
            if key.find("__") != -1:
                key = key[key.find("__")+2:]
            if key == "width":
                key = "size"
            elif key == "height":
                continue
            hold[key] = val
        return hold
