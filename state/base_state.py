from state.command import Command


class State:

    def __init__(self, engine):
        self.engine = engine
        self._default_instructions = [
            ["k", "Look Around", self.engine.world.map.check_collisions],
            ["~", "Exit", self.engine.exit],
        ]
        self.commands = []

    def set_default(self, instructions, blank=False):
        if blank:
            self._default_instructions = instructions
        else:
            self._default_instructions.extend(instructions)

    def create_command(self, quarry):
        self.commands.append(Command(quarry[0].capitalize(), quarry[1], quarry[2], self))

    def create_commands(self, instructions: list):
        for instruction in instructions + self._default_instructions:
            self.create_command(instruction)
