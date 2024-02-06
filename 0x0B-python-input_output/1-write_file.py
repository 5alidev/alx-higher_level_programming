#!/usr/bin/python3
'''
write_file function
'''


def write_file(filename="", text=""):
    '''
    function that writes a string to a text file

    Args:
        filename: name of the file
        text: text to write
    Returns:
        number of characters written
    '''
    with open(filename, 'w') as f:
        return f.write(text)
