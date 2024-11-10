import random
from .base_component import BaseComponent


class KiComponent(BaseComponent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.talent = random.randrange(1, 11)

        self.max_ki = 50
        self.ki = self.max_ki
        self.ki_modifier = 1
        self.max_ki_modifier = 100
        self.ki_recovery = random.randrange(1, 6)

        self.ki_power = random.randrange(200, 700)
        self.ki_power_modifier = 10
        self.ki_control = 1
        self.ki_lvl = 1
        self.ki_mastery = 0
        self.ki_mastery_req = 5000

    def __str__(self):
        return f"{self.ki}/{self.max_ki}"
