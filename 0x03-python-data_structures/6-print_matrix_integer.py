#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    rlen = len(matrix)

    for i in range(rlen):
        clen = len(matrix[i])
        for j in range(clen):
            if j < clen - 1:
                print("{}".format(matrix[i][j]), end=" ")
            else:
                print("{}".format(matrix[i][j]), end="")
        print()
