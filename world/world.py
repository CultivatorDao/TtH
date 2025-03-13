import random

from .map import Map
from .zone_manager import ZoneManager
from .chunk_manager import ChunkManager

from entities.objects import Tree

from entities.mobs.slime import Slime

from .map_generator import MapGenerator


class World:

    def __init__(self, engine):
        self.engine = engine

        self.size = (100, 100)
        self.chunk_size = 50

        self.map_generator = MapGenerator(width=100, height=50, seed=0, tile_size=16, magnification=16)
        self.width = self.map_generator.width * self.map_generator.magnification
        self.height = self.map_generator.height * self.map_generator.magnification

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
        # self.map = Map(self, width=self.size[0], height=self.size[1])
        self.map = Map(self, width=self.width, height=self.height)
        self.all = [self.character, Tree(world=self)]

        self.__chunks_around = None
        self.__chunks_in_sight = None
        self.__zones_around = None

    @property
    def all_objects(self):
        return self.all

    @property
    def chunks_around(self):
        if not self.__chunks_around:
            self.__chunks_around = self.chunk_manager.nearest_chunks(self.character.position.x, self.character.position.y)
        return self.__chunks_around

    @property
    def chunks_in_sight(self):
        if not self.__chunks_in_sight:
            self.__chunks_in_sight = [chunk for chunk in self.chunks_around if self.character.eyesight_shape.intersects_with(chunk)]
        return self.__chunks_in_sight

    @property
    def zones_around(self):
        # return self.zone_manager.get_nearby_zones(self.character)
        if not self.__zones_around:
            zones = []
            for chunk in self.chunks_in_sight:
                zones.extend(chunk.zones)

            self.__zones_around = sorted(set(zones), key=lambda x: x.z_index)

        return self.__zones_around

    def encounter(self):
        if random.randint(0, 1) == 2:
            self.engine.states["Battle"].set_enemy(Slime(None))
            self.engine.change_state("Battle")
