from state.command import Command


class State:
    """
    To create default command list use:
        self_default_instructions = X
    To create command list use:
        self.create_commands(X)
    Where X: list<list>:
        [
            [
            key: string,
            name: string,
            command: function,
            hide_button: bool
            ],
            ...
        ]
    """

    def __init__(self, engine):
        self.engine = engine
        self._default_instructions = [
            ["k", "Look Around", self.engine.world.map.check_collisions, True],
            ["~", "Exit", self.engine.exit],
        ]
        self.commands = []

    def set_default(self, instructions: list, blank=False):
        """
        Set default commands. If blank set True other default commands will be deleted.
        :param instructions: list<list>
        :param blank: bool
        :return: None
        """
        if blank:
            self._default_instructions = instructions
        else:
            self._default_instructions.extend(instructions)

    def create_command(self, quarry):
        if len(quarry) == 3:
            self.commands.append(Command(quarry[0].capitalize(), quarry[1], quarry[2], self))
        else:
            self.commands.append(Command(quarry[0].capitalize(), quarry[1], quarry[2], self, quarry[3]))

    def create_commands(self, instructions: list):
        for instruction in instructions + self._default_instructions:
            self.create_command(instruction)
