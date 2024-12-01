import math

from .shape import Shape


class Ellipse(Shape):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def has_point(self, x: int, y: int, null_center: bool = False) -> bool:
        x, y = self.set_cords(x, y)
        return math.pow(x, 2) / (self.geometry.width // 2) ** 2 \
            + math.pow(y, 2) / (self.geometry.height // 2) ** 2 <= 1


class Circle(Ellipse):

    def __init__(self, radius=0, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry.width = max(radius, self.geometry.width)
        self.geometry.height = max(radius, self.geometry.height)
