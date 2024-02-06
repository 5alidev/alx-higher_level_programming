#!/usr/bin/python3
'''
load_from_json_file() function
'''
import json


def load_from_json_file(filename):
    '''
    function that creates an Object from a “JSON file”

    Args:
        filename: name of the file
    '''
    with open(filename, 'r') as f:
        return json.loads(f.read())
