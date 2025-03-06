import re
import math
from typing import Optional, Union, overload
from dataclasses import dataclass


@dataclass
class Point2D:
    x: Optional[float] = float(0)
    y: Optional[float] = float(0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point2D(x={self.x}, y={self.y})"

    @staticmethod
    def parse(repr_str: str) -> 'Point2D':
        match = re.match(r"Point2D\(x=(.*), y=(.*)\)|\((.*), (.*)\)", repr_str)
        if match:
            x, y = map(float, match.groups()[:2] if match.groups()[0] else match.groups()[2:])
            return Point2D(x, y)
        raise ValueError(f"Invalid Point2D representation: {repr_str}")

    @staticmethod
    def distance(p: 'Point2D', q: 'Point2D') -> float:
        return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2)

    @staticmethod
    def midpoint(p: 'Point2D', q: 'Point2D') -> 'Point2D':
        """
        Calculate the midpoint between two points.

        :param p: The first point
        :param q: The second point
        :return: The midpoint between the points
        """
        return Point2D((p.x + q.x) / 2, (p.y + q.y) / 2)

    @staticmethod
    def slope(p: 'Point2D', q: 'Point2D') -> float:
        """
        Calculate the slope of the line through two points.

        :param p: The first point
        :param q: The second point
        :return: The slope of the line
        :raises: ValueError if the line is vertical
        """
        if p.x == q.x:
            raise ValueError("Slope is undefined for vertical line")
        return (q.y - p.y) / (q.x - p.x)

    @staticmethod
    def y_intercept(p: 'Point2D', q: 'Point2D') -> float:
        """
        Calculate the y-intercept of the line through two points.

        :param p: The first point
        :param q: The second point
        :return: The y-intercept of the line
        """
        return p.y - Point2D.slope(p, q) * p.x

    @staticmethod
    def x_intercept(p: 'Point2D', q: 'Point2D') -> float:
        """
        Calculate the x-intercept of the line through two points.

        :param p: The first point
        :param q: The second point
        :return: The x-intercept of the line
        """
        return -Point2D.y_intercept(p, q) / Point2D.slope(p, q)

    @staticmethod
    def is_vertical(p: 'Point2D', q: 'Point2D') -> bool:
        """
        Check if the line through two points is vertical.

        :param p: The first point
        :param q: The second point
        :return: True if the line is vertical, False otherwise
        """
        return p.x == q.x

    @staticmethod
    def is_horizontal(p: 'Point2D', q: 'Point2D') -> bool:
        """
        Check if the line through two points is horizontal.

        :param p: The first point
        :param q: The second point
        :return: True if the line is horizontal, False otherwise
        """
        return p.y == q.y

    @staticmethod
    def is_parallel(p: 'Point2D', q: 'Point2D', r: 'Point2D', s: 'Point2D') -> bool:
        """
        Check if two lines are parallel.

        :param p: A point on the first line
        :param q: Another point on the first line
        :param r: A point on the second line
        :param s: Another point on the second line
        :return: True if the lines are parallel, False otherwise
        """
        return Point2D.slope(p, q) == Point2D.slope(r, s)

    @staticmethod
    def is_perpendicular(p: 'Point2D', q: 'Point2D', r: 'Point2D', s: 'Point2D') -> bool:
        """
        Check if two lines are perpendicular.

        :param p: A point on the first line
        :param q: Another point on the first line
        :param r: A point on the second line
        :param s: Another point on the second line
        :return: True if the lines are perpendicular, False otherwise
        """
        return Point2D.slope(p, q) * Point2D.slope(r, s) == -1

    @staticmethod
    def are_collinear(p: 'Point2D', q: 'Point2D', r: 'Point2D') -> bool:
        """
        Check if three points are collinear.

        :param p: First point
        :param q: Second point
        :param r: Third point
        :return: True if the points are collinear, False otherwise
        """
        return (r.y - p.y) * (q.x - p.x) == (q.y - p.y) * (r.x - p.x)

    @staticmethod
    def create_from_coordinates(x: float, y: float) -> 'Point2D':
        return Point2D(x, y)

    @staticmethod
    def create_from_coordinate_str(repr_str: str) -> 'Point2D':
        return Point2D.parse(repr_str)

    @staticmethod
    def create_from_polar_coordinates(r: float, theta: float) -> 'Point2D':
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return Point2D(x, y)



