import math
import re
from dataclasses import dataclass, field
from typing import Callable, Optional, Tuple

@dataclass
class Point:
    """
    A class to represent a point in 2D space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """
    x: float = 0.0
    y: float = 0.0

    def __str__(self) -> str:
        """
        Returns a string representation of the point.

        Returns:
            str: The string representation of the point.
        """
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the point.

        Returns:
            str: The detailed string representation of the point.
        """
        return f"Point(x={self.x}, y={self.y})"

    @staticmethod
    def from_coordinates(x: float, y: float) -> "Point":
        """
        Creates a Point instance from x and y coordinates.

        Args:
            x (float): The x-coordinate.
            y (float): The y-coordinate.

        Returns:
            Point: A new Point instance.
        """
        return Point(x, y)

    @staticmethod
    def from_tuple(item: Tuple[float, float]) -> "Point":
        """
        Creates a Point instance from a tuple of coordinates.

        Args:
            item (Tuple[float, float]): A tuple containing the x and y coordinates.

        Returns:
            Point: A new Point instance.
        """
        return Point(item[0], item[1])

    @staticmethod
    def from_string(item: str) -> "Point":
        """
        Creates a Point instance from a string representation.

        Args:
            item (str): The string representation of the point.

        Returns:
            Point: A new Point instance.
        """
        return Point.parse(item)

    @staticmethod
    def parse(repr_str: str) -> "Point":
        """
        Parses a string representation to create a Point instance.

        Args:
            repr_str (str): The string representation of the point.

        Returns:
            Point: A new Point instance.

        Raises:
            ValueError: If the string representation is invalid.
        """
        match = re.match(r"Point\(x=(.*), y=(.*)\)|\((.*), (.*)\)", repr_str)

        if not match:
            raise ValueError(f"Invalid Point representation: {repr_str}")

        if match.groups()[0]:
            x, y = match.groups()[:2]
            x, y = float(x), float(y)
        else:
            x, y = map(float, match.groups()[2:])

        return Point(x, y)

# Define the type for the metric
Metric = Callable[[float, float, float, float], float]

def is_degenerate(x1: float, y1: float, x2: float, y2: float) -> bool:
    """
    Checks if the line segment defined by two points is degenerate (i.e., the points are the same).

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        bool: True if the line segment is degenerate, False otherwise.
    """
    return distance(x1, y1, x2, y2) == 0.0

def slope(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculates the slope of the line segment defined by two points.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        float: The slope of the line segment, or NaN if the line is vertical or degenerate.
    """
    if is_degenerate(x1, y1, x2, y2) or is_vertical(x1, y1, x2, y2):
        return float("nan")

    return (y2 - y1) / (x2 - x1)

def is_vertical(x1: float, y1: float, x2: float, y2: float) -> bool:
    """
    Checks if the line segment defined by two points is vertical.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        bool: True if the line segment is vertical, False otherwise.
    """
    if x1 == x2 and y1 == y2:
        return False

    return x1 == x2

def is_horizontal(x1: float, y1: float, x2: float, y2: float) -> bool:
    """
    Checks if the line segment defined by two points is horizontal.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        bool: True if the line segment is horizontal, False otherwise.
    """
    if x1 == x2 and y1 == y2:
        return False

    return y1 == y2

def are_parallel(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    x3: float,
    y3: float,
    x4: float,
    y4: float,
    tolerance: float = 0.01,
) -> bool:
    """
    Checks if two line segments are parallel.

    Args:
        x1 (float): The x-coordinate of the first point of the first line segment.
        y1 (float): The y-coordinate of the first point of the first line segment.
        x2 (float): The x-coordinate of the second point of the first line segment.
        y2 (float): The y-coordinate of the second point of the first line segment.
        x3 (float): The x-coordinate of the first point of the second line segment.
        y3 (float): The y-coordinate of the first point of the second line segment.
        x4 (float): The x-coordinate of the second point of the second line segment.
        y4 (float): The y-coordinate of the second point of the second line segment.
        tolerance (float): The tolerance for comparing slopes.

    Returns:
        bool: True if the line segments are parallel, False otherwise.
    """
    m1 = slope(x1, y1, x2, y2)
    m2 = slope(x3, y3, x4, y4)

    if math.isnan(m1) and math.isnan(m2):
        return True

    return abs(m1 - m2) <= tolerance

