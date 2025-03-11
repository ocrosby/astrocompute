from dataclasses import dataclass

from typing import Optional, Callable

@dataclass
class Point:
    x: float
    y: float

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"


# Define the type for the metric
Metric = Callable[[Point, Point], float]

def euclidian_metric(p1: Point, p2: Point) -> float:
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5

def taxicab_metric(p1: Point, p2: Point) -> float:
    return abs(p2.x - p1.x) + abs(p2.y - p1.y)


@dataclass
class Line:
    p1: Point
    p2: Point

    def __str__(self) -> str:
        return f"Line({self.p1}, {self.p2})"

    def __repr__(self) -> str:
        return f"Line(p1={self.p1}, p2={self.p2})"

    def __len__(self):
        """
        Returns the length of the line segment

        :return:
        """
        return euclidian_metric(self.p1, self.p2)

    def rise(self) -> float:
        """
        Returns the change in y of the line segment

        :return: the change in y of the line segment
        """
        return self.p2.y - self.p1.y

    def run(self) -> float:
        """
        Returns the change in x of the line segment

        :return: the change in x of the line segment
        """
        return self.p2.x - self.p1.x

    def slope(self) -> float:
        delta_y = self.rise()
        delta_x = self.run()

        if delta_x == 0:
            return float("inf")

        return self.rise() / self.run()

    def is_degenerate(self) -> bool:
        return len(self) == 0

    @staticmethod
    def create_from_coordinates(x1: float, y1: float, x2: float, y2: float) -> "Line":
        return Line.create_from_points(Point(x1, y1), Point(x2, y2))

    @staticmethod
    def create_from_points(p1: Point, p2: Point) -> "Line":
        return Line(p1, p2)


