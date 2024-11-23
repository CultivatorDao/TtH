import colorama

from general.shape import Square, Circle


class Zone:

    def __init__(self,
                 world,
                 x,
                 y,
                 width=30,
                 height=30,
                 ):

        self.world = world

        self.name = None

        self.x = x
        self.y = y

        self.width = width
        self.height = height
        self.shape = None

        self.objects = None
        self.structures = None
        self.mobs = None

        self.ground_symbol = "~"

    @staticmethod
    def color(color: str, symbol: str):
        return colorama.Fore.__dict__[color.upper()] + symbol + colorama.Fore.RESET

    @classmethod
    def get_all_zones(cls):
        return cls.__subclasses__()


class Ocean(Zone):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Ocean"

        self.shape = Square(self.x, self.y, self.world.size[0] + 1)

        self.ground_symbol = self.color("blue", "~")


class Wastelands(Zone):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Wastelands"

        self.shape = Square(self.x, self.y, 30)

        self.ground_symbol = self.color("green", "~")


class Desert(Zone):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Desert"

        self.shape = Circle(self.x, self.y, 10)

        self.ground_symbol = self.color("yellow", "~")


