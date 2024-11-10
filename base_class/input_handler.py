from state.command import Command


class InputHandler:

    def __init__(self, engine):
        self.engine = engine
        self.world = self.engine.world
        self.commands = self.engine.state.commands

    def get_command(self):
        # self.display_commands()
        command = input()
        if command:
            command = command[0]
        # self.execute_command(command)
        for action in self.commands:
            if action.key == command.upper():
                return action
        return Command(key=command.lower())
