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

        # Secondary characteristics
        self.toxicity = 0
        self.gold = 0
        self.inventory = []
        self.skills = ['Pressure Point ', 'atk', 10, 5, color.Color.White, 300, 'Neutral']

        # Hp Properties
        # self.full_hp = 100
        # self.hp = self.full_hp
        # self.regeneration = 1
        # self.hp_mastery = 0
        # self.hp_mastery_req = 20

        # Ki Properties
        # self.cultivation_lvl = 1
        # self.max_ki = 50
        # self.ki = self.max_ki
        # self.ki_modifier = 1
        # self.max_ki_modifier = 100
        # self.ki_recovery = random.randrange(1, 6)
        #
        # self.ki_power = random.randrange(200, 700)
        # self.ki_power_modifier = 10
        # self.ki_control = 1
        # self.ki_lvl = 1
        # self.ki_mastery = 0
        # self.ki_mastery_req = 5000

        # Physical Properties
        # self.physical_power = math.ceil(random.randrange(100, 500))
        # self.armor = self.physical_power // 50
        # self.physical_body = ['CLOSED', 'CLOSED', 'CLOSED', 'CLOSED', 'CLOSED', 'CLOSED', 'CLOSED', 'CLOSED']
        # self.fist_lvl = 1
        # self.kick_lvl = 1
        # self.bare_hand = self.physical_power // 25
        # self.hand = self.bare_hand  # + hand_modifier // maybe was used for buffs IDK
        # self.kick = int((self.bare_hand * 2) // 1.5)
        # self.physical_power_modifier = 10
        # self.fist_modifier = 5
        # self.kick_modifier = 10
        # self.fist_mastery = 0
        # self.kick_mastery = 0
        # self.fist_mastery_req = 10
        # self.kick_mastery_req = 20

        # Life span Properties
        # self.life_span = 200
        # self.max_age = random.randrange(70, 90)
        # self.life_span_modifier = 1
        # self.year = 18
        # self.month = 0
        # self.week = 0
        # self.day = 0
        # self.hour = 0
        # self.minute = 0
