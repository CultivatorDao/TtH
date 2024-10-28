class InputHandler:

    def __init__(self, engine):
        self.engine = engine
        self.map = self.engine.world
        self.commands: dict = self.engine.state.commands
        self.key_bindings: dict = self.create_key_bindings()

    def create_key_bindings(self):
        if len(self.engine.state.key_bindings.keys()) != len(self.commands):
            return {key: list(self.commands.keys())[key] for key in range(len(self.commands.keys()))}
        else:
            return self.engine.state.key_bindings

    def get_command(self):
        self.display_commands()
        command = input()
        self.execute_command(command)
        print(self.engine.character.position)

    def display_commands(self):
        for key in self.key_bindings.keys():
            print(f"[{key.capitalize()}]{self.key_bindings[key]}  ", end="")
        print()

    def execute_command(self, command):
        if command in self.key_bindings.keys():
            self.commands[self.key_bindings[command]]()