@dataclass
class Point3D:
    x: Optional[float] = float(0)
    y: Optional[float] = float(0)
    z: Optional[float] = float(0)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"

    @staticmethod
    def parse(repr_str: str) -> 'Point3D':
        match = re.match(r"Point3D\(x=(.*), y=(.*), z=(.*)\)|\((.*), (.*), (.*)\)", repr_str)
        if match:
            x, y, z = map(float, match.groups()[:3] if match.groups()[0] else match.groups()[3:])
            return Point3D(x, y, z)
        raise ValueError(f"Invalid Point3D representation: {repr_str}")

    @staticmethod
    def distance(point1: 'Point3D', point2: 'Point3D') -> float:
        return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2 + (point2.z - point1.z) ** 2)

    @staticmethod
    def midpoint(p: 'Point3D', q: 'Point3D') -> 'Point3D':
        """
        Calculate the midpoint between two points.

        :param p: The first point
        :param q: The second point
        :return: The midpoint between the points
        """
        return Point3D((p.x + q.x) / 2, (p.y + q.y) / 2, (p.z + q.z) / 2)

    @staticmethod
    def are_collinear(p: 'Point3D', q: 'Point3D', r: 'Point3D') -> bool:
        """
        Check if three points are collinear.

        :param p: First point
        :param q: Second point
        :param r: Third point
        :return: True if the points are collinear, False otherwise
        """
        # Calculate vectors
        v1 = (q.x - p.x, q.y - p.y, q.z - p.z)
        v2 = (r.x - q.x, r.y - q.y, r.z - q.z)

        # Calculate cross product
        cross_product = (
            v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0]
        )

        # If cross product is (0, 0, 0), the points are collinear
        return cross_product == (0, 0, 0)

    @staticmethod
    def are_coplanar(p: 'Point3D', q: 'Point3D', r: 'Point3D', s: 'Point3D') -> bool:
        """
        Check if four points are coplanar.

        :param p: First point
        :param q: Second point
        :param r: Third point
        :param s: Fourth point
        :return: True if the points are coplanar, False otherwise
        """
        # Calculate vectors
        v1 = (q.x - p.x, q.y - p.y, q.z - p.z)
        v2 = (r.x - p.x, r.y - p.y, r.z - p.z)
        v3 = (s.x - p.x, s.y - p.y, s.z - p.z)

        # Calculate scalar triple product
        scalar_triple_product = v1[0] * (v2[1] * v3[2] - v2[2] * v3[1]) - v1[1] * (v2[0] * v3[2] - v2[2] * v3[0]) + v1[2] * (v2[0] * v3[1] - v2[1] * v3[0])

        # If scalar triple product is 0, the points are coplanar
        return scalar_triple_product == 0

    @staticmethod
    def are_cocircular(p: 'Point3D', q: 'Point3D', r: 'Point3D', s: 'Point3D') -> bool:
        """
        Check if four points are cocircular.

        :param p: First point
        :param q: Second point
        :param r: Third point
        :param s: Fourth point
        :return: True if the points are cocircular, False otherwise
        """
        # Calculate the determinant of the matrix
        determinant = (
            p.x * (q.y * r.z - q.z * r.y) -
            p.y * (q.x * r.z - q.z * r.x) +
            p.z * (q.x * r.y - q.y * r.x)
        )

        # If the determinant is 0, the points are cocircular
        return determinant == 0

    @staticmethod
    def create_from_coordinates(x: float, y: float, z: float) -> 'Point3D':
        return Point3D(x, y, z)

    @staticmethod
    def create_from_coordinate_str(repr_str: str) -> 'Point3D':
        return Point3D.parse(repr_str)


def parse_point(repr_str: str) -> Union[Point2D, Point3D]:
    """
    Parse a Point2D or Point3D object from its string representation.

    :param repr_str: String representation of the Point2D or Point3D object
    :return: Point2D or Point3D object
    :raises: ValueError if the string representation is invalid
    """
    if repr_str.startswith("Point2D") or repr_str.startswith("(") and repr_str.count(",") == 1:
        return Point2D.parse(repr_str)

    if repr_str.startswith("Point3D") or repr_str.startswith("(") and repr_str.count(",") == 2:
        return Point3D.parse(repr_str)

    raise ValueError(f"Unknown point representation: {repr_str}")



def create_point(x: float, y: float, z: float = 0) -> Union[Point2D, Point3D]:
    """
    Create a Point2D or Point3D object from the given coordinates.

    :param x: The x-coordinate
    :param y: The y-coordinate
    :param z: The z-coordinate (default: 0)
    :return: Point2D or Point3D object
    """
    if z == 0:
        return Point2D(x, y)
    return Point3D(x, y, z)
