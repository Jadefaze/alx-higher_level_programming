#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """ print list of lists (matrix)

    Args:
        matrix: the list of list

    Returns:
        nothing
    """

    i = 0

    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]), end='')
            else:
                print("{:d}".format(matrix[i][j]), end=' ')
            j += 1
        print()
        i += 1
