import os

from input_handler import InputHandler
from world import World
from state import AdventureState, BattleState
from entities import Character

# TODO: Add doc-strings and comment everywhere if they needed.


class Engine:

    def __init__(self):
        self.character = Character()
        self.world = World(engine=self)

        # TODO: Improve state changing mechanism.
        self.states = {
            "Adventure": AdventureState(engine=self),
            "Battle": BattleState(engine=self)
        }
        self.default_state = AdventureState(engine=self)
        self.state = self.default_state
        self.dialogue = None
        self.input_handler = InputHandler(engine=self)

        self.is_on = True

    def change_state(self, state):
        self.state = self.states[state]

    def exit(self):
        self.is_on = False

    def main(self):
        while self.is_on:
            os.system("cls")

            # get_command returns function that will be called in state.perform
            self.state.display()
            self.state.perform(self.input_handler.get_command())

    def run(self):
        self.main()


eng = Engine()

if __name__ == "__main__":
    eng.run()
