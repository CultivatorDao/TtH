import math


class Shape:

    def __init__(self, x, y, size=1, width=1, height=1):

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.size = size

        self.center = True

    @property
    def rect_size(self):
        return (self.width + (self.width % 2 == 0)) * (self.height + (self.height % 2 == 0))

    @property
    def top_left(self):
        return self.x, self.y

    @property
    def bottom_right(self):
        return self.x + self.size - 1, self.y + self.size - 1

    @property
    def top_left_centered(self):
        return self.x - self.size // 2, self.y - self.size // 2

    @property
    def bottom_right_centered(self):
        return self.x + self.size // 2, self.y + self.size // 2

    def set_cords(self, x, y, center=True):
        x -= self.x
        y -= self.y
        if center:
            x -= (self.size // 2 - (self.size % 2 == 0))
            y -= (self.size // 2 - (self.size % 2 == 0))
        return x, y

    def has_point(self, x: int, y: int, null_center: bool = False) -> bool:
        pass

    def intersects_with(self, area):

        x1, y1 = self.x, self.y
        x2, y2 = self.x + self.size - 1, self.y + self.size - 1
        x3, y3 = area.x, area.y
        x4, y4 = area.x + area.size - 1, area.y + area.size - 1

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


class Square(Shape):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def has_point(self, x: int, y: int, null_center: bool = False) -> bool:
        x, y = self.set_cords(x, y, self.center)

        return abs(x + y - (self.size % 2 == 0)) + abs(y - x) <= self.size


class Circle(Shape):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.size = self.size * 2

    def has_point(self, x: int, y: int, null_center: bool = False) -> bool:
        x, y = self.set_cords(x, y)
        return math.pow(x, 2) + math.pow(y, 2) <= (self.size / 2) ** 2


class Ellipse(Shape):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def has_point(self, x: int, y: int, null_center: bool = False) -> bool:
        x, y = self.set_cords(x, y)
        return math.pow(x, 2) / self.width ** 2 + math.pow(y, 2) / self.height ** 2 <= self.size


class Eyesight(Square):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = False

    def intersects_with(self, area):

        x1, y1 = self.top_left_centered
        x2, y2 = self.bottom_right_centered
        x3, y3 = area.top_left
        x4, y4 = area.bottom_right

        # print(f"Player top-left: {x1}/{y1}")
        # print(f"Player bottom-right: {x2}/{y2}")
        # print(f"Area top-left: {x3}/{y3}")
        # print(f"Area bottom-right: {x4}/{y4}")

        left = max(x1, x3)
        right = min(x2, x4)
        top = max(y1, y3)
        bottom = min(y2, y4)

        width = right - left
        height = bottom - top

        # print(f"width: {width}\nheight: {height}")

        if width * height >= 0:
            return True
        else:
            return False
