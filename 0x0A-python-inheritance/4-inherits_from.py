#!/usr/bin/python3
'''inherits_from() function'''


def inherits_from(obj, a_class):
    '''
    check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: object
        a_class: class

    Returns: True or False
    '''

    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
