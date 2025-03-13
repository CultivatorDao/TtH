import numpy as np
import random
from noise_generator.cpp_functions import noise, apply_distance_function

from world.map_tile import MapTile

from world.biomes.biome import Range, Ocean, Land


class MapGenerator:

    OCEAN = Range(-1, 0.1)
    BEACH = Range(0.1, 0.15)
    PLAINS = Range(0.1, 1)

    def __init__(self, width=0, height=0, seed=0, tile_size: float = 16.0, magnification: int = 1):
        self.width = width
        self.height = height
        self.seed = seed
        self.tile_size = tile_size * magnification
        self.magnification = magnification

    def define_biome(self, noise_value):
        if self.OCEAN.min <= noise_value < self.OCEAN.max:
            return Ocean()
        if self.PLAINS.min <= noise_value < self.PLAINS.max:
            return Land()

        # for biome in biome_list:
        #     if biome.altitude.in_range(number):
        #         return biome

    def generate(self, octaves=1):
        world_map: np.ndarray = np.zeros(
            (self.width * self.magnification, self.height * self.magnification),
            dtype=MapTile
        )
        start_position = None
        for y in range(self.height * self.magnification):
            for x in range(self.width * self.magnification):
                noise_value = noise(x / self.tile_size,
                                    y / self.tile_size,
                                    self.seed, octaves)
                noise_value = apply_distance_function(
                    noise_value,
                    float(x), float(y), self.width, self.height,
                    _magnification=self.magnification
                )
                biome = self.define_biome(noise_value)
                if isinstance(biome, Land) and random.randint(0, 2) > 0:
                    start_position = x, y
                world_map[x][y] = MapTile(biome.bg_color)

        return world_map, start_position
