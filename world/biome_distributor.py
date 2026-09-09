class BiomeDistributor:

    def __init__(self):
        self.biomes = (
            ("Meadows", 0.25, 15, 40, 1, (0, 153, 0)),
            ("Deep Ocean", -0.05, 0, 100, 0, (0, 0, 153)),
            ("Ocean", 0.15, 15, 100, 0, (0, 0, 204)),
            ("Beach", 0.2, 20, 90, 1, (238, 234, 121)),
        )

    @staticmethod
    def remap(noise_value, old_min, old_max, new_min, new_max):
        return new_min + ((noise_value - old_min) * (new_max - new_min)) / (old_max - old_min)

    def define_biome(self, altitude, temperature, moisture):
        closest = self.biomes[0]
        min_dist = float('inf')

        for biome in self.biomes:
            dist = (altitude - biome[1])**2 #+ (temperature - biome[2])**2 + (moisture - biome[3])**2

            if dist < min_dist:
                min_dist = dist
                closest = biome

        return Biome(closest)


class Biome:

    def __init__(self, data):
        self.name = data[0]
        self.altitude = data[1]
        self.temperature = data[2]
        self.moisture = data[3]
        self.passability = data[4]
        self.bg_color = data[5]


class EmptyBiome:
    """
        Placeholder for map rendering when map is still loading
    """
    def __init__(self):
        self.name = "Empty"
        self.bg_color = (0, 0, 0)