import math
from typing import Optional

import pytest

from astrocompute.library.point import Point2D


@pytest.mark.point2d
def test_default_2d_constructor():
    # Arrange & Act
    p = Point2D()

    # Assert
    assert p.x == 0
    assert p.y == 0


@pytest.mark.point2d
def test_default_2d_str():
    # Arrange
    p = Point2D()

    # Act
    actual = str(p)

    # Assert
    assert actual == "(0.0, 0.0)"


@pytest.mark.point2d
def test_default_2d_repr():
    # Arrange
    p = Point2D()

    # Act
    actual = repr(p)

    # Assert
    assert actual == "Point2D(x=0.0, y=0.0, name=None)"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, 0.0),
        (0, 0, 1, 0, 1.0),
        (0, 0, 2, 0, 2.0),
    ],
)
def test_dx(x1: float, y1: float, x2: float, y2: float, expected: float):
    # Arrange
    p = Point2D(x1, y1)
    q = Point2D(x2, y2)

    # Act
    actual = Point2D.dx(p, q)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, 0.0),
        (0, 0, 0, 1, 1.0),
        (0, 0, 0, 2, 2.0),
    ],
)
def test_dy(x1: float, y1: float, x2: float, y2: float, expected: float):
    # Arrange
    p = Point2D(x1, y1)
    q = Point2D(x2, y2)

    # Act
    actual = Point2D.dy(p, q)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, True),
        (0, 0, 1, 0, False),
        (0, 0, 2, 0, False),
    ],
)
def test_same_point(x1: float, y1: float, x2: float, y2: float, expected: bool):
    # Arrange
    p = Point2D(x1, y1)
    q = Point2D(x2, y2)

    # Act
    actual = Point2D.same_point(p, q)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "p, q, expected_message",
    [
        (None, None, "p1, p2 cannot be None"),
        (Point2D(1, 2), None, "p2 cannot be None"),
        (None, Point2D(1, 2), "p1 cannot be None"),
    ],
)
def test_same_point_invalid(
    p: Optional[Point2D], q: Optional[Point2D], expected_message: str
):
    # Act & Assert
    with pytest.raises(ValueError) as e:
        Point2D.same_point(p, q)

    assert str(e.value) == expected_message


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Point2D(x=1, y=2, name=None)", Point2D(1, 2)),
        ("(1, 2)", Point2D(1, 2)),
        ("Point2D(x=0, y=0, name=None)", Point2D(0, 0)),
        ("(0, 0)", Point2D(0, 0)),
        ("Point2D(x=-1, y=-2, name=None)", Point2D(-1, -2)),
        ("(-1, -2)", Point2D(-1, -2)),
        ("Point2D(x=1.5, y=2.5, name=None)", Point2D(1.5, 2.5)),
        ("(1.5, 2.5)", Point2D(1.5, 2.5)),
        ("Point2D(x=1e3, y=2e3, name=None)", Point2D(1e3, 2e3)),
        ("(1e3, 2e3)", Point2D(1e3, 2e3)),
        (
            "Point2D(x=inf, y=inf, name=None)",
            Point2D(float("inf"), float("inf")),
        ),
        ("(inf, inf)", Point2D(float("inf"), float("inf"))),
        (
            "Point2D(x=-inf, y=-inf, name=None)",
            Point2D(float("-inf"), float("-inf")),
        ),
        ("(-inf, -inf)", Point2D(float("-inf"), float("-inf"))),
        ("Point2D(x=1, y=2, name='A')", Point2D(1, 2, "A")),
        ("Point2D(x=0, y=0, name='Origin')", Point2D(0, 0, "Origin")),
    ],
)
def test_point2d_parse(input_str, expected):
    # Act
    actual = Point2D.parse(input_str)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(
    "input_str",
    [
        "invalid",
        "Point2D(x=1, y=2)",
        "(1, 2, 3)",
        "Point2D(x=1, y=2, name='A'",
    ],
)
def test_point2d_parse_invalid(input_str: str):
    print(f"Testing input: {input_str}")
    with pytest.raises(ValueError):
        Point2D.parse(input_str)


def test_distance_p_undefined():
    # Arrange
    p = None
    q = Point2D(1, 2)

    # Act & Assert
    with pytest.raises(ValueError):
        Point2D.distance(p, q)


def test_distance_q_undefined():
    # Arrange
    p = Point2D(1, 2)
    q = None

    # Act & Assert
    with pytest.raises(ValueError):
        Point2D.distance(p, q)


@pytest.mark.parametrize(
    "p, q, expected",
    [
        (Point2D(2, 3), Point2D(5, 7), 5.0),
        (Point2D(5, 7), Point2D(8, 1), 6.708),
        (Point2D(8, 1), Point2D(2, 3), 6.325),
    ],
)
def test_distance(p, q, expected):
    # Act
    actual = Point2D.distance(p, q)

    # Assert
    assert (
        round(actual, 3) == expected
    ), f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "p, q, expected",
    [
        (Point2D(2, 3), Point2D(8, 7), Point2D(5, 5)),
    ],
)
def test_midpoint(p, q, expected):
    # Act
    actual = Point2D.midpoint(p, q)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "p, q, expected", [(Point2D(-2, 4), Point2D(4, 8), 2.0 / 3.0)]
)
def test_slope(p, q, expected):
    # Act
    actual = Point2D.slope(p, q)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


def test_slope_vertical():
    # Arrange
    p = Point2D(1, 2)
    q = Point2D(1, 3)

    # Act
    m = Point2D.slope(p, q)

    # Assert
    assert math.isnan(m), f"Expected: NaN, Actual: {m}"
