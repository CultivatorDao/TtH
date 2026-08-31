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
                ["i", "CHUNK", self.display_chunk],
                ["m", "map", self.display_map]
                # ["k", "Look Around", self.engine.world.map.check_collisions, True],
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

    def display_actions(self, console):
        print(*self.commands)

    def display_chunk(self):
        print(f"Character pos: {self.character_position}")
        chunk_x = self.character_position.x // 100
        chunk_y = self.character_position.y // 50
        print(f"chunk_x: {chunk_x} chunk_y: {chunk_y}")
        for y in range(chunk_y * 50, (chunk_y + 1) * 50):
            for x in range(chunk_x * 100, (chunk_x + 1) * 100):
                if self.world.world_map[x][y].biome.name == "Ocean":
                    print("0", end="")
                else:
                    print("1", end="")
            print()

    def display_map(self):
        for y in range(250):
            for x in range(500):
                if self.world.world_map[x][y].biome.name == "Ocean":
                    print("0", end="")
                else:
                    print("1", end="")
            print()

    def display_sight(self, console):
        self.world.character_sight(console)

    def display(self, console, *args, **kwargs):
        self.display_sight(console=console)
        # self.display_actions(console=console)
        if self.engine.dialogue:
            self.engine.dialogue.show()

    def handle_dialogue(self, action):
        if self.engine.dialogue:
            return self.engine.dialogue.perform(action)
        else:
            return True

    def perform(self, action):
        if self.handle_dialogue(action) and action.name is not None:
            action.execute()
