import random
import color

import components


class Character:

    def __init__(self):

        self.position = components.PositionComponent(0, 0, parent=self)
        self.health = components.HealthComponent(parent=self)
        self.ki = components.KiComponent(parent=self)
        self.physics = components.PhysicalComponent(parent=self)
        self.cultivation = components.CultivationComponent(parent=self)
        self.lifespan = components.LifespanComponent(parent=self)

        self.eyesight = 5

        # Secondary characteristics
        self.toxicity = 0
        self.gold = 0
        self.inventory = []
        self.skills = ['Pressure Point ', 'atk', 10, 5, color.Color.White, 300, 'Neutral']

        self.icon = "@"
