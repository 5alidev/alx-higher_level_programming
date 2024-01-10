#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""
    square = []
    for x in matrix:
        row = map(lambda n: n ** 2, x)
        square.append(list(row))
    return square
