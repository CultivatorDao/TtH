import math
import random

from .base_component import BaseComponent


class PhysicalComponent(BaseComponent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.physical_power = math.ceil(random.randrange(100, 500))
        self.armor = self.physical_power // 50
        self.physical_body = ['CLOSED', 'CLOSED', 'CLOSED', 'CLOSED', 'CLOSED', 'CLOSED', 'CLOSED', 'CLOSED']
        self.bare_hand = self.physical_power // 25
        self.hand = self.bare_hand  # + hand_modifier // maybe was used for buffs IDK
        self.kick = int((self.bare_hand * 2) / 1.5)
        self.physical_power_modifier = 10  # ???

