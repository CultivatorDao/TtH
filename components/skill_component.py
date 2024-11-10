from .base_component import BaseComponent

from skills.base_skills import FistAttack, KickAttack, KiBlast


class SkillComponent(BaseComponent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.base_skills: list = [FistAttack(self.parent), KickAttack(self.parent), KiBlast(self.parent)]
        self.skills = []
        self.quick_slots = {
            "1": KiBlast(self.parent),
            "2": None,
            "3": None,
            "4": None,
            "5": None,
        }

    def __getitem__(self, item):
        return self.skills[item]

    def __len__(self):
        return len(self.skills)

    def add_skill(self, skill):
        self.skills.append(skill(self.parent))

    def show_all_skills(self):
        for i in range(len(self)):
            if i + 5 < len(self):
                print(f"[{i + 5 + 1}]{self[i + 5]}")
                continue
            print(f"[{i + 1}]{self[i]}")

    # Will be implemented via state. Until then no use.
    def set_quick_slots(self):
        while True:
            print("Select slot you want to change: ")
            for key in self.quick_slots:
                print(f"[{key}]{self.quick_slots[key]}")
            command = input()
            if command in self.quick_slots:
                print("Choose skill: ")
                self.show_all_skills()
                while True:
                    command = int(input())
                    if command - 1 < len(self.skills):
                        print(command)
                        self[command - 1].description()

            if command == "exit":
                break

    # Now useless. Maybe can be used in the future.
    def use_skill(self, skill_number, target, from_quick_slots=True):
        if from_quick_slots:
            if skill_number in self.quick_slots and self.quick_slots[skill_number]:
                self.quick_slots[skill_number].use(target)
        else:
            # Skill number will be displaying starting from 1.
            # So we subtract 1 from given skill number
            if skill_number - 1 < len(self):
                self[skill_number - 1].use(target)
