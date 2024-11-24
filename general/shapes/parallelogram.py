from .shape import Shape


class Rectangle(Shape):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def has_point(self, x: int, y: int, null_center: bool = False) -> bool:
        x, y = self.set_cords(x, y)

        return abs(x / self.width + y / self.height) + abs(y / self.height - x / self.width) <= 1


class Square(Rectangle):

    def __init__(self, side_length=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = side_length if side_length else self.width
        self.height = side_length if side_length else self.height
