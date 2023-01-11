import pytest

import reflexion


def matrix_approx(matrix):
    return [pytest.approx(row) for row in matrix]


@pytest.mark.parametrize(["normal_vector_row", "expected"], [
    ([[2, 1]], [[-0.6, -0.8], [-0.8, 0.6]]),
    ([[1, 1, 1]], [[1/3, -2/3, -2/3], [-2/3, 1/3, -2/3], [-2/3, -2/3, 1/3]])
])
def test_householder_matrix(normal_vector_row, expected):
    actual = reflexion.householder_matrix(normal_vector_row)
    assert matrix_approx(actual) == expected


@pytest.mark.parametrize(["normal_vector", "point_as_column", "expected"], [
    ([[2, 1]], [[1], [-3]], [[1.8], [-2.6]]),
    ([[1, 1, 1]], [[3], [4], [0]], [[-5/3], [-2/3], [-14/3]])
])
def test_reflect_on_hyperplane_origin(normal_vector, point_as_column, expected):
    actual = reflexion.reflect_on_hyperplane_origin(normal_vector, point_as_column)
    assert matrix_approx(actual) == expected
