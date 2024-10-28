from .base_component import BaseComponent


class HealthComponent(BaseComponent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.full_hp = 100
        self.hp = self.full_hp
        self.regeneration = 1
        self.hp_mastery = 0
        self.hp_mastery_req = 20
