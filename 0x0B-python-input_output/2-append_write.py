#!/usr/bin/python3
'''
append_write function
'''


def append_write(filename="", text=""):
    '''
    function that appends a string at the end of a text file

    Args:
        filename: name of the file
        text: text to append to the file

    Returns: number of characters added
    '''
    with open(filename, 'a') as f:
        return f.write(text)
