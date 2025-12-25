#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
The result is returned as a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Returns a new matrix with values rounded to 2 decimals.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    
    row_lengths = [len(row) for row in matrix if isinstance(row, list)]
    if len(row_lengths) != len(matrix) or len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    row_length = None

    for row in matrix:
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
