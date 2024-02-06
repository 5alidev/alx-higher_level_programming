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

    def to_json(self):
        '''
        retrieves a dictionary representation of a Student instance
        '''

        return vars(self)
