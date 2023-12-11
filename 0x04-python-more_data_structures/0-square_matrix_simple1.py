#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        row_list = []
        for j in range(len(matrix[i])):
            square = matrix[i][j] ** 2
            row_list.append(square)
        new_matrix.append(row_list)
    return new_matrix

