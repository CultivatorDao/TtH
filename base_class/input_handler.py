import tcod.event

from state.command import Command


class InputHandler:

    def __init__(self, engine):
        self.engine = engine
        self.world = self.engine.world
        self.commands = self.engine.state.commands

    def get_command(self, context):

        for event in tcod.event.wait():
            context.convert_event(event)  # Sets tile coordinates for mouse events.
            # print(event)  # Print event names and attributes.
            if isinstance(event, tcod.event.Quit):
                raise SystemExit()
            elif isinstance(event, tcod.event.WindowResized) and event.type == "WindowSizeChanged":
                pass  # The next call to context.new_console may return a different size.
            elif isinstance(event, tcod.event.KeyDown):
                sym = chr(event.sym.value)
                for action in self.commands:
                    if action.key == sym.upper():
                        return action
                return Command(key=sym.lower())

        return Command(key='')

        # command = input()
        # if command:
        #     command = command[0]
        # for action in self.commands:
        #     if action.key == command.upper():
        #         return action
        # return Command(key=command.lower())
