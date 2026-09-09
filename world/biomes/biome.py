class Biome:

    def __init__(self):
        self.name = "Name"
        self.altitude = 0
        self.temperature = 0
        self.passability = 0
        self.bg_color = (0, 0, 0)


class Range:

    def __init__(self, min_value, max_value):
        self.min = min_value
        self.max = max_value

    def __call__(self, number):
        return self.in_range(number)

    def in_range(self, number):
        return self.min <= number < self.max

class DeepOcean(Biome):

    def __init__(self):
        super().__init__()
        self.name = "Deep Ocean"
        self.temperature = 0
        self.passability = 1
        self.bg_color = (0, 0, 153)

class Ocean(Biome):

    def __init__(self):
        super().__init__()
        self.name = "Ocean"
        self.temperature = 0
        self.passability = 1
        self.bg_color = (0, 0, 204)

class Beach(Biome):

    def __init__(self):
        super().__init__()
        self.name = "Beach"
        self.temperature = 0
        self.passability = 1
        self.bg_color = (238, 234, 121)

class River(Biome):

    def __init__(self):
        super().__init__()
        self.name = "River"
        self.temperature = 0
        self.passability = 1
        self.bg_color = (0, 0, 204)

class Land(Biome):

    def __init__(self):
        super().__init__()
        self.name = "Land"
        self.temperature = 0
        self.passability = 0
        self.bg_color = (0, 153, 0)


class EmptyBiome(Biome):

    def __init__(self):
        super().__init__()
        self.name = "Empty"
        self.temperature = 0
        self.passability = 0
        self.bg_color = (0, 0, 0)
