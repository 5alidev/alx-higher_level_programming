#!/usr/bin/python3
'''
add_attribute() function
'''


def add_attribute(object, name, value):
    '''
    function that adds a new attribute to an object if it’s possible

    Args:
        object: object where to add the attribute
        name: attribute name
        value: attribute value

    Raises:
        TypeError: if the object can’t have new attribute
    '''

    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
