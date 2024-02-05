#!/usr/bin/python3
'''class BaseGeometry'''


class BaseGeometry:
    '''
    BaseGeometry class with instance methods area()
    and integer_validator()
    '''

    def area(self):
        '''
        public instance method that raises an exception
        '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        public instance method that validates value

        Args:
            name: name
            value: value

        Raises
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        '''

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
