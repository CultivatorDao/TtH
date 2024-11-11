from .base_state import State

from entities.mobs.mob import Mob


class BattleState(State):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Battle"
        self.character = self.engine.character
        self.enemy = None

        self.set_default([
            ["q", "Fist", self.character.action.fist_attack],
            ["w", "Kick", self.character.action.kick_attack],
            ["e", "Ki Blast", self.character.action.ki_blast],
            ["r", "All Skills", self.show_all_skills]
        ], blank=True)

        self.create_commands(
            [self.character.action.use_from_quick_slot(slot) for slot in "12345"]
        )

        self.log = None
        self.display_spacing = 50

        self.__state = None
        self.__states = {
            "win": self.win,
            "lose": self.lose
        }

    def set_enemy(self, enemy):
        self.enemy = enemy
        self.character.action.set_target(self.enemy)

    def win(self):
        print(f"You killed {self.enemy.name}")
        self.__state = None
        self.log = None
        self.set_enemy(None)
        self.engine.change_state("Adventure")

    def lose(self):
        print(f"You died to {self.enemy.name}")
        self.engine.exit()

    def show_all_skills(self):
        self.character.skills.show_all_skills()
        return ""

    def display_actions(self):
        for action in self.commands:
            print(action, end="")
            if action.key == "5":
                print()
        print()

    def display_combatants(self):
        player = self.character.display.split("\n")
        enemy = self.enemy.display.split("\n")
        print(
            *[player[i] + " " * (self.display_spacing - len(player[i])) + enemy[i] for i in range(len(player))],
            sep="\n"
        )

    def display_log(self):
        if self.log:
            print(*self.log, sep=" " * (self.display_spacing - len(self.log[0])))

    def display(self):
        if not self.__state:
            self.display_combatants()
            self.display_log()
            self.display_actions()
        else:
            self.__states[self.__state]()

    def perform(self, action):

        if action.name is None:
            self.log = None
            return None

        if action.key == "r".upper():
            # This action will open your skill list.
            # We need other condition for this to avoid getting damage while choosing skill.
            # TODO: Implement choosing other skill through dialog or sub-state in future.
            action.execute()
        else:
            self.log = action.execute(), self.enemy.behavior(self.character)
            if not self.character.is_alive():
                self.__state = "lose"
            if not self.enemy.is_alive():
                self.__state = "win"
