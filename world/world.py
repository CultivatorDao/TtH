import random

from .map import Map
from entities.objects import Tree

from entities.mobs.slime import Slime


class World:

    def __init__(self, engine):
        self.engine = engine
        # TODO: Create Entity Manager that will simplify interaction with entities.
        #  For example: MobManager will divide mobs by some biome(range).
        # all inanimate entities like trees, rocks, etc.
        self.objects = None
        # Any kind of building like towns, caves, etc.
        self.structures = None
        # all animate entities like mobs including player
        self.mobs = None
        # delete when finished with entity class
        self.character = self.engine.character
        self.map = Map(self)
        self.all = [self.character, Tree(world=self)]

    @property
    def all_objects(self):
        return self.all

    def encounter(self):
        if random.randint(0, 1) == 1:
            self.engine.states["Battle"].set_enemy(Slime(None))
            self.engine.change_state("Battle")
