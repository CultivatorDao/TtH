class State:

    def __init__(self, engine):
        self.engine = engine
        self.default_commands = {
            "Exit": self.engine.exit,
        }
        self.commands = None
        self.default_key_bindings = {
            "Exit": "Exit"
        }
        self.key_bindings = None

    @staticmethod
    def add_commands():
        return {}

    def create_commands_dict(self):
        return dict(self.add_commands(), **self.default_commands)

    @staticmethod
    def add_key_bindings():
        return {}

    def create_key_bindings_dict(self):
        return dict(self.add_key_bindings(), **self.default_key_bindings)
