import math

from typing import Tuple

from astrocompute.models.polar import Polar


def to_cartesian(r, theta: float) -> tuple:
    """
    Converts polar coordinates to Cartesian coordinates.

    :param: r: Radius
    :param: theta: Angle in radians
    :return: Cartesian coordinates as a tuple (x, y)
    """
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    return x, y


def from_cartesian(x: float, y: float) -> Tuple[float, float]:
    """
    Converts Cartesian coordinates to polar coordinates.

    :param x: x-coordinate
    :param y: y-coordinate
    :return: Polar coordinates
    """
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)

    return r, theta


def add(r1, theta1, r2, theta2: float) -> Tuple[float, float]:
    """
    Adds two polar coordinates.

    :param r1: Radius of the first polar coordinate
    :param theta1: Angle of the first polar coordinate
    :param r2: Radius of the second polar coordinate
    :param theta2: Angle of the second polar coordinate
    :return: Sum of the two polar coordinates
    """
    x1, y1 = to_cartesian(r1, theta1)
    x2, y2 = to_cartesian(r2, theta2)
    x_sum = x1 + x2
    y_sum = y1 + y2

    return from_cartesian(x_sum, y_sum)


def subtract(r1, theta1, r2, theta2: float) -> Tuple[float, float]:
    """
    Subtracts the second polar coordinate from the first.

    :param r1: Radius of the first polar coordinate
    :param theta1: Angle of the first polar coordinate
    :param r2: Radius of the second polar coordinate
    :param theta2: Angle of the second polar coordinate
    :return: Difference of the two polar coordinates
    """
    x1, y1 = to_cartesian(r1, theta1)
    x2, y2 = to_cartesian(r2, theta2)
    x_diff = x1 - x2
    y_diff = y1 - y2

    return from_cartesian(x_diff, y_diff)


def multiply(r, theta, scalar: float) -> Tuple[float, float]:
    """
    Multiplies a polar coordinate by a scalar.

    :param r: Radius of the polar coordinate
    :param theta: Angle of the polar coordinate
    :param scalar: Scalar to multiply by
    :return: Result of the scalar multiplication
    """
    x, y = to_cartesian(r, theta)
    x_product = x * scalar
    y_product = y * scalar

    return from_cartesian(x_product, y_product)


def rotate(r, theta, angle: float) -> Tuple[float, float]:
    """
    Rotates a polar coordinate by a given angle.

    :param r: Radius of the polar coordinate
    :param theta: Angle of the polar coordinate
    :return: Rotated polar coordinate
    """
    new_theta = theta + angle

    return r, new_theta
