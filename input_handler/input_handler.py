class InputHandler:

    def __init__(self, engine):
        self.engine = engine
        self.map = self.engine.world
        self.commands = {
            "exit": self.engine.exit,
            "map": self.map.show_map
        }
        # self.commands = self.engine.state.commands

    def get_command(self):
        for i in range(len(self.commands.keys())):
            print(f"[{i}]{list(self.commands.keys())[i].capitalize()} ", end="")
        print()
        command = input()
        print(list(self.commands.keys())[int(command)])
        if list(self.commands.keys())[int(command)] in self.commands.keys():
            self.commands[list(self.commands.keys())[int(command)]]()
        else:
            pass

