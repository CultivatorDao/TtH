import random

from .map_generator import MapGenerator
from .map import Map

from entities.mobs.slime import Slime


class World:

    def __init__(self, engine):
        self.engine = engine

        self.size = (100, 100)
        self.chunk_size = 50

        self.map_generator = MapGenerator(width=100, height=50, chunk_width=100, chunk_height=50,
                                          seed=0, tile_size=16, magnification=8)
        self.chunk_width = self.map_generator.chunk_width
        self.chunk_height = self.map_generator.chunk_height
        self.width = self.map_generator.width * self.map_generator.magnification
        self.height = self.map_generator.height * self.map_generator.magnification

        # TODO: Create Entity Manager that will simplify interaction with entities.
        #  For example: MobManager will divide mobs by some biome(range).
        # all inanimate entities like trees, rocks, etc.
        self.objects = None
        # Any kind of building like towns, caves, etc.
        self.structures = None
        # all animate entities like mobs including player
        self.mobs = None

        self.character = self.engine.character

        self.map = Map(self, width=self.width, height=self.height)

    def encounter(self):
        if random.randint(0, 1) == 2:
            self.engine.states["Battle"].set_enemy(Slime(None))
            self.engine.change_state("Battle")
