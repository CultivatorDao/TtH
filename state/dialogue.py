from .base_state import State


class Dialogue(State):

    def __init__(self, message, instructions, can_skip=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.can_skip = can_skip
        self.message = message
        self.set_default([
            ["`", "Close", self.close],
        ], blank=True)
        self.create_commands(instructions)

    def show(self):
        print(self.message)
        print(*self.commands)

    def close(self):
        self.engine.dialogue = None

    def perform(self, action):
        for command in self.commands:
            if command.key == action.key:
                command.execute()
                break
        else:
            if self.can_skip and action.name:
                self.close()
            else:
                return False
        return True
