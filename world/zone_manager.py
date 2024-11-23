import random as rn

from .zones.zone import Zone


class ZoneManager:

    def __init__(self, world):

        self.world = world
        self.all_zones = Zone.get_all_zones()
        self.zones = self.generate_zones(3)

    def generate_zones(self, number):
        # all_x = [rn.sample(range(self.world.size[0]), number)]
        # all_y = [rn.sample(range(self.world.size[0]), number)]
        # return [zone(world=self) for zone in self.all_zones]
        return [self.all_zones[0](world=self.world, x=0, y=0), self.all_zones[1](world=self.world, x=15, y=14),
                self.all_zones[2](world=self.world, x=20, y=16)]

    def get_nearby_zones(self, character):

        return [zone for zone in self.zones if character.eyesight_shape.intersects_with(zone.shape)]
