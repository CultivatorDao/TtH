from .base_state import State


class Dialogue(State):

    def __init__(self, message, instructions, can_skip=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.can_skip = True
        self.message = message
        self.set_default([
            ["`", "Close", self.close],
        ], blank=True)
        self.create_commands(instructions)

    def show(self):
        print(self.message)
        for key in self.commands:
            print(key, end="")
        print()

    def close(self):
        self.engine.dialogue = None
