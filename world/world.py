import random

from .map import Map
from .zone_manager import ZoneManager
from .chunk_manager import ChunkManager

from entities.objects import Tree

from entities.mobs.slime import Slime


class World:

    def __init__(self, engine):
        self.engine = engine

        self.size = (90, 90)
        self.chunk_size = 30

        self.current_zone = None
        self.zone_manager = ZoneManager(world=self)

        self.chunk_manager = ChunkManager(world=self)

        # TODO: Create Entity Manager that will simplify interaction with entities.
        #  For example: MobManager will divide mobs by some biome(range).
        # all inanimate entities like trees, rocks, etc.
        self.objects = None
        # Any kind of building like towns, caves, etc.
        self.structures = None
        # all animate entities like mobs including player
        self.mobs = None

        self.character = self.engine.character
        self.map = Map(self, width=self.size[0], height=self.size[1])
        self.all = [self.character, Tree(world=self)]

    @property
    def all_objects(self):
        return self.all

    @property
    def zones_around(self):
        return self.zone_manager.get_nearby_zones(self.character)

    def encounter(self):
        if random.randint(0, 1) == 2:
            self.engine.states["Battle"].set_enemy(Slime(None))
            self.engine.change_state("Battle")
