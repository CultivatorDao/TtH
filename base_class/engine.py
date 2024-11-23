import os
import state as st

from general.custom_types import StateType

from base_class.input_handler import InputHandler
from base_class.save_manager import SaveManager

from world.world import World
from entities.mobs import Character

# TODO: Add doc-strings and comment everywhere if they needed.


class Engine:

    def __init__(self):
        self.character = Character()
        self.world = World(engine=self)

        self.save_manager = None
        self.states: dict[StateType] = None
        self.default_state = None
        self.state = None
        self.dialogue = None
        self.input_handler = None

        self.__initialize()

        self.is_on = True

    def __initialize(self, engine=None):
        data = self if not engine else engine
        self.save_manager = SaveManager(engine=data)

        # TODO: Improve state changing mechanism.

        self.states = {
            "Adventure": st.AdventureState(engine=data),
            "Battle": st.BattleState(engine=data),
            "Menu": st.MenuState(engine=data)
        }
        self.default_state = self.states["Adventure"]
        self.state = self.default_state
        self.dialogue = None
        self.input_handler = InputHandler(engine=data)

    def open_menu(self):
        self.states["Menu"].previous = self.state.name
        self.change_state("Menu")

    def load(self):
        data: Engine = self.save_manager.load()

        self.character = data.character
        self.world = World(engine=data)

        self.__initialize(engine=data)

    def save(self):
        self.save_manager.save()

    def change_state(self, state):
        self.state = self.states[state]
        self.input_handler = InputHandler(engine=self)

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
