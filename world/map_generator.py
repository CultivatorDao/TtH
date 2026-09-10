import numpy as np
import math

from noise_generator.cpp_functions import noise, apply_distance_function

from world.map_tile import MapTile

from .biome_distributor import BiomeDistributor, Biome


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

            distance_from_equator = abs(float(y) - (self.height / 2.0))
            normalized_pole_dist = distance_from_equator / (self.height / 2.0)
            latitude_baseline = 1.0 - normalized_pole_dist

            for x in range(chunk_x * self.chunk_width, (chunk_x + 1) * self.chunk_width):
                noise_value = noise(x / self.tile_size,
                                    y / self.tile_size,
                                    self.seed)
                x_cord = x % self.chunk_width
                y_cord = y % self.chunk_height
                altitude = apply_distance_function(
                    noise_value,
                    float(x), float(y), self.width, self.height,
                    _magnification=self.magnification
                )

                if altitude > distributor.mountain_threshold:
                    print("cehcek")
                    biome = Biome(distributor.extreme_biome[3])
                    chunk[x_cord, y_cord] = MapTile(biome)
                    continue
                if altitude < distributor.ocean_level:
                    biome = Biome(distributor.extreme_biome[0])
                    chunk[x_cord, y_cord] = MapTile(biome)
                    continue
                if altitude < distributor.sea_level:
                    biome = Biome(distributor.extreme_biome[1])
                    chunk[x_cord, y_cord] = MapTile(biome)
                    continue
                if altitude < distributor.beach_threshold:
                    biome = Biome(distributor.extreme_biome[2])
                    chunk[x_cord, y_cord] = MapTile(biome)
                    continue


                temperature_noise = noise(x / self.tile_size,
                                    y / self.tile_size,
                                    self.seed)
                moisture_noise = noise(x / self.tile_size,
                                    y / self.tile_size,
                                    self.seed)

                raw_temp = (temperature_noise + 1.0) / 2.0
                raw_moisture = (moisture_noise + 1.0) / 2.0

                # Evaluate low-altitude baseline climate
                temperature = (latitude_baseline * 0.7) + (raw_temp * 0.3)
                land_range = 1.0 - distributor.beach_threshold
                coastal_influence = 1.0 - ((altitude - distributor.beach_threshold) / land_range)
                moisture = (coastal_influence * 0.6) + (raw_moisture * 0.4)
                #

                temperature = max(0, min(1, temperature))
                moisture = max(0, min(1, moisture))

                temperature = distributor.remap(temperature, -1, 1, -50, 50)
                moisture = distributor.remap(moisture, -1, 1, 0, 100)
                # temperature = temperature * 50
                # moisture = ((moisture + 1) / 2) * 100

                # temperature = max(-50, min(50, temperature))
                # moisture = max(0, min(100, moisture))

                biome = distributor.define_biome(temperature, moisture)
                chunk[x_cord, y_cord] = MapTile(biome)

        return chunk
