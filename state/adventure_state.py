from .base_state import State
from components import PositionComponent


class AdventureState(State):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.character_position: PositionComponent = self.engine.character.position
        self.commands = self.create_commands_dict()
        self.key_bindings = self.create_key_bindings_dict()

    def add_commands(self):
        return {
            "Up": self.travel_up,
            "Down": self.travel_down,
            "Right": self.travel_right,
            "Left": self.travel_left
        }

    def add_key_bindings(self):
        return {
            "w": "Up",
            "a": "Left",
            "s": "Down",
            "d": "Right"
        }

    def travel_up(self):
        self.character_position.move(0, -1)

    def travel_down(self):
        self.character_position.move(0, 1)

    def travel_right(self):
        self.character_position.move(1, 0)

    def travel_left(self):
        self.character_position.move(-1, 0)
