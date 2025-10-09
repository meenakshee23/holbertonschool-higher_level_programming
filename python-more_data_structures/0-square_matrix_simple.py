#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        square_matrix_simple = []
        for num in row:
            square_matrix_simple.append(num ** 2)
            new_matrix.append(square_matrix_simple)

            return new_matrix
