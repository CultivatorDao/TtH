import components
import random

from ..entity import Entity


class Mob(Entity):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = "Mob"
        self.health = components.HealthComponent(parent=self)
        self.physics = components.PhysicalComponent(parent=self)
        self.ki = components.KiComponent(parent=self)
        self.skills = components.SkillComponent(parent=self)
        self.action = components.ActionComponent(parent=self)

    @property
    def display(self):
        return f"{self.name}\n{self.health}\nKi: {self.ki}\n"

    def __str__(self):
        return self.display

    # TODO: Make more complex mob behavior
    def behavior(self, target):
        """
        Specify behavior of any mob except player.
        :return: str
        """
        return self.action.skills.base_skills[random.randint(0, 2)].use(target)

    def is_alive(self):
        return self.health.hp > 0
