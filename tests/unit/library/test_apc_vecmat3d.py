import pytest

from astrocompute.library.vector3d import (
    add,
    cross_product,
    dot_product,
    norm,
    normalize,
    scalar_multiply,
)
from astrocompute.models.vector import Vector3D


@pytest.mark.parametrize(
    "u, v, expected",
    [
        (Vector3D(1, 2, 3), Vector3D(4, 5, 6), Vector3D(5, 7, 9)),
        (Vector3D(-1, -2, -3), Vector3D(1, 2, 3), Vector3D(0, 0, 0)),
        (Vector3D(0, 0, 0), Vector3D(0, 0, 0), Vector3D(0, 0, 0)),
    ],
)
def test_add(u, v, expected):
    """
    Test the add function with various cases.
    """
    # Act
    result = add(u, v)

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "u, v",
    [
        (None, Vector3D(1, 2, 3)),
        (Vector3D(1, 2, 3), None),
    ],
)
def test_add_value_error(u, v):
    """
    Test the add function raises ValueError for undefined arguments.
    """
    with pytest.raises(ValueError):
        add(u, v)


@pytest.mark.parametrize(
    "s, v, expected",
    [
        (2, Vector3D(1, 2, 3), Vector3D(2, 4, 6)),
        (-1, Vector3D(1, 2, 3), Vector3D(-1, -2, -3)),
        (0, Vector3D(1, 2, 3), Vector3D(0, 0, 0)),
    ],
)
def test_scalar_multiply(s, v, expected):
    """
    Test the scalar_multiply function with various cases.
    """
    # Act
    result = scalar_multiply(s, v)

    # Assert
    assert result == expected


def test_scalar_multiply_value_error():
    """
    Test the scalar_multiply function raises ValueError for undefined arguments.
    """
    with pytest.raises(ValueError):
        scalar_multiply(2, None)


@pytest.mark.parametrize(
    "u, v",
    [
        (None, Vector3D(1, 2, 3)),
        (Vector3D(1, 2, 3), None),
    ],
)
def test_add_value_error(u, v):
    """
    Test the add function raises ValueError for undefined arguments.
    """
    with pytest.raises(ValueError):
        add(u, v)


@pytest.mark.parametrize(
    "u, v, expected",
    [
        (Vector3D(1, 2, 3), Vector3D(4, 5, 6), 32),
        (Vector3D(-1, -2, -3), Vector3D(1, 2, 3), -14),
        (Vector3D(0, 0, 0), Vector3D(1, 2, 3), 0),
    ],
)
def test_dot_product(u, v, expected):
    """
    Test the dot_product function with various cases.
    """
    # Act
    result = dot_product(u, v)

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "u, v",
    [
        (None, Vector3D(1, 2, 3)),
        (Vector3D(1, 2, 3), None),
    ],
)
def test_dot_product_value_error(u, v):
    """
    Test the dot_product function raises ValueError for undefined arguments.
    """
    with pytest.raises(ValueError):
        dot_product(u, v)


@pytest.mark.parametrize(
    "u, v, expected",
    [
        (Vector3D(1, 2, 3), Vector3D(4, 5, 6), Vector3D(-3, 6, -3)),
        (Vector3D(1, 0, 0), Vector3D(0, 1, 0), Vector3D(0, 0, 1)),
        (Vector3D(0, 0, 0), Vector3D(1, 2, 3), Vector3D(0, 0, 0)),
    ],
)
def test_cross_product(u, v, expected):
    """
    Test the cross_product function with various cases.
    """
    # Act
    result = cross_product(u, v)

    # Assert
    assert result == expected


@pytest.mark.parametrize(
    "u, v",
    [
        (None, Vector3D(1, 2, 3)),
        (Vector3D(1, 2, 3), None),
    ],
)
def test_cross_product_value_error(u, v):
    """
    Test the cross_product function raises ValueError for undefined arguments.
    """
    with pytest.raises(ValueError):
        cross_product(u, v)


