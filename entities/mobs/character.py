import components

from .mob import Mob


class Character(Mob):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = "Player"

        self.position = components.PositionComponent(1, 20, parent=self)
        # self.health = components.HealthComponent(parent=self)
        # self.ki = components.KiComponent(parent=self)
        # self.physics = components.PhysicalComponent(parent=self)
        self.cultivation = components.CultivationComponent(parent=self)
        self.lifespan = components.LifespanComponent(parent=self)

        # self.skills = components.SkillComponent(parent=self)
        # self.action = components.ActionComponent(parent=self)

        self.eyesight = 10

        # Secondary characteristics
        self.toxicity = 0
        self.gold = 0
        self.inventory = []

        self.icon = "@"
