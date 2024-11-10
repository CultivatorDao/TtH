from .base_state import State

from entities.mobs.mob import Mob


class BattleState(State):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.character = self.engine.character
        self.enemy = Mob()
        self.character.action.set_target(self.enemy)

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
            "win": self.__win,
            "lose": self.__lose
        }

    def __win(self):
        print(f"You killed {self.enemy.name}")
        self.engine.change_state("Adventure")

    def __lose(self):
        print(f"You lost to {self.enemy.name}")

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
        # This action will open your skill list.
        # We need other condition for this to avoid getting damage while choosing skill.
        # TODO: Implement choosing other skill through dialog or sub-state in future.
        if action and action.key == "r".upper():
            action.execute()
        if action and not action.key == "r".upper():
            self.log = action.execute(), self.enemy.behavior(self.character)
            if not self.character.is_alive():
                self.__state = "lose"
            if not self.enemy.is_alive():
                self.__state = "win"
        else:
            self.log = None