@pytest.mark.parametrize(
    "v, expected",
    [
        (Vector3D(1, 2, 2), 3),
        (Vector3D(0, 0, 0), 0),
        (Vector3D(-1, -2, -2), 3),
    ],
)
def test_norm(v, expected):
    """
    Test the norm function with various cases.
    """
    # Act
    result = norm(v)

    # Assert
    assert result == pytest.approx(expected)


def test_norm_zero_vector():
    """
    Test the normalize function with a zero vector.
    """
    # Act & Assert
    with pytest.raises(ValueError):
        norm(None)


@pytest.mark.parametrize(
    "v, expected",
    [
        (Vector3D(1, 2, 2), Vector3D(1 / 3, 2 / 3, 2 / 3)),
        (Vector3D(-1, -2, -2), Vector3D(-1 / 3, -2 / 3, -2 / 3)),
    ],
)
def test_normalize(v, expected):
    """
    Test the normalize function with various cases.
    """
    # Act
    result = normalize(v)

    # Assert
    assert result == expected


def test_normalize_zero_vector():
    """
    Test the normalize function with a zero vector.
    """
    # Arrange
    v = Vector3D(0, 0, 0)

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        normalize(v)


@pytest.mark.parametrize(
    "v1, v2, expected",
    [
        (Vector3D(1, 2, 3), Vector3D(4, 5, 6), Vector3D(5, 7, 9)),
        (Vector3D(-1, -2, -3), Vector3D(1, 2, 3), Vector3D(0, 0, 0)),
        (Vector3D(0, 0, 0), Vector3D(0, 0, 0), Vector3D(0, 0, 0)),
    ],
)
def test_vec3d_add(v1, v2, expected):
    assert v1 + v2 == expected


@pytest.mark.parametrize(
    "v1, v2, expected",
    [
        (Vector3D(1, 2, 3), Vector3D(4, 5, 6), Vector3D(-3, -3, -3)),
        (Vector3D(-1, -2, -3), Vector3D(1, 2, 3), Vector3D(-2, -4, -6)),
        (Vector3D(0, 0, 0), Vector3D(0, 0, 0), Vector3D(0, 0, 0)),
    ],
)
def test_vec3d_sub(v1, v2, expected):
    assert v1 - v2 == expected


@pytest.mark.parametrize(
    "v, scalar, expected",
    [
        (Vector3D(1, 2, 3), 2, Vector3D(2, 4, 6)),
        (Vector3D(-1, -2, -3), -1, Vector3D(1, 2, 3)),
        (Vector3D(0, 0, 0), 5, Vector3D(0, 0, 0)),
    ],
)
def test_vec3d_mul(v, scalar, expected):
    assert v * scalar == expected


@pytest.mark.parametrize(
    "v, scalar, expected",
    [
        (Vector3D(2, 4, 6), 2, Vector3D(1, 2, 3)),
        (Vector3D(-1, -2, -3), -1, Vector3D(1, 2, 3)),
        (Vector3D(0, 0, 0), 5, Vector3D(0, 0, 0)),
    ],
)
def test_vec3d_truediv(v, scalar, expected):
    assert v / scalar == expected


def test_vec3d_truediv_zero_division():
    with pytest.raises(ZeroDivisionError):
        Vector3D(1, 2, 3) / 0


@pytest.mark.parametrize(
    "v, expected",
    [
        (Vector3D(1, 2, 2), 3),
        (Vector3D(0, 0, 0), 0),
        (Vector3D(-1, -2, -2), 3),
    ],
)
def test_vec3d_norm(v, expected):
    assert v.norm() == pytest.approx(expected)


@pytest.mark.parametrize(
    "v, expected",
    [
        (Vector3D(1, 2, 2), Vector3D(1 / 3, 2 / 3, 2 / 3)),
        (Vector3D(0, 0, 0), Vector3D(0, 0, 0)),
        (Vector3D(-1, -2, -2), Vector3D(-1 / 3, -2 / 3, -2 / 3)),
    ],
)
def test_vec3d_normalize(v, expected):
    if v.norm() == 0:
        with pytest.raises(ZeroDivisionError):
            v.normalize()
    else:
        assert v.normalize() == expected


def test_vec3d_str():
    v = Vector3D(1, 2, 3)
    assert str(v) == "(1, 2, 3)"
