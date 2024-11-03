class Command:

    def __init__(self, key, name, command, dialogue, is_hidden=False):
        self.is_hidden = is_hidden
        self.dialogue = dialogue
        self.key = key
        self.name = name
        self.__command = command

    def __str__(self):
        return f"[{self.key}]{self.name}  "

    def execute(self):
        self.__command()
