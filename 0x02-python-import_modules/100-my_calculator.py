#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv as args
if __name__ == "__main__":
    if len(args) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(args[1])
        b = int(args[3])
        op = args[2]
        if op == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif op == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif op == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif op == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
