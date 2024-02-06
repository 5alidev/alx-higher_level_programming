#!/usr/bin/python3
'''
class_to_json() function
'''


def class_to_json(obj):
    '''
    JSON serialization of an object

    Args:
        obj: instance of a class

    Returns: JSON
    '''
    return vars(obj)
