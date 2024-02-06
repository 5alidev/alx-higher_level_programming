#!/usr/bin/python3
'''
class Student
'''


class Student:
    '''
    Student class with 3 public instance attributes
    and a public method
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Student Constructor

        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of student
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        retrieves a dictionary representation of a Student instance
        '''

        if attrs is None:
            return vars(self)
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary

    def reload_from_json(self, json):
        '''
        replaces all attributes of the Students instance
        '''

        for key, value in json.items():
            setattr(self, key, value)
