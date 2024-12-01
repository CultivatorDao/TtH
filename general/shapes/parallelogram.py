from .shape import Shape


class Rectangle(Shape):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def has_point(self, x: int, y: int, null_center: bool = False) -> bool:
        x, y = self.set_cords(x, y)

        return abs(x / self.geometry.width + y / self.geometry.height)\
            + abs(y / self.geometry.height - x / self.geometry.width) <= 1


class Square(Rectangle):

    def __init__(self, side_length=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry.width = max(side_length, self.geometry.width)
        self.geometry.height = max(side_length, self.geometry.height)
