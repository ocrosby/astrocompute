import pytest

import astrocompute.library.point import Point2D
import astrocompute.library.line import Line2D

@pytest.mark.line2d
def test_default_line():
    # Arrange & Act
    l = Line2D()

    # Assert
    assert l.p1.x == 0.0
    assert l.p1.y == 0.0
    assert l.p2.x == 0.0
    assert l.p2.y == 0.0

@pytest.mark.line2d
@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (0, 0, 0, 0, 0.0, Line2D(Point2D(0, 0), Point2D(0, 0))),
        (0, 0, 1, 0, 1.0, Line2D(Point2D(0, 0), Point2D(1, 0))),
        (0, 0, 2, 0, 2.0, Line2D(Point2D(0, 0), Point2D(2, 0))),
    ]
)
def test_line2d_create_from_coordinates(x1: float, y1: float, x2: float, y2: float, expected: Line2D):
    # Act
    actual = Line2D.create_from_coordinates(x1, y1, x2, y2)

    # Assert
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"

