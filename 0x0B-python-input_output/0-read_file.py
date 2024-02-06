#!/usr/bin/python3
'''
read_file function
'''


def read_file(filename=""):
    '''
    function that reads a text file and prints it to STDOUT

    Args:
        filename: file name
    '''
    with open(filename) as f:
        read_data = f.read()
        print(read_data, end='')
