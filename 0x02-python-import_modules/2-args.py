#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    inc = 0
    if len(argv) <= 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
        print(f"1: {argv[1]}")
    else:
        print("{:d} arguments:".format(len(argv) - 1))
        for arg in argv[1:]:
            inc += 1
            print(f"{inc}: {arg}")
