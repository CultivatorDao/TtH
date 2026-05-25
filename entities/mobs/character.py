import components

from .mob import Mob


class Character(Mob):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = "Player"

        self.position = components.PositionComponent(parent=self)
        self.global_position = components.PositionComponent(parent=self)

        self.cultivation = components.CultivationComponent(parent=self)
        self.lifespan = components.LifespanComponent(parent=self)

        # Secondary characteristics
        self.toxicity = 0
        self.gold = 0
        self.inventory = []

        self.icon = "@"

