#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        for num in row:
            new_matrix.append(num ** 2)
    return new_matrix
