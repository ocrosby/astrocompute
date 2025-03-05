"""
The module apc_math.py provides (among others) the two functions:

frac and modulo
"""

import math

from enum import Enum
from typing import Tuple
from dataclasses import dataclass

class AngleFormat(Enum):
    Dd = "Dd"
    DMM = "DMM"
    DMMm = "DMMm"
    DMMSS = "DMMSS"
    DMMSSs = "DMMSSs"


@dataclass
class Angle:
    def __init__(self, alpha: float, format: AngleFormat=AngleFormat.Dd):
        self.alpha = alpha
        self.format = format

    def set(self, format: AngleFormat):
        self.format = format


class AngleSerializer:
    """
    AngleSerializer class to serialize and deserialize angles
    """

    def __init__(self, precision: int = 2, width: int = 12):
        """
        Initialize the AngleSerializer

        :param precision:
        :param width:
        """
        self.precision = precision
        self.width = width

    def serialize(self, angle: Angle) -> str:
        """
        Serialize an angle to a string

        :param angle:
        :return:
        """
        d, m, s = dms(angle.alpha)
        if angle.format == AngleFormat.Dd:
            return f"{angle.alpha:0.{self.precision}f}"
        elif angle.format == AngleFormat.DMM:
            return f"{d} {m:02d}"
        elif angle.format == AngleFormat.DMMm:
            decimal_minutes = m + s / 60
            return f"{d} {decimal_minutes:0.{self.precision}f}"
        elif angle.format == AngleFormat.DMMSS:
            return f"{d} {m:02d} {int(s):02d}"
        elif angle.format == AngleFormat.DMMSSs:
            return f"{d} {m:02d} {s:0.{self.precision}f}"
        else:
            raise ValueError("Invalid AngleFormat")
def frac(x: float) -> float:
    """
    Calculate the fractional part of x

    :param x:
    :return:
    :rtype: float
    :raises: ZeroDivisionError
    """
    floor_value = math.floor(x)
    difference = x - floor_value

    return difference


def modulo(x: float, y: float) -> float:
    """
    Calculate the modulo of x and y

    :param x:
    :param y:
    :return:
    :rtype: float
    :raises: ZeroDivisionError
    """
    return y * frac(x / y)

def ddd(d: int, m: int, s: float) -> float:
    """
    Convert degrees, minutes, seconds to decimal degrees

    :param d: degrees
    :param m: minutes
    :param s: seconds
    :return: Angle in decimal representation
    """
    sign = -1.0 if d < 0 or m < 0 or s < 0 else 1.0
    return sign * (abs(float(d)) + abs(float(m))/60.0 + abs(float(s))/3600.0)

def dms(dd: float) -> Tuple[int, int, float]:
    """
    Convert decimal degrees to degrees, minutes, seconds

    :param dd: Angle in decimal representation
    :return: Tuple of degrees, minutes, seconds
    """
    sign = -1 if dd < 0 else 1
    dd = abs(dd)
    d = int(dd)
    m = int((dd - d) * 60)
    s = (dd - d - m / 60) * 3600

    if sign == -1:
        if d != 0:
            d = -d
        elif m != 0:
            m = -m
        else:
            s = -s

    return d, m, s
