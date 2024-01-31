#!/usr/bin/python3
def matrix_divided(matrix, div):
    '''
    divides all elements of a matrix.
    '''

    rowLength = None
    excepMsg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(excepMsg)
    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(excepMsg)
        for column in row:
            if not isinstance(column, int) and not isinstance(column, float):
                raise TypeError(excepMsg)
        if rowLength is None:
            rowLength = len(row)
        elif rowLength != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    newMatrix = [[round(column / div, 2) for column in row] for row in matrix]
    return newMatrix
