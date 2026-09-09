import numpy as np
import math

from noise_generator.cpp_functions import noise, apply_distance_function

from world.map_tile import MapTile

from .biome_distributor import BiomeDistributor


class MapGenerator:

    def __init__(self, width, height, chunk_width, chunk_height,
                 seed=0, tile_size: float = 16.0, magnification: int = 1):
        self.width = width
        self.height = height
        self.chunk_width = chunk_width
        self.chunk_height = chunk_height
        self.seed = seed
        self.tile_size = tile_size * magnification
        self.magnification = magnification

    def get_location(self, min_height, max_height: int = 0):
        if not max_height:
            max_height = min_height

        for y in range(self.height * self.magnification):
            for x in range(self.width * self.magnification):
                height = apply_distance_function(
                    noise(x / self.tile_size, y / self.tile_size, self.seed),
                    float(x), float(y), self.width, self.height,
                    _magnification=self.magnification
                )
                if min_height <= height < max_height:
                    return x, y
        return 0, 0

    def generate_initial_map(self, start_x, start_y, width, height):
        """
        Generates map at start of the game.
        :param start_x:
        :param start_y:
        :param width: in chunks
        :param height: in chunks
        :return: ndarray(width * chunk width, height * chunk height)
        """
        world_map: np.ndarray = np.array([])

        for y in range(start_y // self.chunk_height - height // 2, start_y // self.chunk_height + math.ceil(height / 2)):

            temp_map: np.ndarray = np.array([])
            for x in range(start_x // self.chunk_width - width // 2, start_x // self.chunk_width + math.ceil(width / 2)):
                chunk = self.generate_by_chunk(x, y)
                if temp_map.size == 0:
                    temp_map = chunk
                    continue
                temp_map = np.concatenate((temp_map, chunk), axis=0)

            if world_map.size == 0:
                world_map = temp_map
                continue
            world_map = np.concatenate((world_map, temp_map), axis=1)

        return world_map.reshape((width * self.chunk_width, height * self.chunk_height))

    def generate_by_chunk(self, chunk_x, chunk_y):
        distributor = BiomeDistributor()
        chunk: np.ndarray = np.zeros(
            (self.chunk_width, self.chunk_height), dtype=MapTile
        )
        for y in range(chunk_y * self.chunk_height, (chunk_y + 1) * self.chunk_height):
            for x in range(chunk_x * self.chunk_width, (chunk_x + 1) * self.chunk_width):
                noise_value = noise(x / self.tile_size,
                                    y / self.tile_size,
                                    self.seed)
                temperature = 0
                moisture = 0
                altitude = apply_distance_function(
                    noise_value,
                    float(x), float(y), self.width, self.height,
                    _magnification=self.magnification
                )
                biome = distributor.define_biome(altitude, temperature, moisture)
                chunk[x % self.chunk_width, y % self.chunk_height] = MapTile(biome)

        return chunk
