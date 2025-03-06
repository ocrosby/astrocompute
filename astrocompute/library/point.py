import math
from typing import Union, overload


from astrocompute.models.point import Point2D, Point3D

@overload
def distance(p1: Point2D, p2: Point2D) -> float:
    ...

@overload
def distance(p1: Point3D, p2: Point3D) -> float:
    ...

def distance(p: Union[Point2D, Point3D], q: Union[Point2D, Point3D]) -> float:
    """
    Calculate the distance between two points.

    :param p: First point
    :param q: Second point
    :return: Distance between the points
    """
    if isinstance(p, Point2D):
        return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2)

    return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2 + (q.z - p.z) ** 2)

def slope(p: Point2D, q: Point2D) -> float:
    """
    Calculate the slope of the line through two points.

    :param p: First point
    :param q: Second point
    :return: Slope of the line
    :raises: ValueError if the line is vertical
    """
    if p.x == q.x:
        raise ValueError("Slope is undefined for vertical line")

    return (q.y - p.y) / (q.x - p.x)


@overload
def midpoint(p: Point2D, q: Point2D) -> Point2D:
    ...

@overload
def midpoint(p: Point3D, q: Point3D) -> Point3D:
    ...

def midpoint(p: Union[Point2D, Point3D], q: Union[Point2D, Point3D]) -> Union[Point2D, Point3D]:
    """
    Calculate the midpoint between two points.

    :param p: First point
    :param q: Second point
    :return: Midpoint between the points
    """
    if isinstance(p, Point2D) and isinstance(q, Point2D):
        return Point2D((p.x + q.x) / 2, (p.y + q.y) / 2)

    if isinstance(p, Point3D) and isinstance(q, Point3D):
        return Point3D((p.x + q.x) / 2, (p.y + q.y) / 2, (p.z + q.z) / 2)

    raise ValueError("Both points must be of the same type")

@overload
def is_collinear(p: Point2D, q: Point2D, r: Point2D) -> bool:
    ...

@overload
def is_collinear(p: Point3D, q: Point3D, r: Point3D) -> bool:
    ...

def is_collinear(p: Union[Point2D, Point3D], q: Union[Point2D, Point3D], r: Union[Point2D, Point3D]) -> bool:
    """
    Check if three points are collinear.

    :param p: First point
    :param q: Second point
    :param r: Third point
    :return: True if the points are collinear, False otherwise
    """
    if isinstance(p, Point2D) and isinstance(q, Point2D) and isinstance(r, Point2D):
        return (r.y - p.y) * (q.x - p.x) == (q.y - p.y) * (r.x - p.x)

    if isinstance(p, Point3D) and isinstance(q, Point3D) and isinstance(r, Point3D):
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

    raise ValueError("All points must be of the same type")