from .base_component import BaseComponent
from .skill_component import SkillComponent

from entities import Mob
from functools import partial


class ActionComponent(BaseComponent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target: Mob = None
        self.skills: SkillComponent = self.parent.skills

    def set_target(self, target):
        self.target = target

    def fist_attack(self):
        return self.skills.base_skills[0].use(self.target)

    def kick_attack(self):
        return self.skills.base_skills[1].use(self.target)

    def ki_blast(self):
        return self.skills.base_skills[2].use(self.target)

    def use_from_quick_slot(self, slot):
        if self.skills.quick_slots[slot]:
            return [slot, self.skills.quick_slots[slot].name, partial(self.skills.quick_slots[slot].use, self.target)]
        else:
            return [slot, "None", None, True]
