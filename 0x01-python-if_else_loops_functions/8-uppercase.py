#!/usr/bin/python3
# Author - Benhamou Khalid

def uppercase(str):
    """function that prints a string in uppercase followed by a new line."""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
