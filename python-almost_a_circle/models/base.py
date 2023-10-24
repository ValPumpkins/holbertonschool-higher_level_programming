#!/usr/bin/python3
""" Defines a base model class """

import json


class Base:
    """ Represent the base model for this project
    Attributes:
        __nb_objects (int): number of instantiated Bases
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a new Base
        Args:
            id (int): identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string rep of a list dict
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save a list of objects to a file
        Args:
            list_objs (list): a list of objects
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            objects = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(objects)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ Return the JSON string rep of a list dict
        Args:
            json_string (str): a JSON string
        Returns:
            JSON string representation of list_dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
