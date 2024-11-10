from general.custom_types import MobType


class Skill:

    class Types:

        damage = "Damage"
        heal = "Heal"
        utility = "Utility"

    class DamageTypes:

        physical = "Physical"
        mystical = "Mystical"
        # elemental = "Elemental"

    def __init__(self, user: MobType):

        self.user = user
        self.name = "Skill"
        self.type = ""
        self.damage_type = ""
        self.level = 1
        self.max_level = 10
        self.cost = 0

        self.mastery = 0
        self.level_up_mastery = 100
        self.modifier = 1

        self.power_source = 0
        #: Specify formula of how damage will be calculated.
        self.power = 0

    def __str__(self):
        return f"{self.name}: {self.power} damage"

    def level_up(self, *args, **kwargs):
        """
        What will happen when skill levels up.
        :return: None
        """
        if self.level < self.max_level:
            self.level += 1
            self.mastery -= self.level_up_mastery
            self.level_up_mastery = int(self.level_up_mastery * 1.1)
            self.modifier += 0.1
            self.power = int(self.power_source * self.modifier)

    def progress(self, *args, **kwargs):
        """
        Specify how skill will progress.
        :return: None
        """
        self.mastery += 1
        if self.mastery >= self.level_up_mastery:
            self.level_up()

    def skill_effect_description(self):
        """
        Formulate what skill does.
        Must return skill effect message:\n
        Skill name, what it does, power, type, damage type as string
        :return: str
        """
        return f"{self.name} {'deals' if self.type == self.Types.damage else 'healed'} " \
               f"{self.power} {self.damage_type} {'damage' if self.type == self.Types.damage else 'health'}"

    def activate(self, target: MobType):
        target.health.change_hp(self.power - target.physics.armor)

    def use(self, target):
        # TODO: Use spend_ki method of KiComponent to handle this.
        if self.user.ki.ki - self.cost >= 0:
            self.user.ki.ki -= self.cost
            self.activate(target)
            self.progress()
            return self.skill_effect_description()
        else:
            return f"Not enough Ki to use {self.name}"

    def description(self):
        print(f"{self.name} Damage: {self.power}")
