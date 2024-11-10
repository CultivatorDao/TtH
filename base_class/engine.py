import os


from base_class.input_handler import InputHandler
from base_class.save_manager import SaveManager

from world import World
from state import AdventureState, BattleState
from entities.mobs import Character

# TODO: Add doc-strings and comment everywhere if they needed.


class Engine:

    def __init__(self):
        self.character = Character()
        self.world = World(engine=self)

        self.save_manager = SaveManager(engine=self)

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

    def load(self):
        data: Engine = self.save_manager.load()

        self.character = data.character
        self.world = World(engine=data)

        self.save_manager = SaveManager(engine=data)

        self.states = {
            "Adventure": AdventureState(engine=data),
            "Battle": BattleState(engine=data)
        }
        self.default_state = self.states["Adventure"]
        self.state = self.default_state
        self.dialogue = data.dialogue
        self.input_handler = InputHandler(engine=data)

    def save(self):
        self.save_manager.save()

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
