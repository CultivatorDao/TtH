from .base_component import BaseComponent


class PositionComponent(BaseComponent):

    def __init__(self, x=0, y=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x = x
        self.y = y

    @property
    def position(self):
        return self.x, self.y

    def move(self, x, y):
        self.x += x
        self.y += y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
