from .skill import Skill


class BaseSkill(Skill):

    def __init__(self, user):
        super().__init__(user)
        self.max_level = 50

    def activate(self, target):
        target.health.change_hp(self.power)


class FistAttack(BaseSkill):

    def __init__(self, user):
        super().__init__(user)
        self.name = "Fist Attack"
        self.type = self.Types.damage
        self.damage_type = self.DamageTypes.physical
        self.cost = 0
        self.power_source = self.user.physics.hand
        self.power = int(self.power_source * self.modifier)


class KickAttack(BaseSkill):

    def __init__(self, user):
        super().__init__(user)
        self.name = "Kick Attack"
        self.type = self.Types.damage
        self.damage_type = self.DamageTypes.physical
        self.cost = 0
        self.power_source = self.user.physics.kick
        self.power = int(self.power_source * self.modifier)


class KiBlast(BaseSkill):

    def __init__(self, user):
        super().__init__(user)
        self.name = "Ki Blast"
        self.type = self.Types.damage
        self.damage_type = self.DamageTypes.mystical
        self.power_source = self.user.ki.ki_power
        self.cost = 25
        self.modifier = 0.05
        self.power = int(self.power_source * self.modifier)

    def __set_modifier(self):
        self.modifier += 0.05
