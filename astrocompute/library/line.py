from dataclasses import dataclass
from typing import Optional

from astrocompute.models.point import Point2D, Point3D

@dataclass
class Line2D:
    p1: Optional[Point2D] = Point2D()
    p2: Optional[Point2D] = Point2D()

    def rise(self) -> float:
        return self.p2.y - self.p1.y

    def run(self) -> float:
        return self.p2.x - self.p1.x

    def slope(self) -> float:
        return self.rise() / self.run()

    def is_degenerate(self) -> bool:
        return self.p1 == self.p2

    @staticmethod
    def create_from_coordinates(x1: float, y1: float, x2: float, y2: float) -> "Line2D":
        return Line2D(Point2D(x1, y1), Point2D(x2, y2))


@dataclass
class Line3D:
    p1: Optional[Point3D] = Point3D()
    p2: Optional[Point3D] = Point3D()

    @staticmethod
    def create_from_points(p1: Point3D, p2: Point3D):
        return Line3D(p1, p2)
