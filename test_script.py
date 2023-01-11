import pytest

import matrix_ops


@pytest.mark.parametrize(["matrix", "expected"], [
    ([[1, 2], [0, 3]], True), ([[1, 2], [0]], False)
])
def test_is_matrix(matrix, expected):
    actual = matrix_ops.is_matrix(matrix)
    assert actual == expected


@pytest.mark.parametrize(["matrix", "expected"], [
    ([[1, 2], [0, 3], [6, 8]], (3, 2)),
    ([[3, 6, 2]], (1, 3)),
])
def test_dim(matrix, expected):
    actual = matrix_ops.dim(matrix)
    assert actual == expected


@pytest.mark.parametrize(["matrix"], [
    ([[0, 1], [3, 7, 9]],),
    ([[2, 5], [1, 0], [7]],)
])
def test_dim_error(matrix):
    with pytest.raises(ValueError):
        matrix_ops.dim(matrix)


@pytest.mark.parametrize(["matrix_a", "matrix_b", "expected"], [
    ([[1, 2]], [[3, 6, 4], [5, -1, 0]], True),
    ([[2, 4, 5], [1, -1, 0]], [[1], [2], [3]], True),
    ([[1, 2], [6, -1], [8, -13]], [[2, 3], [4, -6], [1, 3]], False)
])
def test_are_dimensions_compatible(matrix_a, matrix_b, expected):
    actual = matrix_ops.are_dimensions_compatible(matrix_a, matrix_b)
    assert actual == expected
