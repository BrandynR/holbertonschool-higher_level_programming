#!/usr/bin/python3
"""Base class"""
import json
import csv


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string of dictionary list"""
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

@staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws"""
        window = turtle.Screen()
        window.title("Turtle Square")
        tT = turtle.Turtle()
        for cls in list_rectangles + list_squares:
            tT.up()
            tT.setpos(cls.x, cls.y)
            tT.down()
            tT.setheading(0)
            tT.forward(cls.width)
            tT.right(90)
            tT.forward(cls.height)
            tT.right(90)
            tT.forward(cls.width)
            tT.right(90)
            tT.forward(cls.height)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation to file """
        LO_dict = []
        if list_objs is not None:
            LO_dict = [x.to_dictionary() for x in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(LO_dict))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV and saves to file"""
        filename = (list_objs[0].__class__.__name__) + ".csv"
        new = []
        for x in list_objs:
            new.append(x.to_dictionary())
        keys = new[0].keys()
        print(type(keys))
        with open(filename, "w") as csv_file:
            writer = csv.DictWriter(csv_file, keys)
            writer.writeheader()
            writer.writerows(new)

    @classmethod
    def load_from_file(cls):
        """returns list of instances from JSON file"""
        filename = (cls.__name__) + ".json"
        new = []
        try:
            with open(filename) as f:
                data = f.read()
                convert = cls.from_json_string(data)
                for x in convert:
                    new.append(cls.create(**x))
                f.close()
                return new
        except:
            return new

    @classmethod
    def load_from_file_csv(cls):
        """returns list of instances from CSV file"""
        name = cls.__name__
        filename = (cls.__name__) + ".csv"
        new = []
        try:
            with open(filename) as f:
                reader = csv.reader(f)
                for row in reader:
                    pass
        except:
            return new

    @staticmethod
    def from_json_string(json_string):
        """returns JSON string representation"""
        if json_string is None:
            return []

        j = json.loads(json_string)
        return j

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new
