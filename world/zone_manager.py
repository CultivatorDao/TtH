import random
import random as rn

from .zones.zone import Zone


class ZoneManager:

    def __init__(self, world):

        self.world = world
        self.all_zones = Zone.get_all_zones()
        self.zones = self.generate_zones(7)

    def generate_zones(self, number):

        base = self.all_zones[0](
                world=self.world, x=0, y=0, z_index=0, width=self.world.size[0], height=self.world.size[1]
            )
        padding = 10

        x_offset = base.x + padding, base.width - padding
        y_offset = base.y + padding, base.height - padding

        layer_1 = self.all_zones[1](
            world=self.world, x=x_offset[0], y=y_offset[0], z_index=1,
            width=random.randint(x_offset[1] / 2, x_offset[1]), height=random.randint(y_offset[1] / 2, y_offset[1])
        )

        x_offset = layer_1.x + padding, layer_1.width - padding
        y_offset = layer_1.y + padding, layer_1.height - padding

        zones = [self.all_zones[random.randint(1, 2)](
            world=self.world,
            x=random.randint(*x_offset), y=random.randint(*y_offset),
            width=random.randint(20, x_offset[1]), height=random.randint(20, y_offset[1]), z_index=2
        ) for _ in range(number)]

        zones.append(base)
        zones.append(layer_1)

        return zones

        # return [
        #     self.all_zones[0](
        #         world=self.world, x=0, y=0, z_index=0, width=self.world.size[0], height=self.world.size[1]
        #     ),
        #
        #     self.all_zones[2](
        #         world=self.world, x=20, y=16, z_index=2, width=10, height=20, objects_frequency=100
        #     )
        # ]

    # def get_nearby_zones(self, character):
    #
    #     return [zone for zone in self.zones if character.eyesight_shape.intersects_with(zone.shape)]
