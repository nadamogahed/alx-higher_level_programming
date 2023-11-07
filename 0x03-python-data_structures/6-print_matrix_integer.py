#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        print()
    else:
        for row in matrix:
            for num in row:
                print(num, end=' ')
            print()
