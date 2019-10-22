#!/usr/bin/python3
"""Base class
"""
import json


class Base:
    """
    class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Called when a new instance of this class is created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a given list of dictionaries to a json string.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a json formatted file.
        """
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
                return
            new = "["
            for x in list_objs:
                new += (cls.to_json_string(cls.to_dictionary(x)))
            new += "]"
            f.write(new.replace('}{', '}, {'))

    @classmethod
    def reset(cls):
        cls.__nb_objects = 0
