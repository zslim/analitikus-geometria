def is_matrix(matrix):
    first_row_length = len(matrix[0])
    for i in range(1, len(matrix)):
        if len(matrix[i]) != first_row_length:
            return False
    return True


def dim(matrix):
    if not is_matrix(matrix):
        raise ValueError("Argument is not a matrix")
    rows = len(matrix)
    columns = len(matrix[0])
    return (rows, columns)


def are_dimensions_compatible(matrix_a, matrix_b):
    rows_a, columns_a = dim(matrix_a)
    rows_b, columns_b = dim(matrix_b)
    return columns_a == rows_b


def multiply(matrix_a, matrix_b):
    if not are_dimensions_compatible(matrix_a, matrix_b):
        raise ValueError("Matrices are not compatible")
    result = []
    rows_a, columns_a = dim(matrix_a)
    rows_b, columns_b = dim(matrix_b)
    for i in range(rows_a):
        result_row = []
        for z in range(columns_b):
            result_element = 0
            for j in range(columns_a):
                result_element += matrix_a[i][j] * matrix_b[j][z]
            result_row.append(result_element)
        result.append(result_row)
    return result


def transpose(matrix):
    if not is_matrix(matrix):
        raise ValueError("Argument is not a matrix")
    result = []
    for j in range(len(matrix[0])):
        result_row = []
        for i in range(len(matrix)):
            result_row.append(matrix[i][j])
        result.append(result_row)
    return result
