import components

from .mob import Mob
from general.shapes import Square


class Character(Mob):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = "Player"

        self.position = components.PositionComponent(26, 18, parent=self)
        self.cultivation = components.CultivationComponent(parent=self)
        self.lifespan = components.LifespanComponent(parent=self)

        self.eyesight = 30
        self.eyesight_shape = Square(
            x=self.position.x,
            y=self.position.y,
            side_length=2 * self.eyesight + 1,
            corner=False
        )

        # Secondary characteristics
        self.toxicity = 0
        self.gold = 0
        self.inventory = []

        self.icon = "@"

    def move_eyesight(self, x, y):
        self.eyesight_shape.geometry.x = x
        self.eyesight_shape.geometry.y = y
