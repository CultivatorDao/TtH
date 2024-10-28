from input_handler.input_handler import InputHandler
from world.map import Map


class Engine:

    def __init__(self):
        self.character = None
        self.world = Map(engine=self)
        self.input_handler = InputHandler(engine=self)
        self.default_state = None
        self.state = self.default_state
        self.is_on = True

    def main(self):
        while self.is_on:
            self.input_handler.get_command()

    def run(self):
        self.main()

    def exit(self):
        self.is_on = False


eng = Engine()

if __name__ == "__main__":
    eng.run()
