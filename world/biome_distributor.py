class BiomeDistributor:

    def __init__(self):
        self.biomes = (
            ("Hot Desert", 40, 5, 1, (255, 128, 0)), ("Savanna", 28, 35, 1, (255, 182, 71)), ("Tropical Rainforest", 26, 90, 1, (102, 204, 0)),
            ("Grassland", 18, 40, 1, (0, 153, 0)), ("Temperate Forest", 14, 70, 1, (76, 153, 0)), ("Swamp", 20, 14, 1, (51, 102, 0)),

            # High-Latitude or Mid-Elevation Biomes
            ("Cold Desert", -5, 10, 1, (153, 255, 255)), ("Taiga", -2, 55, 1, (153, 255, 153)), ("Boreal Forest", 4, 75, 1, (0, 102, 0)),

            # Extreme Alpine / Polar Biomes (Perfect for mountain zones)
            ("Alpine Tundra", -15, 30, 1, (51, 102, 0)),  # High mountains, freezing, sparse growth
            ("Mountain Scree", -12, 10, 1, (0, 153, 153)),  # Freezing, dry, barren exposed rock
            ("Glacial Icecap", -35, 50, 1, (0, 204, 204))  # The absolute peak. Frozen solid.
        )
        self.extreme_biome = (
            ("Deep Ocean", 0, 100, 0, (0, 0, 153)),
            ("Ocean", 15, 100, 0, (0, 0, 204)),
            ("Beach", 20, 90, 1, (238, 234, 121)),
            ("Mountains", 10, 50, 1, (160, 160, 160))
        )
        self.ocean_level = 0.05
        self.sea_level = 0.15
        self.beach_threshold = 0.2
        self.mountain_threshold = 0.45

    @staticmethod
    def remap(noise_value, old_min, old_max, new_min, new_max):
        return new_min + ((noise_value - old_min) * (new_max - new_min)) / (old_max - old_min)

    def define_biome(self, temperature, moisture):
        closest = self.biomes[0]
        min_dist = float('inf')

        for biome in self.biomes:
            dist = (temperature - biome[1])**2 + (moisture - biome[2])**2

            if dist < min_dist:
                min_dist = dist
                closest = biome

        return Biome(closest)


class Biome:

    def __init__(self, data):
        self.name = data[0]
        self.temperature = data[1]
        self.moisture = data[2]
        self.passability = data[3]
        self.bg_color = data[4]


class EmptyBiome:
    """
        Placeholder for map rendering when map is still loading
    """
    def __init__(self):
        self.name = "Empty"
        self.bg_color = (0, 0, 0)