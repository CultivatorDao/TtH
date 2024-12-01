from components.geometry_component import GeometryComponent


class Shape:

    def __init__(self, x, y, width=1, height=1, corner=True):

        self.geometry = GeometryComponent(x=x,
                                          y=y,
                                          width=width,
                                          height=height)

        self.corner = corner

    def set_cords(self, x, y):
        x -= self.geometry.x
        y -= self.geometry.y
        if self.corner:
            x -= self.geometry.width // 2
            y -= self.geometry.height // 2
        return x, y

    def has_point(self, x: int, y: int, null_center: bool = False) -> bool:
        pass

    def intersects_with(self, area):

        x1, y1 = self.geometry.top_left
        x2, y2 = self.geometry.bottom_right
        x3, y3 = area.geometry.top_left
        x4, y4 = area.geometry.bottom_right

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
