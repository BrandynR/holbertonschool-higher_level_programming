#!/usr/bin/python3
"""
matrix_divided:
Function to divide the contents a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Matrix must be a list of integers or floats
    Else a TypeError will raise
    Each row must be the same size
    Else a TypeError will raise
    Div must be a number, otherwise
    Else a TypeError will raise
    Div can't be zero
    Else ZeroDivisionError
    All elements will be divided by div and rounded to 2 decimal places
    Returns a new matrix
    """
    newmatrix = []
    length = 0

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if matrix == [] or matrix == [[]]:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    if len(matrix[0]) <= 0:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')
    for row in matrix:
        newrow = []
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        if length is 0:
            length = len(row)
        elif len(row) is not length:
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')
            if div is True or div is False:
                        raise TypeError("div must be a number")
            newrow.append(round(item / div, 2))
        newmatrix.append(newrow)
    return newmatrix
