from math import hypot
from typing import Tuple, Optional, Iterable

class Point():
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance(self, other: "Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)


class Polygon():
    def __init__(self) -> None:
        self.vertices: list[Point] = []

    def add_point(self, point: Point) -> None:
        self.vertices.append((point))

    def perimeter(self) -> float:
        pairs = zip(
            self.vertices, self.vertices[1:] + self.vertices[:1]
        )

        return sum(p1.distance(p2) for p1, p2 in pairs)


class Polygon2:
    def __init__(self, vertices: Optional[Iterable[Point]] = None) -> None:
        self.vertices = list(vertices) if vertices else []


    def perimeter(self) -> float:
        pairs = zip(
            self.vertices, self.vertices[1:] + self.vertices[:1]
        )

        return sum(p1.distance(p2) for p1, p2 in pairs)

class Polygon3:
    


# square = Polygon()
# square.add_point(Point(1, 1))
# square.add_point(Point(1, 2))
# square.add_point(Point(2, 1))
# square.add_point(Point(2, 2))

square = Polygon2(
    [Point(1, 1), Point(1, 2), Point(2, 1), Point(2, 2)]
)

print(square.perimeter())