from .base_state import State


class MenuState(State):

    def __init__(self, engine):
        super().__init__(engine)
        self.set_default([], blank=True)
        self.previous = None
        self.create_commands(
            [
                ["1", "Save", self.engine.save],
                ["2", "Load", self.engine.load],
                ["e", "Close", self.close_menu],
                ["~", "Exit", self.engine.exit]
            ]
        )

    def close_menu(self):
        self.engine.change_state(self.previous)

    def display_commands(self, *args, **kwargs):
        print(*self.commands)

    def display(self, *args, **kwargs):
        self.display_commands()

    def perform(self, action):
        action.execute()

