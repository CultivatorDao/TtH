from .base_component import BaseComponent


class GeometryComponent(BaseComponent):

    def __init__(self, x, y, width, height, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        if hasattr(self.parent, "corner"):
            self.corner = self.parent.corner
        else:
            self.corner = True

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
