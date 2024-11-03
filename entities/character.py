import color

import components
from .entity import Entity


class Character:

    def __init__(self, *args, **kwargs):

        self.position = components.PositionComponent(13, 13, parent=self)
        self.health = components.HealthComponent(parent=self)
        self.ki = components.KiComponent(parent=self)
        self.physics = components.PhysicalComponent(parent=self)
        self.cultivation = components.CultivationComponent(parent=self)
        self.lifespan = components.LifespanComponent(parent=self)

        self.eyesight = 10

        # Secondary characteristics
        self.toxicity = 0
        self.gold = 0
        self.inventory = []
        self.skills = ['Pressure Point ', 'atk', 10, 5, color.Color.White, 300, 'Neutral']

        self.icon = "@"
