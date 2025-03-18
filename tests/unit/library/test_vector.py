import math

import pytest

from astrocompute.library.vector import (
    Vector,
    add,
    are_orthogonal,
    are_parallel,
    are_same_dimension,
    dot_product,
    norm,
    normalize,
    scalar_multiply,
)


@pytest.mark.parametrize(
    "u, v, expected",
    [
        ((1, 2), (3, 4), (4, 6)),
        ((-1, -2), (-3, -4), (-4, -6)),
        ((0, 0), (0, 0), (0, 0)),
        ((1.5, 2.5), (3.5, 4.5), (5.0, 7.0)),
        ((1, 2, 3), (4, 5, 6), (5, 7, 9)),
    ],
)
def test_add(u: Vector, v: Vector, expected: Vector):
    assert add(u, v) == expected


@pytest.mark.parametrize(
    "s, v, expected",
    [
        (2, (1, 2), (2, 4)),
        (-1, (1, 2), (-1, -2)),
        (0, (1, 2), (0, 0)),
        (1.5, (1, 2), (1.5, 3.0)),
        (2, (1, 2, 3), (2, 4, 6)),
    ],
)
def test_scalar_multiply(s: float, v: Vector, expected: Vector):
    assert scalar_multiply(s, v) == expected


@pytest.mark.parametrize(
    "u, v, expected",
    [
        ((1, 2), (3, 4), 11),
        ((-1, -2), (-3, -4), 11),
        ((0, 0), (0, 0), 0),
        ((1.5, 2.5), (3.5, 4.5), 16.5),
        ((1, 2, 3), (4, 5, 6), 32),
    ],
)
def test_dot_product(u: Vector, v: Vector, expected: float):
    assert dot_product(u, v) == expected


@pytest.mark.parametrize(
    "v, expected",
    [
        ((3, 4), 5.0),
        ((-3, -4), 5.0),
        ((0, 0), 0.0),
        ((1.5, 2.5), math.sqrt(8.5)),
        ((1, 2, 2), 3.0),
    ],
)
def test_norm(v: Vector, expected: float):
    assert math.isclose(norm(v), expected, rel_tol=1e-9)


@pytest.mark.parametrize(
    "v, expected",
    [
        ((3, 4), (0.6, 0.8)),
        ((-3, -4), (-0.6, -0.8)),
        ((1.5, 2.5), (1.5 / math.sqrt(8.5), 2.5 / math.sqrt(8.5))),
        ((1, 2, 2), (1 / 3, 2 / 3, 2 / 3)),
    ],
)
def test_normalize(v: Vector, expected: Vector):
    # Act
    result = normalize(v)

    # Assert
    assert all(
        math.isclose(r, e, rel_tol=1e-9) for r, e in zip(result, expected)
    )


@pytest.mark.parametrize(
    "v",
    [
        (0.0, 0.0),  # 2D zero vector
        (0.0, 0.0, 0.0),  # 3D zero vector
    ],
)
def test_normalize_zero_vector(v: Vector):
    with pytest.raises(ValueError, match="Cannot normalize the zero vector"):
        normalize(v)


@pytest.mark.parametrize(
    "u, v, expected",
    [
        ((1, 0), (0, 1), True),
        ((1, 2), (2, 4), False),
        ((0, 0), (0, 0), True),
        ((1, 0, 0), (0, 1, 0), True),
        ((1, 2, 3), (4, 5, 6), False),
    ],
)
def test_are_orthogonal(u: Vector, v: Vector, expected: bool):
    assert are_orthogonal(u, v) == expected


@pytest.mark.parametrize(
    "u, v, expected",
    [
        ((1, 2), (2, 4), True),
        ((1, 2), (2, 3), False),
        ((0, 0), (0, 0), True),
        ((1, 2, 3), (2, 4, 6), True),
        ((1, 2, 3), (4, 5, 6), False),
    ],
)
def test_are_parallel(u: Vector, v: Vector, expected: bool):
    assert are_parallel(u, v) == expected


@pytest.mark.parametrize(
    "u, v, expected",
    [
        ((1, 2), (3, 4), True),
        ((1, 2), (3, 4, 5), False),
        ((1, 2, 3), (4, 5, 6), True),
        ((1, 2, 3), (4, 5), False),
    ],
)
def test_are_same_dimension(u: Vector, v: Vector, expected: bool):
    assert are_same_dimension(u, v) == expected
