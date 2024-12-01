import colorama

from general.shapes import Square, Circle, Ellipse


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

        self.min_width = 20
        self.min_height = 20

        self.width = max(width, self.min_width)
        self.height = max(height, self.min_height)
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

    def generate(self):
        pass


class Ocean(Zone):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Ocean"

        self.shape = Square(x=self.x, y=self.y, side_length=60)

        self.ground_symbol = self.color("blue", "~")


class Wastelands(Zone):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Wastelands"

        self.shape = Square(x=self.x, y=self.y, side_length=30)

        self.ground_symbol = self.color("green", "~")


class Desert(Zone):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Desert"

        self.shape = Ellipse(x=self.x, y=self.y, width=10, height=20)

        self.ground_symbol = self.color("yellow", "~")