def are_collinear(
    x1: float, y1: float, x2: float, y2: float, x3: float, y3: float
) -> bool:
    """
    Checks if three points are collinear.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.
        x3 (float): The x-coordinate of the third point.
        y3 (float): The y-coordinate of the third point.

    Returns:
        bool: True if the points are collinear, False otherwise.
    """
    if distance(x1, y1, x2, y2) == 0.0:
        return True

    if distance(x2, y2, x3, y3) == 0.0:
        return True

    if distance(x1, y1, x3, y3) == 0.0:
        return True

    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0

def euclidian_metric(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculates the Euclidean distance between two points.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        float: The Euclidean distance between the points.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def taxicab_metric(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculates the Taxicab (Manhattan) distance between two points.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        float: The Taxicab distance between the points.
    """
    return abs(x2 - x1) + abs(y2 - y1)

def chebyshev_metric(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculates the Chebyshev distance between two points.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        float: The Chebyshev distance between the points.
    """
    return max(abs(x2 - x1), abs(y2 - y1))

def minkowski_metric(
    x1: float, y1: float, x2: float, y2: float, p: float
) -> float:
    """
    Calculates the Minkowski distance between two points.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.
        p (float): The order of the Minkowski distance.

    Returns:
        float: The Minkowski distance between the points.
    """
    return (abs(x2 - x1) ** p + abs(y2 - y1) ** p) ** (1 / p)

def cosine_similarity_metric(
    x1: float, y1: float, x2: float, y2: float
) -> float:
    """
    Calculates the cosine similarity between two points.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.

    Returns:
        float: The cosine similarity between the points.
    """
    dot_product = x1 * x2 + y1 * y2
    magnitude1 = math.sqrt(x1**2 + y1**2)
    magnitude2 = math.sqrt(x2**2 + y2**2)
    if magnitude1 == 0 or magnitude2 == 0:
        return float("nan")
    return dot_product / (magnitude1 * magnitude2)

def distance(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    metric: Metric = euclidian_metric,
) -> float:
    """
    Calculates the distance between two points using a specified metric.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y2 (float): The y-coordinate of the second point.
        metric (Metric): The metric function to use for distance calculation.

    Returns:
        float: The distance between the points.
    """
    return metric(x1, y1, x2, y2)

@dataclass
class LineSegment:
    """
    A class to represent a line segment in 2D space.

    Attributes:
        p1 (Point): The first endpoint of the line segment.
        p2 (Point): The second endpoint of the line segment.
    """
    p1: Point = field(default_factory=Point)
    p2: Point = field(default_factory=Point)

    def __str__(self) -> str:
        """
        Returns a string representation of the line segment.

        Returns:
            str: The string representation of the line segment.
        """
        return f"LineSegment({self.p1}, {self.p2})"

    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the line segment.

        Returns:
            str: The detailed string representation of the line segment.
        """
        return f"LineSegment(p1={self.p1}, p2={self.p2})"

    def length(self) -> float:
        """
        Returns the length of the line segment.

        Returns:
            float: The length of the line segment.
        """
        return distance(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def slope(self) -> float:
        """
        Returns the slope of the line segment.

        Returns:
            float: The slope of the line segment.
        """
        return slope(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def is_vertical(self) -> bool:
        """
        Checks if the line segment is vertical.

        Returns:
            bool: True if the line segment is vertical, False otherwise.
        """
        return is_vertical(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def is_horizontal(self) -> bool:
        """
        Checks if the line segment is horizontal.

        Returns:
            bool: True if the line segment is horizontal, False otherwise.
        """
        return is_horizontal(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def is_degenerate(self) -> bool:
        """
        Checks if the line segment is degenerate (i.e., the endpoints are the same).

        Returns:
            bool: True if the line segment is degenerate, False otherwise.
        """
        return is_degenerate(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    @staticmethod
    def from_coordinates(
        x1: float, y1: float, x2: float, y2: float
    ) -> "LineSegment":
        """
        Creates a LineSegment instance from coordinates.

        Args:
            x1 (float): The x-coordinate of the first endpoint.
            y1 (float): The y-coordinate of the first endpoint.
            x2 (float): The x-coordinate of the second endpoint.
            y2 (float): The y-coordinate of the second endpoint.

        Returns:
            LineSegment: A new LineSegment instance.
        """
        return LineSegment.from_points(Point(x1, y1), Point(x2, y2))

    @staticmethod
    def from_points(p1: Point, p2: Point) -> "LineSegment":
        """
        Creates a LineSegment instance from two points.

        Args:
            p1 (Point): The first endpoint.
            p2 (Point): The second endpoint.

        Returns:
            LineSegment: A new LineSegment instance.
        """
        return LineSegment(p1, p2)