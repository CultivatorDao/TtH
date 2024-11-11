from .base_state import State
from components import PositionComponent


class AdventureState(State):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Adventure"
        self.world = self.engine.world.map
        self.character_position: PositionComponent = self.engine.character.position
        self.create_commands(
            [
                ["w", "Up", self.travel_up],
                ["a", "Left", self.travel_left],
                ["s", "Down", self.travel_down],
                ["d", "Right", self.travel_right],
                ["k", "Look Around", self.engine.world.map.check_collisions, True],
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

    def display_actions(self):
        print(*self.commands)

    def display_sight(self):
        self.world.character_sight()

    def display(self, *args, **kwargs):
        self.display_sight()
        self.display_actions()
        if self.engine.dialogue:
            self.engine.dialogue.show()

    def handle_dialogue(self, action):
        if self.engine.dialogue:
            return self.engine.dialogue.perform(action)
        else:
            return True

    def perform(self, action):
        if self.handle_dialogue(action):
            action.execute()
