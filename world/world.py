import random

from .map import Map
from .zone_manager import ZoneManager
from .chunk_manager import ChunkManager

from entities.objects import Tree

from entities.mobs.slime import Slime


class World:

    def __init__(self, engine):
        self.engine = engine

        self.size = (100, 100)
        self.chunk_size = 50

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
    def chunks_around(self):
        return self.chunk_manager.nearest_chunks(self.character.position.x, self.character.position.y)

    @property
    def chunks_in_sight(self):
        return [chunk for chunk in self.chunks_around if self.character.eyesight_shape.intersects_with(chunk)]

    @property
    def zones_around(self):
        # return self.zone_manager.get_nearby_zones(self.character)
        zones = []
        for chunk in self.chunks_in_sight:
            zones.extend(chunk.zones)

        return sorted(set(zones), key=lambda x: x.z_index)

    def encounter(self):
        if random.randint(0, 1) == 2:
            self.engine.states["Battle"].set_enemy(Slime(None))
            self.engine.change_state("Battle")
