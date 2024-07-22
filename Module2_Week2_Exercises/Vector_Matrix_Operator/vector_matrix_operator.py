import numpy as np


# Length of vector
def compute_vector_length(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector


# Dot product of two vectors
def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


# Product of matrix and vector
def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


# Product of two matrices
def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


# Inverse of matrix
def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result


def main():

    m1 = np.array([[0, 1, 2],
                   [2, -3, 1]])
    m2 = np.array([[1, -3],
                   [6, 1],
                   [0, -1]])
    result = matrix_multi_matrix(m1, m2)
    print(result)


if __name__ == "__main__":
    main()
