#!/usr/bin/python3
"""Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherits from class Base.
    """
    def errCheck(self, name, value):
        """
        Error checking method that will raise appropriate
        error/message combos.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def __init__(self, width, height, x=0, y=0, id=None):
        """Called when a new instance of this class is created.
        """
        super(Rectangle, self).__init__(id)
        self.errCheck("width", width)
        self.errCheck("height", height)
        self.errCheck("x", x)
        self.errCheck("y", y)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Overloads normal str.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates attributes values using a list or dictionary.
        """
        atts = ["id", "width", "height", "x", "y"]
        [setattr(self, a, b) for a, b in zip(atts, args)]
        [setattr(self, a, b) for a, b in kwargs.items()]

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        """
        self.errCheck("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        """
        self.errCheck("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        """
        self.errCheck("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        """
        self.errCheck("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the class instance.
        """
        return self.width * self.height

    def display(self):
        """Prints a 2D representation of the class instance.
        """
        [print() for a in range(self.y)]
        [print("{}{}".format(
            " " * self.x, "#" * self.width)) for x in range(self.height)]

    def to_dictionary(self):
        """
        Creats a dictionary of an object
        """
        return dict((key[key.find("__")+2:]
                    if key.find("__") != -1 else key, val)
                    for key, val in self.__dict__.items())
