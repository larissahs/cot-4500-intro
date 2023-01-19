# imported libraries
import numpy as np

def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print("%d" % elem ,end=' ')
        print('\n')

if __name__ == "__main__":

    # initialize 3x3 matrix with zeroes 
    matrix = np.zeros((3, 3))

    # print matrix initialized to zeros
    print("matrix initialized to zeros\n")
    print_matrix(matrix)

    # step through rows
    # step through columns
    # if row == column set cell to 1, otherwise keep 0
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[0]):
            if row == col:
                matrix[row][col] = 1

    # print first matrix
    print("first matrix\n")
    print_matrix(matrix)

    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[0]):
            if row != col:
                matrix[row][col] = matrix[row][col] + 3
    
    print("second matrix\n")
    print_matrix(matrix)
    
    print("third matrix\n")
    del_col_matrix = np.delete(matrix, 2, 1)
    print_matrix(del_col_matrix)
    

    





    

