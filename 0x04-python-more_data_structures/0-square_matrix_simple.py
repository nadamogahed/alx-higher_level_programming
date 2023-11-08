#!/usr/bin/python3
def square(x):
    return x**2
def square_matrix_simple(matrix=[]):
    new_matrix = [row.copy() for row in matrix]  # This creates a copy of the matrix
    for i, row in enumerate(new_matrix):
        new_matrix[i] = list(map(square, row))
    return new_matrix
