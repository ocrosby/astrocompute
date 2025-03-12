import math

import pytest

from astrocompute.library.geo2d import (
    LineSegment,
    Point,
    are_collinear,
    are_parallel,
    distance,
    euclidian_metric,
    is_degenerate,
    is_horizontal,
    is_vertical,
    slope,
    taxicab_metric,
)


def test_default_point():
    # Arrange & Act
    p = Point()

    # Assert
    assert p.x == 0, f"Expected: 0, Actual: {p.x}"
    assert p.y == 0, f"Expected: 0, Actual: {p.y}"


def test_default_line():
    # Arrange & Act
    l = LineSegment()

    # Assert
    assert l.p1.x == 0, f"Expected: 0, Actual: {l.p1.x}"
    assert l.p1.y == 0, f"Expected: 0, Actual: {l.p1.y}"
    assert l.p2.x == 0, f"Expected: 0, Actual: {l.p2.x}"
    assert l.p2.y == 0, f"Expected: 0, Actual: {l.p2.y}"


@pytest.mark.parametrize(
    "item, expected",
    [
        ((0, 0), Point(0, 0)),
        ((1, 0), Point(1, 0)),
        ((2, 0), Point(2, 0)),
        ((1, 1), Point(1, 1)),
        ((1.5, 2.5), Point(1.5, 2.5)),
    ],
)
def test_point_from_tuple(item, expected):
    # Arrange
    p = Point.from_tuple(item)

    # Act
    actual = p

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, x3, y3, expected",
    [
        (0, 0, 0, 0, 0, 0, True),
        (0, 0, 1, 0, 1, 0, True),
        (1, 1, 0, 0, 1, 1, True),
        (0, 0, 1, 0, 2, 0, True),
        (0, 0, 1, 1, 2, 2, True),
        (0, 0, 1, 1, 0, 2, False),
    ],
)
def test_are_collinear(x1, y1, x2, y2, x3, y3, expected):
    # Act
    actual = are_collinear(x1, y1, x2, y2, x3, y3)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, True),
        (0, 0, 1, 0, False),
        (0, 0, 1, 1, False),
        (1, 2, 3, 4, False),
    ],
)
def test_is_degenerate(x1, y1, x2, y2, expected):
    # Act
    actual = is_degenerate(x1, y1, x2, y2)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (0, 0, Point(0, 0)),
        (1, 0, Point(1, 0)),
        (2, 0, Point(2, 0)),
        (1, 1, Point(1, 1)),
        (1.5, 2.5, Point(1.5, 2.5)),
    ],
)
def test_point_from_coordinates(x, y, expected):
    # Arrange
    p = Point.from_coordinates(x, y)

    # Act
    actual = p

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (0, 0, "(0, 0)"),
        (1, 0, "(1, 0)"),
        (2, 0, "(2, 0)"),
        (1, 1, "(1, 1)"),
        (1.5, 2.5, "(1.5, 2.5)"),
    ],
)
def test_point_str(x, y, expected):
    # Arrange
    p = Point(x, y)

    # Act
    actual = str(p)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, "LineSegment((0, 0), (0, 0))"),
        (0, 0, 1, 0, "LineSegment((0, 0), (1, 0))"),
        (0, 0, 2, 0, "LineSegment((0, 0), (2, 0))"),
        (0, 0, 1, 1, "LineSegment((0, 0), (1, 1))"),
    ],
)
def test_line_segment_str(x1, y1, x2, y2, expected):
    # Arrange
    l = LineSegment.from_coordinates(x1, y1, x2, y2)

    # Act
    actual = str(l)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, "LineSegment(p1=(0, 0), p2=(0, 0))"),
        (0, 0, 1, 0, "LineSegment(p1=(0, 0), p2=(1, 0))"),
        (0, 0, 2, 0, "LineSegment(p1=(0, 0), p2=(2, 0))"),
        (0, 0, 1, 1, "LineSegment(p1=(0, 0), p2=(1, 1))"),
    ],
)
def test_line_segment_repr(x1, y1, x2, y2, expected):
    # Arrange
    l = LineSegment.from_coordinates(x1, y1, x2, y2)

    # Act
    actual = repr(l)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (0, 0, "Point(x=0, y=0)"),
        (1, 0, "Point(x=1, y=0)"),
        (2, 0, "Point(x=2, y=0)"),
        (1, 1, "Point(x=1, y=1)"),
        (1.5, 2.5, "Point(x=1.5, y=2.5)"),
    ],
)
def test_point_repr(x, y, expected):
    # Arrange
    p = Point(x, y)

    # Act
    actual = repr(p)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, 0.0),
        (0, 0, 1, 0, 1.0),
        (0, 0, 2, 0, 2.0),
        (0, 0, 1, 1, 1.4142135623730951),
    ],
)
def test_line_segment_len(x1, y1, x2, y2, expected):
    # Arrange
    l = LineSegment.from_coordinates(x1, y1, x2, y2)

    # Act
    actual = l.length()

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, float("nan")),
        (0, 0, 1, 0, 0.0),
        (0, 0, 2, 0, 0.0),
        (0, 0, 1, 1, 1.0),
        (0, 0, 0, 1, float("nan")),
    ],
)
def test_slope(x1, y1, x2, y2, expected):
    # Act
    actual = slope(x1, y1, x2, y2)

    # Assert
    if math.isnan(expected):
        assert math.isnan(actual), f"Expected: {expected}, Actual: {actual}"
    else:
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, float("nan")),
        (0, 0, 1, 0, 0.0),
        (0, 0, 2, 0, 0.0),
        (0, 0, 1, 1, 1.0),
        (0, 0, 0, 1, float("nan")),
    ],
)
def test_line_segment_slope(x1, y1, x2, y2, expected):
    # Arrange
    l = LineSegment.from_coordinates(x1, y1, x2, y2)

    # Act
    actual = l.slope()

    # Assert
    if math.isnan(expected):
        assert math.isnan(actual), f"Expected: {expected}, Actual: {actual}"
    else:
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, False),
        (0, 0, 1, 0, False),
        (0, 0, 1, 1, False),
        (0, 0, 0, 1, True),
    ],
)
def test_line_segment_is_vertical(x1, y1, x2, y2, expected):
    # Arrange
    l = LineSegment.from_coordinates(x1, y1, x2, y2)

    # Act
    actual = l.is_vertical()

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, False),  # Degenerate Case
        (0, 0, 1, 0, False),  # Horizontal
        (0, 0, 1, 1, False),  # Diagonal
        (0, 0, 0, 1, True),  # Vertical
        (1, 0, 1, 1, True),  # Vertical
    ],
)
def test_is_vertical(x1, y1, x2, y2, expected):
    # Act
    actual = is_vertical(x1, y1, x2, y2)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, False),  # Degenerate Case
        (0, 0, 1, 0, True),  # Horizontal
        (0, 1, 1, 1, True),  # Horizontal
        (0, 0, 1, 1, False),  # Diagonal
        (0, 0, 0, 1, False),  # Vertical
    ],
)
def test_is_horizontal(x1, y1, x2, y2, expected):
    # Act
    actual = is_horizontal(x1, y1, x2, y2)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, False),
        (0, 0, 1, 0, True),
        (0, 0, 1, 1, False),
        (0, 0, 0, 1, False),
    ],
)
def test_line_segment_is_horizontal(x1, y1, x2, y2, expected):
    # Arrange
    l = LineSegment.from_coordinates(x1, y1, x2, y2)

    # Act
    actual = l.is_horizontal()

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, True),
        (0, 0, 1, 0, False),
        (0, 0, 1, 1, False),
        (0, 0, 0, 1, False),
    ],
)
def test_line_segment_is_degenerate(x1, y1, x2, y2, expected):
    # Arrange
    l = LineSegment.from_coordinates(x1, y1, x2, y2)

    # Act
    actual = l.is_degenerate()

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, 0.0),
        (0, 0, 1, 0, 1.0),
        (0, 0, 2, 0, 2.0),
        (0, 0, 1, 1, 1.4142135623730951),
    ],
)
def test_distance(x1, y1, x2, y2, expected):
    # Act
    actual = distance(x1, y1, x2, y2)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, 0.0),
        (0, 0, 1, 0, 1.0),
        (0, 0, 2, 0, 2.0),
        (0, 0, 1, 1, 1.4142135623730951),
    ],
)
def test_euclidian_metric(x1, y1, x2, y2, expected):
    # Act
    actual = euclidian_metric(x1, y1, x2, y2)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, 0.0),
        (0, 0, 1, 0, 1.0),
        (0, 0, 2, 0, 2.0),
        (0, 0, 1, 1, 2.0),
    ],
)
def test_taxicab_metric(x1, y1, x2, y2, expected):
    # Act
    actual = taxicab_metric(x1, y1, x2, y2)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Point(x=1, y=2)", Point(1, 2)),
        ("(1, 2)", Point(1, 2)),
        ("Point(x=0, y=0)", Point(0, 0)),
        ("(0, 0)", Point(0, 0)),
        ("Point(x=-1, y=-2)", Point(-1, -2)),
        ("(-1, -2)", Point(-1, -2)),
        ("Point(x=1.5, y=2.5)", Point(1.5, 2.5)),
        ("(1.5, 2.5)", Point(1.5, 2.5)),
        ("Point(x=1e3, y=2e3)", Point(1e3, 2e3)),
        ("(1e3, 2e3)", Point(1e3, 2e3)),
        (
            "Point(x=inf, y=inf)",
            Point(float("inf"), float("inf")),
        ),
        ("(inf, inf)", Point(float("inf"), float("inf"))),
        (
            "Point(x=-inf, y=-inf)",
            Point(float("-inf"), float("-inf")),
        ),
        ("(-inf, -inf)", Point(float("-inf"), float("-inf"))),
        ("Point(x=1, y=2)", Point(1, 2)),
        ("Point(x=0, y=0)", Point(0, 0)),
    ],
)
def test_point_parse(input_str, expected):
    # Act
    actual = Point.parse(input_str)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Point(x=1, y=2)", Point(1, 2)),
        ("(1, 2)", Point(1, 2)),
        ("Point(x=0, y=0)", Point(0, 0)),
        ("(0, 0)", Point(0, 0)),
        ("Point(x=-1, y=-2)", Point(-1, -2)),
        ("(-1, -2)", Point(-1, -2)),
        ("Point(x=1.5, y=2.5)", Point(1.5, 2.5)),
        ("(1.5, 2.5)", Point(1.5, 2.5)),
        ("Point(x=1e3, y=2e3)", Point(1e3, 2e3)),
        ("(1e3, 2e3)", Point(1e3, 2e3)),
        (
            "Point(x=inf, y=inf)",
            Point(float("inf"), float("inf")),
        ),
        ("(inf, inf)", Point(float("inf"), float("inf"))),
        (
            "Point(x=-inf, y=-inf)",
            Point(float("-inf"), float("-inf")),
        ),
        ("(-inf, -inf)", Point(float("-inf"), float("-inf"))),
        ("Point(x=1, y=2)", Point(1, 2)),
        ("Point(x=0, y=0)", Point(0, 0)),
    ],
)
def test_point_from_string(input_str: str, expected: Point):
    # Arrange
    p = Point.from_string(input_str)

    # Act
    actual = p

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"


@pytest.mark.parametrize(
    "input_str",
    [
        "invalid",
        "(1, 2, 3)",
        "Point(x=1, y=2",
    ],
)
def test_point_parse_invalid(input_str: str):
    print(f"Testing input: {input_str}")
    with pytest.raises(ValueError):
        Point.parse(input_str)


@pytest.mark.parametrize(
    "x1, y1, x2, y2, x3, y3, x4, y4, expected",
    [
        (0, 0, 0, 1, 1, 0, 1, 1, True),  # Vertical
        (0, 0, 1, 0, 0, 1, 1, 1, True),  # Horizontal
        (0, 0, 1, 1, 1, 0, 2, 1, True),  # Diagonal
        (0, 0, 1, 1, 0, 1, 1, 0, False),  # Not parallel
    ],
)
def test_are_parallel(x1, y1, x2, y2, x3, y3, x4, y4, expected):
    # Act
    actual = are_parallel(x1, y1, x2, y2, x3, y3, x4, y4)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"
