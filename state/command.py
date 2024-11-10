class Command:

    def __init__(self, key, name=None, command=None, dialogue=None, is_hidden=False):
        self.is_hidden = is_hidden
        self.dialogue = dialogue
        self.key = key
        self.name = name
        self.__command = command

    def __str__(self):
        return f"[{self.key}]{self.name}  "

    def execute(self):
        if callable(self.__command):
            return self.__command()
