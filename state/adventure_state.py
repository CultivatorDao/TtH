from .base_state import State
from components import PositionComponent


class AdventureState(State):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.world = self.engine.world.map
        self.character_position: PositionComponent = self.engine.character.position
        self.create_commands(
            [
                ["w", "Up", self.travel_up],
                ["a", "Left", self.travel_left],
                ["s", "Down", self.travel_down],
                ["d", "Right", self.travel_right],
            ]
        )

    def travel_up(self):
        self.world.move(0, -1)

    def travel_down(self):
        self.world.move(0, 1)

    def travel_right(self):
        self.world.move(1, 0)

    def travel_left(self):
        self.world.move(-1, 0)
