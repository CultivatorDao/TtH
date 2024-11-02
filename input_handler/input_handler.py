class InputHandler:

    def __init__(self, engine):
        self.engine = engine
        self.world = self.engine.world
        self.commands = self.engine.state.commands

    @property
    def keys(self):
        if self.engine.dialogue:
            return self.engine.dialogue.commands + self.commands
        else:
            return self.commands

    def get_command(self):
        self.display_commands()
        command = input()
        self.execute_command(command)

    def display_commands(self):
        for command in self.commands:
            print(command, end="")
        print()
        if self.engine.dialogue:
            self.engine.dialogue.show()

    def execute_command(self, command):
        for key in self.keys:
            if key.key.lower() == command:
                if self.engine.dialogue:
                    if self.engine.dialogue.can_skip:
                        if self.engine.dialogue != key.dialogue:
                            self.engine.dialogue.close()
                            key.execute()
                        else:
                            key.execute()
                    else:
                        pass
                else:
                    key.execute()
