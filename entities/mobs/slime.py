from .mob import Mob


class Slime(Mob):

    def __init__(self, world):
        super().__init__(world)
        self.name = "Slime"
