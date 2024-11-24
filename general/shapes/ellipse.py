import math

from .shape import Shape


class Ellipse(Shape):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def has_point(self, x: int, y: int, null_center: bool = False) -> bool:
        x, y = self.set_cords(x, y)
        return math.pow(x, 2) / (self.width // 2) ** 2 + math.pow(y, 2) / (self.height // 2) ** 2 <= 1


class Circle(Ellipse):

    def __init__(self, radius=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = radius if radius else self.width
        self.height = radius if radius else self.height
