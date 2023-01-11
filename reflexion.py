import math

import matrix_ops


def householder_matrix(normal_vector_row):
    n = len(normal_vector_row[0])
    identity_n = matrix_ops.identity_matrix(n)
    normal_vector_column = matrix_ops.transpose(normal_vector_row)
    normal_vector_matrix = matrix_ops.multiply(normal_vector_column, normal_vector_row)
    normal_vector_norm = matrix_ops.vector_norm(normal_vector_row)
    scalar_multiplier = -2 / math.pow(normal_vector_norm, 2)
    householder = matrix_ops.add(identity_n,
                                 matrix_ops.multiply_with_scalar(normal_vector_matrix, scalar_multiplier))
    return householder


def reflect_on_hyperplane_origin(normal_vector, point_as_column):
    householder = householder_matrix(normal_vector)
    return matrix_ops.multiply(householder, point_as_column)
