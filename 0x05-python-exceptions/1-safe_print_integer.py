#!/usr/bin/python3
def safe_print_integer(value):
    """safe printing of an integer"""
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        return False
