from .map import Map
from entities.objects import Tree


class World:

    def __init__(self, engine):
        self.engine = engine
        # all inanimate entities like trees, rocks, etc.
        self.objects = None
        # Any kind of building like towns, caves, etc.
        self.structures = None
        # all animate entities like mobs including player
        self.mobs = None
        # delete when finished with entity class
        self.character = self.engine.character
        self.map = Map(self)

    @property
    def all_objects(self):
        return [self.character, Tree(world=self)]

