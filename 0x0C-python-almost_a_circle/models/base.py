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
