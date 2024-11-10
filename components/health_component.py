from .base_component import BaseComponent


class HealthComponent(BaseComponent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_hp = 100
        self.hp = self.max_hp
        self.regeneration = 1
        self.hp_mastery = 0
        self.hp_mastery_req = 20

    def __increase_health(self, rate):
        self.max_hp += rate

    def __increase_mastery(self):
        if self.hp_mastery >= self.hp_mastery_req:
            self.hp_mastery -= self.hp_mastery_req
            self.hp_mastery_req = int(self.hp_mastery_req * 1.4)
            self.__increase_health(self.max_hp // 50)

    def __get_damage(self, damage):
        self.hp -= damage
        self.hp_mastery += damage
        self.__increase_mastery()

    def __heal(self, heal):
        if self.hp < self.max_hp:
            self.hp += heal
            self.hp += self.regeneration
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def change_hp(self, damage=0, heal=0):
        self.__get_damage(damage)
        self.__heal(heal)

    def __str__(self):
        return f"Hp: {self.hp}/{self.max_hp}"
