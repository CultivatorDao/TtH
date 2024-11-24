# from .shape import Shape


class Shape:

    def __init__(self, x, y, width=1, height=1, corner=True):

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.corner = corner

    @property
    def rect_size(self):
        return (self.width + (self.width % 2 == 0)) * (self.height + (self.height % 2 == 0))

    @property
    def top_left(self):
        return (self.x, self.y) if self.corner \
            else (self.x - self.width // 2, self.y - self.height // 2)

    @property
    def bottom_right(self):
        return (self.x + self.width - (self.width % 2 != 0), self.y + self.height - (self.height % 2)) if self.corner \
            else (self.x + self.width // 2, self.y + self.height // 2)

    def set_cords(self, x, y):
        x -= self.x
        y -= self.y
        if self.corner:
            x -= self.width // 2
            y -= self.height // 2
        return x, y

    def has_point(self, x: int, y: int, null_center: bool = False) -> bool:
        pass

    def intersects_with(self, area):

        x1, y1 = self.top_left
        x2, y2 = self.bottom_right
        x3, y3 = area.top_left
        x4, y4 = area.bottom_right

        left = max(x1, x3)
        right = min(x2, x4)
        top = max(y1, y3)
        bottom = min(y2, y4)

        # print(f"Player top-left: {x1}/{y1}")
        # print(f"Player bottom-right: {x2}/{y2}")
        # print(f"Area top-left: {x3}/{y3}")
        # print(f"Area bottom-right: {x4}/{y4}")

        width = right - left
        height = bottom - top

        # print(f"width: {width}\nheight: {height}")

        if width * height >= 0:
            return True
        else:
            return False

        # max_zone_size = max(self.size, area.size)
        # min_zone_size = min(self.size, area.size)
        # print(f"max_zone: {max_zone_size}")
        # max_distance = max_zone_size + min_zone_size
        # print(f"max_distance: {max_distance}")
        # distance = (abs(self.x - area.x) + abs(self.y - area.y))
        # print(f"distance: {distance}")
        # if distance < max_distance:
        #     return True
        # else:
        #     return False


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
