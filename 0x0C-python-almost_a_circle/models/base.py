#!/usr/bin/python3
'''
module containing Base Class
'''
import json


class Base:
    '''
    class Base with private class attribute and a class constructor

    Attributes:
        __nb_objects: number of instances created by Base class
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Base class constructor

        Args:
            id: integer
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returns the JSON string representation
        '''

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation of list_objs to a file
        '''

        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_dicts)
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''
        returns the list of the JSON string representation json_string
        '''

        if json_string is None or len(json_string) <= 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes already set
        '''

        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == 'Rectangle':
            dummy = Rectangle(1, 1)
        elif cls.__name__ == 'Square':
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        returns a list of instances
        '''

        from os import path
        filename = "{}.json".format(cls.__name__)
        if not path.isfile(filename):
            return []
        with open(filename, 'r') as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
