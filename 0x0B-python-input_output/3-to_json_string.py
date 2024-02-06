#!/usr/bin/python3
'''
to_json_string function
'''
import json


def to_json_string(my_obj):
    '''
    function that returns the JSON representation of an object (string)

    Args:
        my_obj: object

    Returns: JSON representation of my_obj
    '''
    return json.dumps(my_obj)
