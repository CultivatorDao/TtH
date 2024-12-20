import colorama
import random

from general.shapes import Square, Circle, Ellipse

from entities.objects.tree import Tree
from entities.entity_manager import EntityManager


class Zone:

    def __init__(self,
                 world,
                 x,
                 y,
                 width=30,
                 height=30,
                 z_index=0,
                 objects_frequency=0,
                 structures_frequency=0,
                 mobs_frequency=0,
                 ):

        self.world = world

        self.name = None
        self.z_index = z_index

        self.x = x
        self.y = y

        self.min_width = 20
        self.min_height = 20

        self.width = max(width, self.min_width)
        self.height = max(height, self.min_height)
        self.shape = None

        self.objects = EntityManager(frequency=objects_frequency, types={Tree})
        self.structures = EntityManager()
        self.mobs = EntityManager()

        self.ground_symbol = "~"

    @staticmethod
    def color(color: str, symbol: str):
        return colorama.Fore.__dict__[color.upper()] + symbol + colorama.Fore.RESET

    @classmethod
    def get_all_zones(cls):
        return cls.__subclasses__()

    @property
    def all_entities(self):
        return ()

    def intersects_with(self, zones):
        for zone in zones:
            if self.shape.intersects_with(zone):
                return True
        return False

    def generate(self, zones, number):
        return []

    def generate_entities(self, zones=None):
        for y in range(self.y, self.y + self.height + 1):
            for x in range(self.x, self.x + self.width + 1):
                if self.shape.has_point(x, y):
                    rng = random.randint(1, 100)
                    for entity in (self.mobs, self.objects, self.structures):
                        if entity.frequency >= rng:
                            for entity_type in entity.entity_types:
                                obj = entity_type(world=self.world, x=x, y=y)
                                if obj.frequency >= rng:
                                    entity[(x, y)] = obj


class Ocean(Zone):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Ocean"

        self.shape = Square(x=self.x, y=self.y, side_length=self.width)

        self.ground_symbol = self.color("blue", "~")


class Wastelands(Zone):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Wastelands"

        self.shape = Square(x=self.x, y=self.y, side_length=self.width)

        self.ground_symbol = self.color("green", "~")


class Desert(Zone):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "Desert"

        self.shape = Ellipse(x=self.x, y=self.y, width=self.width, height=self.height)

        self.ground_symbol = self.color("yellow", "~")
        self.generate_entities()


