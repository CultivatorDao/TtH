from input_handler.input_handler import InputHandler
from world import World
from state.adventure_state import AdventureState
from entities.character import Character

import os


class Engine:

    def __init__(self):
        self.character = Character()
        self.world = World(engine=self)
        self.default_state = AdventureState(engine=self)
        self.state = self.default_state
        self.is_on = True
        self.input_handler = InputHandler(engine=self)

    def main(self):
        self.world.map.character_sight()
        while self.is_on:
            self.input_handler.get_command()

    def run(self):
        self.main()

    def exit(self):
        self.is_on = False


eng = Engine()

if __name__ == "__main__":
    eng.run()
