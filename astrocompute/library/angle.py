from dataclasses import dataclass
from enum import Enum


class AngleFormat(Enum):
    Dd = "Dd"  # pylint: disable=invalid-name
    DMM = "DMM"
    DMMm = "DMMm"  # pylint: disable=invalid-name
    DMMSS = "DMMSS"
    DMMSSs = "DMMSSs"  # pylint: disable=invalid-name


def dms(alpha: float):
    """
    Convert an angle in decimal degrees to degrees, minutes, and seconds

    :param alpha:
    :return:
    """
    d = int(alpha)
    m = int((alpha - d) * 60)
    s = ((alpha - d) * 60 - m) * 60
    return d, m, s


@dataclass
class Angle:
    def __init__(
        self, alpha: float, angle_format: AngleFormat = AngleFormat.Dd
    ):
        self.alpha = alpha
        self.format = angle_format

    def set(self, angle_format: AngleFormat):
        self.format = angle_format


def angle_to_string(
        alpha: float,
        angle_format: AngleFormat,
        precision: int = 2,
        width: int = 12) -> str:
    """
    Convert an angle to a string representation

    :param alpha: The angle in decimal degrees
    :param angle_format: The format of the angle
    :param precision: The precision of the angle representation
    :param width: The width of the resulting string
    :return: The string representation of the angle
    """
    d, m, s = dms(alpha)
    if angle_format == AngleFormat.Dd:
        return f"{alpha:0.{precision}f}".rjust(width)

    if angle_format == AngleFormat.DMM:
        return f"{d} {m:02d}".rjust(width)

    if angle_format == AngleFormat.DMMm:
        decimal_minutes = m + s / 60
        return f"{d} {decimal_minutes:0.{precision}f}".rjust(width)

    if angle_format == AngleFormat.DMMSS:
        return f"{d} {m:02d} {int(s):02d}".rjust(width)

    if angle_format == AngleFormat.DMMSSs:
        return f"{d} {m:02d} {s:0.{precision}f}".rjust(width)

    raise ValueError("Invalid AngleFormat")
