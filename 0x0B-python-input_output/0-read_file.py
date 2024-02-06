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
    f = open(filename, 'r')
    for line in f:
        print(line, end='')
